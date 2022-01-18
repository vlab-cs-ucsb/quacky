# Functions and class definitions for translating GCP conditions

from utilities import comment, declare
import celpy
import lark
import re

# Mapping of supported attributes to types
attrs = {
    'resource.service': 'String',
    'resource.type': 'String',
    'resource.name': 'String',
    'request.time': 'Int',
    'request.path': 'String',
    'destination.ip': 'String',
    'destination.port': 'Int',
    'request.host': 'String'
}

# CEL interpreter: visits the GCP condition parse tree
class CELInterpreter(lark.visitors.Interpreter):
    
    def __init__(self, tree, id, smt_lib, enc):
        self.id = id
        self.smt_lib = smt_lib
        self.enc = enc

        self.body = ''
        self.visit(tree)

    def smt(self):
        # remove extra spaces
        self.body = self.body.replace('( ', '(')
        self.body = self.body.strip()

        body = comment('Condition: {}'.format(self.id))
        body += declare(self.id, 'Bool')
        body += '(assert (= {} {}))\n\n'.format(self.id, self.body)

        decls = set()

        # Handle conditions on resource type, name, service
        for attr, dtype in attrs.items():
            if attr not in self.body:
                continue

            if attr in ['resource.service', 'resource.type']:
                matches = re.findall('= {} "([^"]+)"'.format(attr), self.body)
                
                for match in matches:
                    if self.smt_lib:
                        scope = '(re.++ (re.* re.allchar) (str.to.re "/") (str.to.re "{}") (str.to.re "/") (re.* re.allchar))'.format(match)
                        expr = 'str.in.re resource ' + scope

                    else:
                        scope = '.*/{}/.*'.format(match)
                        scope = scope.replace('//', '/')
                        scope = scope.replace('/', '\\/')
                        scope = '/' + scope + '/'
                        expr = 'in resource ' + scope

                    self.body = self.body.replace('= {} "{}"'.format(attr, match), expr)

            elif attr == 'resource.name':
                matches = re.findall('= {} "([^"]+)"'.format(attr), self.body)
                
                for match in matches:
                    self.body = self.body.replace('= {} "{}"'.format(attr, match), '= resource "{}"'.format(match))
            
            if True: # else
                decls.add('(declare-const {} {})'.format(attr, dtype))

        return decls, {}, body

    def expr(self, tree):
        self.visit_children(tree)

    def conditionalor(self, tree):
        if len(tree.children) > 1:
            self.body += ' (or'

        self.visit_children(tree)

        if len(tree.children) > 1:
            self.body += ')'

    def conditionaland(self, tree):
        if len(tree.children) > 1:
            self.body += ' (and'

        self.visit_children(tree)

        if len(tree.children) > 1:
            self.body += ')'

    def relation(self, tree):
        self.visit_children(tree)

        # not
        if tree.children[0].data == 'relation_ne':
            self.body += '))'

        # other relational ops
        elif 'relation' in tree.children[0].data:
            self.body += ')'

    def relation_lt(self, tree):
        self.body += ' (<'
        self.visit_children(tree)

    def relation_le(self, tree):
        self.body += ' (<='
        self.visit_children(tree)

    def relation_gt(self, tree):
        self.body += ' (>'
        self.visit_children(tree)

    def relation_ge(self, tree):
        self.body += ' (>='
        self.visit_children(tree)

    def relation_eq(self, tree):
        self.body += ' (='
        self.visit_children(tree)

    def relation_ne(self, tree):
        self.body += ' (not (='
        self.visit_children(tree)

    def addition(self, tree):
        self.visit_children(tree)

        # for + or -
        if len(tree.children) > 1:
            self.body += ')'

    def addition_add(self, tree):
        self.body += ' (+'
        self.visit_children(tree)

    def addition_sub(self, tree):
        self.body += ' (-'
        self.visit_children(tree)

    def multiplication(self, tree):
        self.visit_children(tree)

    def unary(self, tree):
        self.visit_children(tree)

    def unary_not(self, tree):
        self.body += ' (not'
        self.visit_children(tree)
        self.body += ')'

    def member(self, tree):
        self.visit_children(tree)

    def member_dot(self, tree):
        self.visit(tree.children[0])
        self.body += '.'
        self.body += tree.children[1].value

    def member_dot_arg(self, tree):
        self.visit(tree.children[0])
        self.body += '.'
        self.body += tree.children[1].value
        self.body += '('
        
        if len(tree.children) > 2:
            self.visit(tree.children[2])
        
        self.body += ')'

    def primary(self, tree):
        self.visit_children(tree)

    def dot_ident(self, tree):
        self.body += '.'
        self.body += tree.children[0].value

    def dot_ident_arg(self, tree):
        self.body += '.'
        self.body += tree.children[0].value
        self.body += '('
        
        if len(tree.children) > 1:
            self.visit(tree.children[1])
        
        self.body += ')'

    def ident(self, tree):
        self.body += ' ' + tree.children[0].value

    def ident_arg(self, tree):
        self.body += ' ' + tree.children[0].value
        self.body += '('
        
        if len(tree.children) > 1:
            self.visit(tree.children[1])
    
        self.body += ')'
    
    def paren_expr(self, tree):
        self.visit_children(tree)

    def exprlist(self, tree):
        self.visit(tree.children[0])
    
    def literal(self, tree): 
        self.body += ' ' + tree.children[0].value

# GCP condition
class GCPCondition:

    def __init__(self, id, value, smt_lib, enc):
        self.id = id.replace(':', '.')
        self.value = value
        self.smt_lib = smt_lib
        self.enc = enc

        env = celpy.Environment()
        self.ast = env.compile(self.value)

    def smt(self):
        return CELInterpreter(self.ast, self.id, self.smt_lib, self.enc).smt()
