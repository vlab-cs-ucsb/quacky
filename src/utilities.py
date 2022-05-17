# Utility functions

from datetime import datetime
from ipaddress import IPv4Address
from ipaddress import IPv6Address
from utils.Shell import Shell
import itertools
import json
import re

def header():
    """
    Build SMT formula header

    Returns:
        str: SMT header
    """

    smt = '(set-logic ALL)\n'
    smt += '(set-option :produce-models true)\n\n'

    return smt

def footer(id1, id2 = None):
    """
    Build SMT formula footer

    Args:
        id1 (str): ID of policy 1 in SMT formula
        id2 (str, optional): ID of policy 2 in SMT formula. Defaults to None.

    Returns:
        str: SMT footer
    """

    smt = '(assert {}.allows)\n'.format(id1)

    if id2:
        smt += '(assert (or {0}.denies {0}.neutral))\n'.format(id2)

    smt += '(check-sat)\n'
    smt += '(get-model)\n'

    return smt

def comment(value):
    """
    Create a SMT comment

    Args:
        value (str): value of comment

    Returns:
        str: comment
    """

    return '; ' + value + '\n'

def declare(id, dtype):
    """
    Create a SMT declaration

    Args:
        id (str): variable name
        dtype (str): variable type

    Returns:
        str: declaration
    """
    
    return '(declare-const ' + id + ' ' + dtype + ')\n'

def bit_string(ip):
    """
    Translate CIDR IP address to a bit string (really just a string)

    Args:
        ip (str): IP address

    Returns:
        str: bit string
        int: number of bits in CIDR prefix
    """

    ip = ip.split('/')

    addr = ip[0]
    if ':' in addr:
        v6 = True
        addr = bin(int(IPv6Address(addr)))
    else:
        v6 = False
        addr = bin(int(IPv4Address(addr)))

    addr = addr.replace('0b', '')

    if v6 and len(addr) < 128:
        addr += '0' * (128 - len(addr))

    elif not v6 and len(addr) < 32:
        addr += '0' * (32 - len(addr))

    if len(ip) > 1:
        prefix = ip[1]
    else:
        prefix = len(addr)

    return addr, int(prefix)

def unix_time(obj):
    """
    Convert a date into an int from UNIX epoch time

    Args:
        obj (str): date

    Returns:
        str: UNIX epoch time
    """

    t = datetime.strptime(obj, '%Y-%m-%dT%H:%M:%SZ').timestamp()
    return str(round(t))

def disjunction_to_ranges(obj, lang='aws'):
    """
    Convert a disjunction constraint to a range constraint.
    Used in action encoding.
    e.g. action in {1, 2, 3, 4} => 1 <= action <= 4

    Args:
        obj (list): elements in disjunction

    Returns:
        list: ranges
    """

    obj = [int(n) for n in obj] # preprocess obj
    
    if lang == 'gcp':
        D = 3
    else:
        D = 5

    ranges = list()

    # magic
    for a, b in itertools.groupby(enumerate(obj), lambda x : x[1] - x[0]):
        b = list(b)
        if b[0][1] == b[-1][1]:
            ranges.append(str(b[0][1]).zfill(D))
        else:
            ranges.append((str(b[0][1]).zfill(D), str(b[-1][1]).zfill(D)))

    disjunction_ops = len(obj) + 1 # len "="s and 1 "or"
    ranges_ops = len(ranges) + 1 # len "and"s or "="s and 1 "or"
    ranges_ops += 2 * len([r for r in ranges if type(r) == tuple]) # len ">="s and "<="s
        
    if disjunction_ops < ranges_ops:
        return [str(n).zfill(D) for n in obj]
    else:
        return ranges

def get_abc_result_line(out, err):
    """
    Parse ABC results from stdout and stderr (from VLab)

    Args:
        out (str): stdout dump
        err (str): stderr dump

    Returns:
        dict: ABC results
    """

    lines = err.strip(' \t\n\r,').split('\n')
    var_results = {}
    results = {}
    for line in lines:
        match = re.match(
            r".*report is_sat:\s*(?P<is_sat>\w+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line,     re.IGNORECASE)
        if match:
            results["is_sat"] = match.group('is_sat')
            results["solve_time"] = match.group('time')
            continue

        match = re.match(
            r".*report \(TUPLE\) bound:\s*(?P<bound>\d+)\s*count:\s*(?P<count>\d+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line, re.IGNORECASE)
        if match:
            results["bound"] = match.group('bound')
            results["count"] = match.group('count')
            results["count_time"] = match.group('time')

        match = re.match(
            r".*report bound:\s*(?P<bound>\d+)\s*count:\s*(?P<count>\d+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line, re.IGNORECASE)
        if match:
            if "var" in results:
                var_results[results["var"]] = {"bound": match.group(
                    'bound'), "count": match.group('count'),     "count_time": match.group('time')}
            continue

        match = re.match(r".*report var:\s*(?P<var>.+)\s*",
                         line, re.IGNORECASE)
        if match:
            results["var"] = match.group('var')
            continue

    results["var"] = var_results
    return results

def get_variables(fname):
    """
    Infer variables from SMT formula.
    Args:
        fname (str): file name of SMT formula
    Returns:
        list: variables
    """

    formula = open(fname, 'r').read()
    variables = []

    for dtype in ['String', 'Int']:
        pattern = 'declare-const ([A-Za-z0-9\.]+) {}'.format(dtype)
        variables += re.findall(pattern, formula)

    return variables

def get_results(fname, bound, shell, timeout = None):
    """
    Run ABC and get results.
    Args:
        fname ([str): file name
        bound (str): bound
        timeout (int): timeout, in seconds
    Returns:
        dict: results
    """

    variables = get_variables(fname)

    cmd = ''
    
    if timeout:
        cmd += 'timeout -k {0}s {0}s '.format(timeout)
    
    cmd += 'abc -i {}'.format(fname)
    cmd += ' -bs {0}'.format(bound)
    cmd += ' --precise --count-tuple --count-variable {} -v 0'.format(','.join(variables))
    
    out, err = shell.runcmd(cmd)

    # Parse ABC output
    results = get_abc_result_line(out, err)

    return results