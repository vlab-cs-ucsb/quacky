# Functions for building SMT-LIB expressions

from re2smt.re2smt import re2smt

# characters to escape
symbols = ['@', '/', '-', '.', '^', '$', '{', '}', '[', ']', '(', ')'] 

# Create a regular expression
def regexpr(obj, smt_lib):
    """
    Create a SMT regular expression

    Args:
        obj (str): pattern
        smt_lib (bool): use SMT-LIB syntax

    Returns:
        str: regular expression
    """
    # escape characters
    for symbol in symbols:
        obj = obj.replace(symbol, '\\' + symbol)

    obj = obj.replace('*', '.*')
    obj = obj.replace('?','.')

    if smt_lib:
        return re2smt(obj)
    else:
        return obj

def expr(key, val, op = '=', dtype = 'String', literal = False, smt_lib = False):
    """
    Create a simple expression with an operator and 2 operands
    e.g. (< x 5) or (= s3.prefix "foo")
    
    Args:
        key (str): key (left operand)
        val (str): value (right operand)
        op (str, optional): operator. Defaults to '='.
        dtype (str, optional): key/value type. Defaults to 'String'.
        literal (bool, optional): treat wildcards literally. Defaults to False.
        smt_lib (bool, optional): use SMT-LIB syntax. Defaults to False.

    Returns:
        str: SMT encoding of expression
    """

    smt = ''

    # Create a regular expression instead
    if dtype == 'String' and ('*' in val or '?' in val) and not literal:
        if smt_lib:
            smt += '(str.in.re {} {})'.format(key, regexpr(val, True))
        else:
            smt += '(in {} /{}/)'.format(key, regexpr(val, False))
    
    else:
        smt += '({} {} '.format(op, key)
        
        # Add quotation marks if expression involves a string
        if dtype == 'String':
            smt += '"'

        smt += str(val)

        if dtype == 'String':
            smt += '"'
        
        smt += ')'

    return smt