# Functions and class definitions for translating AWS condition elements.

from expressions import expr
from re2smt.re2smt import re2smt
from utilities import bit_string, comment, declare, unix_time

# StringEquals
def string_equals(key, values, for_all, smt_lib):
    dtype = 'String'
    
    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in values:
        body += ' ' + expr(key, i, literal = True, smt_lib = smt_lib)

    body += ')'

    return dtype, body

# StringNotEquals
def string_not_equals(key, values, for_all, smt_lib):
    dtype, body = string_equals(key, values, for_all, smt_lib) # use StringEquals

    body = '(not ' + body + ')'

    return dtype, body

# StringEqualsIgnoreCase
def string_equals_ignore_case(key, values, for_all, smt_lib):
    dtype = 'String'
    
    if for_all:
        body = '(and'
    else:
        body = '(or'

    for string in values:
        obj = ''
        
        for i in string:
            obj += '({}|{})'.format(i.upper(), i.lower())

        if smt_lib:
            body += ' (str.in.re {} {})'.format(key, re2smt(obj))
        else:
            body += ' (in {} /{}/)'.format(key, obj)
    
    body += ')'

    return dtype, body

# StringNotEqualsIgnoreCase
def string_not_equals_ignore_case(key, values, for_all, smt_lib):
    dtype, body = string_equals_ignore_case(key, values, for_all, smt_lib) # use StringEqualsIgnoreCase

    body = '(not ' + body + ')'

    return dtype, body

# StringLike
def string_like(key, values, for_all, smt_lib):
    dtype = 'String'
   
    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in range(len(values)):
        body += ' ' + expr(key, values[i], smt_lib = smt_lib) # create a regular expression

    body += ')'

    return dtype, body

# StringNotLike
def string_not_like(key, values, for_all, smt_lib):
    dtype, body = string_like(key, values, for_all, smt_lib) # use StringLike

    body = '(not ' + body + ')'

    return dtype, body

# Helper function for condition operators involving integers
def numeric(key, values, op, for_all, smt_lib):
    dtype = 'Int'
    
    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in values:
        body += ' ' + expr(key, i, op, dtype = dtype, smt_lib = smt_lib)

    body += ')'

    return dtype, body

# NumericEquals
def numeric_equals(key, values, for_all, smt_lib):
    return numeric(key, values, '=', for_all, smt_lib)

# NumericNotEquals
def numeric_not_equals(key, values, for_all, smt_lib):
    dtype, body = numeric_equals(key, values, for_all, smt_lib) # use NumericEquals

    body = '(not ' + body + ')'

    return dtype, body

# NumericLessThan
def numeric_less_than(key, values, for_all, smt_lib):
    return numeric(key, values, '<', for_all, smt_lib)

# NumericLessThanEquals
def numeric_less_than_equals(key, values, for_all, smt_lib):
    return numeric(key, values, '<=', for_all, smt_lib)

# NumericGreaterThan
def numeric_greater_than(key, values, for_all, smt_lib):
    return numeric(key, values, '>', for_all, smt_lib)

# NumericGreaterThanEquals
def numeric_greater_than_equals(key, values, for_all, smt_lib):
    return numeric(key, values, '>=', for_all, smt_lib)

# Helper function for condition operators involving dates
def date(key, values, op, for_all, smt_lib):
    dtype = 'Int'

    if for_all:
        body = '(and'
    else:
        body = '(or'

    # Convert dates to integers from UNIX epoch time
    for i in values:
        body += ' ' + expr(key, unix_time(i), op, dtype = dtype, smt_lib = smt_lib)

    body += ')'

    return dtype, body

# DateEquals
def date_equals(key, values, for_all, smt_lib):
    return date(key, values, '=', for_all, smt_lib)

# DateNotEquals
def date_not_equals(key, values, for_all, smt_lib):
    dtype, body = date_equals(key, values, for_all, smt_lib) # use DateEquals

    body = '(not ' + body + ')'

    return dtype, body

# DateLessThan
def date_less_than(key, values, for_all, smt_lib):
    return date(key, values, '<', for_all, smt_lib)

# DateLessThanEquals
def date_less_than_equals(key, values, for_all, smt_lib):
    return date(key, values, '<=', for_all, smt_lib)

# DateGreaterThan
def date_greater_than(key, values, for_all, smt_lib):
    return date(key, values, '>', for_all, smt_lib)

# DateGreaterThanEquals
def date_greater_than_equals(key, values, for_all, smt_lib):
    return date(key, values, '>=', for_all, smt_lib)

# Bool
def boolean(key, values, for_all, smt_lib):
    dtype = 'Bool'

    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in values:
        body += ' ' + expr(key, str(i).lower(), dtype = dtype)
    
    body += ')'

    return dtype, body

# IpAddress
# TODO: handle IPv6
def ip_address(key, values, for_all, smt_lib):
    dtype = 'IPv4'

    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in values:
        # Convert IP addresses in CIDR notation to a bit string
        addr, prefix = bit_string(i)
        network_part = addr[:prefix]

        # Create a regular expression involving the bit string
        obj = network_part
        obj += '.*'
        
        if smt_lib:
            body += ' (str.in.re {} {})'.format(key, re2smt(obj))
        else:
            body += ' (in {} /{}/)'.format(key, obj)

    body += ')'

    return dtype, body

# NotIpAddress
def not_ip_address(key, values, for_all, smt_lib):
    dtype, body = ip_address(key, values, for_all, smt_lib) # use IpAddress

    body = '(not ' + body + ')'

    return dtype, body

# Null
def if_null(key, values, for_all, smt_lib):
    dtype = 'Bool'

    if for_all:
        body = '(and'
    else:
        body = '(or'

    for i in values:
        body += ' (not ' + expr(key + '.exists', i, dtype = dtype, smt_lib = smt_lib) + ')'
    
    body += ')'

    return dtype, body

# Map condition operators to functions in operators.py
ops = {
    'StringEquals': string_equals,
    'StringNotEquals': string_not_equals,
    'StringEqualsIgnoreCase': string_equals_ignore_case,
    'StringNotEqualsIgnoreCase': string_not_equals_ignore_case,
    'StringLike': string_like,
    'StringNotLike': string_not_like,
    'NumericEquals': numeric_equals,
    'NumericNotEquals': numeric_not_equals,
    'NumericLessThan': numeric_less_than,
    'NumericLessThanEquals': numeric_less_than_equals,
    'NumericGreaterThan': numeric_greater_than,
    'NumericGreaterThanEquals': numeric_greater_than_equals,
    'DateEquals': date_equals,
    'DateNotEquals': date_not_equals,
    'DateLessThan': date_less_than,
    'DateLessThanEquals': date_less_than_equals,
    'DateGreaterThan': date_greater_than,
    'DateGreaterThanEquals': date_greater_than_equals,
    'Bool': boolean,
    'BinaryEquals': string_equals,
    'IpAddress': ip_address,
    'NotIpAddress': not_ip_address,
    'ArnEquals': string_equals,
    'ArnNotEquals': string_not_equals,
    'ArnLike': string_like,
    'ArnNotLike': string_not_like,
    'Null': if_null
}

class AWSCondition:

    def __init__(self, id, op, key, values, smt_lib):
        self.id = id.replace(':', '.')
        self.op = op # condition operator
        self.key = key.replace(':', '.') # condition key
        self.values = values # values for condition key
        self.smt_lib = smt_lib
   
    # Translate a condition to SMT
    def smt(self):
        body = comment('Condition: ' + self.id)

        # Handle the ForAny/AllValues condition operators
        # e.g. ForAllValues:StringLike
        op = self.op
        op = op.replace('ForAllValues:', '')
        op = op.replace('ForAnyValues:', '')

        # Handle the IfExists condition operator
        # e.g. StringLikeIfExists
        if 'IfExists' in self.op:
            op = op.replace('IfExists', '')
        
        dtype, smt = ops[op](self.key, self.values, ('All' in self.op), self.smt_lib)

        # Add declared condition keys to declarations
        # e.g. s3.prefix, s3.prefix.exists
        declarations = set()

        if 'Null' not in self.op:
            if 'IP' in dtype:
                declarations.add(declare(self.key, 'String')) # treat IP addresses as integers
            else:
                declarations.add(declare(self.key, dtype))
        
        declarations.add(declare(self.key + '.exists', 'Bool'))
        body += declare(self.id, 'Bool')

        # Assert that a string does not "exist" if it is null
        assertions = set()

        if dtype == 'String':
            assertions.add('(assert (= {}.exists (not {})))\n'.format(self.key, expr(self.key, '\x00', smt_lib = self.smt_lib)))
        
        # Assert that an IP address is valid
        elif 'IP' in dtype:
            if dtype == 'IPv4':
                obj = '[01]{32,32}'
            elif dtype == 'IPv6':
                obj = '[01]{128,128}'

            if self.smt_lib:
                assertions.add('(assert (str.in.re {} {}))\n'.format(self.key, re2smt(obj)))
            else:
                assertions.add('(assert (in {} /{}/))\n'.format(self.key, obj))
        
        body += '(assert (= {}'.format(self.id)
        
        # Handle the IfExists condition operator
        # e.g. StringLikeIfExists
        if 'IfExists' in self.op:
            body += ' (=> {}.exists {})'.format(self.key, smt)
        else:
            if 'Null' not in self.op:
                body += ' (and {}.exists {})'.format(self.key, smt)
            else:
                body += ' ' + smt

        body += '))\n\n'

        return declarations, assertions, body