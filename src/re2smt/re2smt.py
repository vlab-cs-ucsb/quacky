# RE2SMT: translates PCRE regex to SMT-LIB

from lark import *
import re

# Visitor for PCRE regex grammar
class PCREInterpreter(visitors.Interpreter):
    def __init__(self, tree):
        self.smt = ''
        self.in_range = False
        self.visit(tree)

    def __str__(self):
        return self.smt.strip()

    def metacharacters(self, tree):
        self.smt += ' (str.to.re "'
        self.smt += tree.children[0].value
        self.smt += '")'

    def square_metacharacters(self, tree):
        self.smt += ' (str.to.re "'
        self.smt += tree.children[0].value
        self.smt += '")'
    
    def char_types(self, tree):
        self.smt += ' (str.to.re "'
        self.smt += tree.children[1].value
        self.smt += '")'

    def escaped_square_simple_value(self, tree):
        if not self.in_range:
            self.smt += ' (str.to.re "'
        
        self.smt += tree.children[1]

        if not self.in_range:
            self.smt += '")'

    def escaped_square_metacharacters(self, tree):
        self.visit_children(tree)

    def square_base_value(self, tree):
        if not self.in_range:
            self.smt += ' (str.to.re "'

        self.smt += tree.children[0]

        if not self.in_range:
            self.smt += '")'

    def range_literal_value(self, tree):
        self.visit_children(tree)

    def square_literal_value(self, tree):
        self.visit_children(tree)

    def range(self, tree):
        self.in_range = True
        self.smt += ' (re.range "'
        self.visit(tree.children[0])
        self.smt += '" "'
        self.visit(tree.children[2])
        self.smt += '")'
        self.in_range = False

    def positive_class(self, tree):
        self.visit_children(tree)
    
    def char_class(self, tree):
        if len(tree.children) > 3:
            self.smt += ' (re.union'
        
        self.visit_children(tree)
        
        if len(tree.children) > 3:
            self.smt += ')'

    def escaped_simple_value(self, tree):
        self.smt += ' (str.to.re "'
        self.smt += tree.children[1]
        self.smt += '")'

    def escaped_meta_value(self, tree):
        self.visit_children(tree)
        
    def base_value(self, tree):
        self.smt += ' (str.to.re "'
        self.smt += tree.children[0]
        self.smt += '")'

    def literal_value(self, tree):
        self.visit_children(tree)

    def all_char(self, tree):
        self.smt += ' re.allchar'

    def base_pattern(self, tree):
        self.visit_children(tree)

    def inter_pattern(self, tree):
        self.smt += ' (re.inter'
        self.visit_children(tree)
        self.smt += ')'
        
    def union_pattern(self, tree):
        self.smt += ' (re.union'
        self.visit_children(tree)
        self.smt += ')'

    def complement_pattern(self, tree):
        self.smt += ' (re.complement'
        self.visit_children(tree)
        self.smt += ')'

    def subpattern(self, tree):
        self.visit_children(tree)

    def captured_pattern(self, tree):
        self.visit_children(tree)

    def repetition_pattern_base(self, tree):
        self.visit_children(tree)

    def repetition_pattern(self, tree):
        self.visit(tree.children[1])
        self.visit(tree.children[0])
        self.smt += ')'

    def quantifier(self, tree):
        if 'KLEENE' in tree.children[0].type:
            self.smt += ' (re.' + tree.children[0].value
        elif 'ZO' in tree.children[0].type:
            self.smt += ' (re.opt'
        else:
            self.smt += ' ((_ re.loop'
            self.smt += ' ' + tree.children[0]

            if len(tree.children) > 1:
                self.smt += ' ' + tree.children[1]

            self.smt += ')'

    def non_greedy_quantifier(self, tree):
        self.visit_children(tree)

    def pattern(self, tree):
        if len(tree.children) > 1:
            self.smt += ' (re.++'

        self.visit_children(tree)
        
        if len(tree.children) > 1:
            self.smt += ')'

    def start(self, tree):
        self.visit_children(tree)

def re2smt(obj):
    """
    Translate PCRE regex into SMT-LIB

    Args:
        obj (str): PCRE regex

    Returns:
        str: SMT-LIB regex
    """

    grammar = open('re2smt/pcre.lark', 'r').read()
    pcre_parser = Lark(grammar)
    ast = pcre_parser.parse(obj)
    
    return str(PCREInterpreter(ast))