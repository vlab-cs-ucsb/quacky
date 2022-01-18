# Functions and class definitions for translating Azure conditions.

# TODO: fully implement "subattributes"
# i.e. @Resource[...:subattr]

from azure_constraints import azure_action_encoding
from re2smt.re2smt import re2smt
from utilities import comment, declare
import lark

def expr(attr, value, op, smt_lib):
    """
    Convert Azure relational expressions to SMT

    Args:
        attr (str): attribute (key)
        value (str): value
        op (str): Azure relational operator
        smt_lib (bool): use SMT-LIB syntax

    Returns:
        str: SMT encoding
    """

    smt = ' ('

    if 'LessThanEquals' in op:
        smt += '<='
    elif 'LessThan' in op:
        smt += '<'
    elif 'GreaterThanEquals' in op:
        smt += '>='
    elif 'GreaterThan' in op:
        smt += '>'
    elif 'Equals' in op:
        smt += '='
    elif 'Like' in op:
        if smt_lib:
            smt += 'str.in.re'
        else:
            smt += 'in'

    if smt_lib:
        smt += ' ' + attr + ' ' + re2smt(value) + ')'
    else:
        smt += ' ' + attr + ' ' + value + ')'
    
    return smt

# Azure condition interpreter: visits the condition's parse tree
# TODO: support conditions with $, <, >, etc.
class AzureConditionInterpreter(lark.visitors.Interpreter):
    
    def __init__(self, tree, id, smt_lib, enc):
        self.id = id
        self.smt_lib = smt_lib
        self.enc = enc

        self.declarations = set()
        self.body = ''
        self.visit(tree)

    def smt(self):
        # remove extra spaces
        self.body = self.body.replace('( ', '(')
        self.body = self.body.strip()

        body = comment('Condition: {}'.format(self.id))
        body += declare(self.id, 'Bool')
        body += '(assert (= {} {}))\n\n'.format(self.id, self.cond_expr)

        return self.declarations, {}, body

    def start(self, tree):
        self.visit_children(tree)

    def lexp2(self, tree):
        if len(tree.children) > 1:
            self.body += ' (or'

        self.visit_children(tree)

        if len(tree.children) > 1:
            self.body += ')'

    def lexp1(self, tree):
        if len(tree.children) > 1:
            self.body += ' (and'

        self.visit_children(tree)

        if len(tree.children) > 1:
            self.body += ')'

    def lexp0(self, tree):
        if len(tree.children) == 2:
            self.body += ' (not'

        self.visit_children(tree)

        if len(tree.children) == 2:
            self.body += ')'

    def match(self, tree):
        if self.enc:
            self.body += azure_action_encoding(tree.children[0].value[1:-1].lower(), self.smt_lib)
        else:
            self.body += ' (= action {})'.format(tree.children[0].value.lower()) # didn't use expr because of conflict
        
    
    def rexp(self, tree):
        attr  = self.visit(tree.children[0])
        op    = self.visit(tree.children[1])
        value = self.visit(tree.children[2])

        # do some work on attr and value
        if type(attr) == tuple:
            # TODO: change how attrs are declared/used
            if attr[1].endswith(':name') or attr[1].endswith(':path'):
                rtype, subattr = attr[1].split(':')
                
                attr = 'resource'
                
                if 'Not' in op:
                    op = 'StringNotLike'
                else:
                    op = 'StringLike'
                
                value = value.replace('"', '')

                if subattr == 'name':
                    value = '"*/{}/{}/*"'.format(rtype, value)
                elif subattr == 'path':
                    value = '"*/{}/{}"'.format(rtype, value)

            else:
                attr = '.'.join(attr)
                self.declarations.add(declare(attr, 'String'))
        
        if type(op) == str:
            if 'Not' in op:
                self.body += ' (not'
            
            if 'Like' in op:
                value = value.replace('*', '.*')
                value = value.replace('?', '.?')
                value = value.replace('/', '\/')
                value = value.replace('"', '/')
    
            self.body += expr(attr, value, op, self.smt_lib)

            if 'Not' in op[0]:
                self.body += ')'

        # Cartesian products
        else:
            if type(attr) == str:
                attr = {attr}
            
            if op[0] == 'ForAnyOfAnyValues':
                self.body += ' (or'
                
                for a in attr:
                    for b in value:
                        if 'Not' in op[1]:
                            self.body += ' (not'
            
                        if 'Like' in op[1]:
                            b = b.replace('*', '.*')
                            b = b.replace('?', '.?')
                            b = b.replace('"', '/')
            
                        self.body += expr(a, b, op[1], self.smt_lib)

                        if 'Not' in op[1]:
                            self.body += ')' 

            elif op[0] == 'ForAllOfAnyValues':
                self.body += ' (and'
                
                for a in attr:
                    self.body += ' (or'
    
                    for b in value:
                        if 'Not' in op[1]:
                            self.body += ' (not'
            
                        if 'Like' in op[1]:
                            b = b.replace('*', '.*')
                            b = b.replace('?', '.?')
                            b = b.replace('"', '/')
            
                        self.body += expr(a, b, op[1], self.smt_lib)

                        if 'Not' in op[1]:
                            self.body += ')' 

                    self.body += ')'

            elif op[0] == 'ForAnyOfAllValues':
                self.body += ' (and'
                
                for b in value:
                    self.body += ' (or'

                    for a in attr:
                        if 'Not' in op[1]:
                            self.body += ' (not'
            
                        if 'Like' in op[1]:
                            b = b.replace('*', '.*')
                            b = b.replace('?', '.?')
                            b = b.replace('"', '/')
            
                        self.body += expr(a, b, op[1], self.smt_lib)

                        if 'Not' in op[1]:
                            self.body += ')' 

                    self.body += ')'

            if op[0] == 'ForAllOfAllValues':
                self.body += ' (and'
                
                for a in attr:
                    for b in value:
                        if 'Not' in op[1]:
                            self.body += ' (not'
            
                        if 'Like' in op[1]:
                            b = b.replace('*', '.*')
                            b = b.replace('?', '.?')
                            b = b.replace('"', '/')
            
                        self.body += expr(a, b, op[1], self.smt_lib)

                        if 'Not' in op[1]:
                            self.body += ')' 

            self.body += ')'

    def attr(self, tree):
        if len(tree.children) == 1:
            return self.visit(tree.children[0])

        else:
            return (tree.children[0].value,
                    tree.children[1].value)

    def op(self, tree):
        if len(tree.children) == 1:
            return tree.children[0].value
        
        else:
            return (tree.children[0].value,
                    tree.children[1].value)

    def value(self, tree):
        if type(tree.children[0]) == Token:
            return tree.children[0].value

        else:
            return self.visit(tree.children[0])

    def elems(self, tree):
        s = set()

        for child in tree.children:
            s.add(self.visit(child))

        return s

    def elem(self, tree):
        return tree.children[0].value

# Azure condition
class AzureCondition:
    
    def __init__(self, id, value, smt_lib, enc):
        self.id = id.replace(':', '.')
        self.value = value # conditional expression, as string
        self.smt_lib = smt_lib
        self.enc = enc

        cfg = open('azure.lark', 'r')
        cfg_parser = lark.Lark(cfg)
        self.ast = cfg_parser.parse(self.value.replace('\'', '"'))

    def smt(self):
        return AzureConditionInterpreter(self.ast, self.id, self.smt_lib, self.enc).smt()