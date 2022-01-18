# Class definitions for policy model. Each class (or object thereof)
# - represents a node in the tree implementing the policy model.
# - implements .smt(), which encodes the node in SMT-LIB

from aws_conditions import AWSCondition
from aws_constraints import *
from azure_conditions import AzureCondition
from azure_constraints import *
from gcp_conditions import GCPCondition
from gcp_constraints import *
from expressions import expr
from utilities import comment, declare
from re2smt.re2smt import re2smt

lang = 'aws' # Maintain the policy language globally

# Maintain a set of static declarations
static_declarations = {
    declare('principal', 'String'),
    declare('action', 'String'),
    declare('resource', 'String')
}

declarations = set() # Maintain a set of declarations
assertions = set() # Maintain a set of one-time assertions
namespaces = set() # Maintain a set of namespaces across all statements (for AWS)
actions = set() # Maintain a set of actions across all statements (for Azure)

# Principal
class Principal:
    
    def __init__(self, id, obj, is_not, smt_lib):
        self.id = id
        self.obj = obj # principals
        self.is_not = is_not # is NotPrincipal
        self.from_domain = (id == '') # is from a domain file
        self.smt_lib = smt_lib

    # Translate a principal to SMT
    def smt(self):
        body = ''

        if not self.from_domain:
            body += comment('Principal: ' + self.id)
            body += declare(self.id, 'Bool')
        
        body += '(assert'

        # Modify SMT if a principal is specified in a domain file
        if not self.from_domain:
            body += ' (= ' + self.id

        # Handle NotPrincipal
        if self.is_not:
            body += ' (not'

        body += ' (or'
        
        for i in self.obj:
            body += ' ' + expr('principal', i, smt_lib = self.smt_lib)
        
        body += ')'
    
        if self.is_not:
            body += ')'

        if not self.from_domain:
            body += ')'
        
        body += ')\n\n'
    
        return body

# Action   
class Action:

    def __init__(self, id, obj, is_not, smt_lib, enc):
        self.id = id
        self.obj = obj # actions
        self.is_not = is_not # is NotAction
        self.from_domain = (id == '') # is from a domain file
        self.smt_lib = smt_lib
        self.enc = enc
        
        # Add a namespace to the set of namespaces
        global namespaces
        for i in self.obj:
            namespaces.add(i.split(':')[0])
    
    # Translate an action to SMT
    def smt(self):
        body = ''

        if not self.from_domain:
            body += comment('Action: ' + self.id)
            body += declare(self.id, 'Bool')
        
        body += '(assert'

        # Modify SMT if an action is specified in a domain file 
        if not self.from_domain:
            body += ' (= ' + self.id

        # Handle NotAction
        if self.is_not:
            body += ' (not'
    
        body += ' (or'
        
        for i in self.obj:
            global actions
            actions.add(i)

            if i == '*':
                body += ' ' + expr('action', i, smt_lib = self.smt_lib)
            
            elif self.enc:
                # Use action encoding
                i = i.lower()

                if lang == 'aws':
                    body += aws_action_encoding(i, self.smt_lib)
                elif lang == 'azure':
                    body += azure_action_encoding(i, self.smt_lib)
                elif lang == 'gcp':
                    body += gcp_action_encoding(i, self.smt_lib)
            
            else:
                body += ' ' + expr('action', i.lower(), smt_lib = self.smt_lib)    
        
        body += ')'     

        if self.is_not:
            body += ')'
        
        if not self.from_domain:    
            body += ')'

        body += ')\n\n'

        return body

# Resource
class Resource:

    def __init__(self, id, obj, is_not, smt_lib):
        self.id = id
        self.obj = obj # resources
        self.is_not = is_not # is NotResource
        self.from_domain = (self.id == '') # is from a domain file
        self.smt_lib = smt_lib

    # Translate a resource to SMT
    def smt(self):
        body = ''

        if not self.from_domain:
            body += comment('Resource: ' + self.id)
            body += declare(self.id, 'Bool')
        
        body += '(assert'
        
        # Modify SMT if a resource is specified in a domain file
        if not self.from_domain:
            body += ' (= ' + self.id

        # Handle NotResource
        if self.is_not:
            body += ' (not'
    
        body += ' (or'
        
        for i in self.obj:
            body += ' ' + expr('resource', i, smt_lib = self.smt_lib)
        
        body += ')'

        if self.is_not:
            body += ')'

        if not self.from_domain:
            body += ')'
        
        body += ')\n\n'
        
        return body

# Statement
class Statement:

    def __init__(self, id, obj, smt_lib, enc):
        self.id = id
        self.smt_lib = smt_lib
        self.enc = enc
        self.is_allow = (obj['Effect'] == 'Allow') # statement allows
        self.principals = [] # principals
        self.actions = [] # actions
        self.resources = [] # resources
        self.conditions = [] # conditions

        # Handle NotPrincipal
        if 'NotPrincipal' in obj.keys():
            # Handle "NotPrincipal": {...}
            if type(obj['NotPrincipal']) == dict:
                principals = []
                for k, v in obj['NotPrincipal'].items():
                    principals += [i for i in v]

                self.principals.append(Principal('{}.npr'.format(self.id), principals, True, self.smt_lib))

            # Handle "NotPrincipal": [...]
            elif type(obj['NotPrincipal']) == list:
                self.principals.append(Principal('{}.npr'.format(self.id), obj['NotPrincipal'], True, self.smt_lib))
            
            # Handle "NotPrincipal": "*"
            else:
                self.principals.append(Principal('{}.npr'.format(self.id), ['*'], True, self.smt_lib))
                    
        # Handle Principal
        if 'Principal' in obj.keys():
            # Handle "Principal": {...}
            if type(obj['Principal']) == dict:
                principals = []
                for k, v in obj['Principal'].items():
                    principals += [i for i in v]
                
                self.principals.append(Principal('{}.pr'.format(self.id), principals, False, self.smt_lib))

            # Handle "Principal": [...]
            elif type(obj['Principal']) == list:
                self.principals.append(Principal('{}.pr'.format(self.id), obj['Principal'], False, self.smt_lib))

            # Handle "NotPrincipal": "*"
            else:
                self.principals.append(Principal('{}.pr'.format(self.id), ['*'], False, self.smt_lib))
        
        # If no Principal or NotPrincipal, add "Principal": [null]
        if 'NotPrincipal' not in obj.keys() and 'Principal' not in obj.keys():
            self.principals.append(Principal('{}.pr'.format(self.id), ['\x00'], False, self.smt_lib))
        
        # Handle NotAction
        if 'NotAction' in obj.keys():
            self.actions.append(Action('{}.na'.format(self.id), obj['NotAction'], True, self.smt_lib, self.enc))

        # Handle Action
        if 'Action' in obj.keys():
            self.actions.append(Action('{}.a'.format(self.id), obj['Action'], False, self.smt_lib, self.enc))
        
        # If no Action or NotAction (in domain), add "Action": ["*"]
        if 'NotAction' not in obj.keys() and 'Action' not in obj.keys():
            self.actions.append(Action('{}.a'.format(self.id), ['*'], False, self.smt_lib, self.enc))
        
        # Handle NotResource
        if 'NotResource' in obj.keys():
            self.resources.append(Resource('{}.nr'.format(self.id), obj['NotResource'], True, self.smt_lib))

        # Handle Resource
        if 'Resource' in obj.keys():
            self.resources.append(Resource('{}.r'.format(self.id), obj['Resource'], False, self.smt_lib))
        
        # If no Resource or NotResource (in domain), add "Resource": ["*"]
        if 'NotResource' not in obj.keys() and 'Resource' not in obj.keys():
            self.resources.append(Resource('{}.r'.format(self.id), ['*'], False, self.smt_lib))

        # Handle Condition
        if 'Condition' in obj.keys():
            if lang == 'aws':
                # Create a Condition object for each condition operator
                for i in obj['Condition']:
                    for k, v in obj['Condition'][i].items():
                        self.conditions.append(AWSCondition('{}.c{}{}'.format(self.id, i, k), i, k, v, self.smt_lib))
            
            elif lang == 'azure':
                # Create a singleton Condition object
                self.conditions.append(AzureCondition('{}.c'.format(self.id), obj['Condition'][0], self.smt_lib, self.enc))

            elif lang == 'gcp':
                # Create a singleton Condition object
                self.conditions.append(GCPCondition('{}.c'.format(self.id), obj['Condition'][0], self.smt_lib, self.enc))
    
    # Translate a statement to SMT
    def smt(self):
        body = ''

        # Translate all elements to SMT
        for element in self.principals + self.actions + self.resources:
            body += element.smt()

        for condition in self.conditions:
            d, a, b = condition.smt()

            global declarations
            declarations.update(d)

            global assertions
            assertions.update(a)

            body += b

        allows = self.id + '.allows' 
        denies = self.id + '.denies'

        body += comment('Statement: ' + self.id)
        body += declare(allows, 'Bool')
        body += declare(denies, 'Bool')

        # Assert over all elements
        body += '(assert (= '
        
        if self.is_allow:
            body += allows
        else:
            body += denies

        body += ' (and'

        for element in self.principals + self.actions + self.resources + self.conditions:
            body += ' ' + element.id
        
        body += ')))\n'
        body += '(assert (not '
        
        if self.is_allow:
            body += denies
        else:
            body += allows
         
        body += '))\n\n'

        return body

# Policy
class Policy:

    def __init__(self, id, obj, smt_lib, enc):
        self.id = id
        self.smt_lib = smt_lib
        self.enc = enc
        self.statements = []

        if 'Version' in obj:
            global lang
            lang = obj['Version']

        # Handle "Statement": {...}
        if type(obj['Statement']) == dict:
            statement = obj['Statement']
            obj['Statement'] = [statement]

        # Handle "Statement": [...]
        for i in range(len(obj['Statement'])):
            self.statements.append(
                Statement('{}.s{}'.format(self.id, str(i)), obj['Statement'][i], self.smt_lib, self.enc))

    # Translate a policy to SMT
    def smt(self):
        body = ''

        # Translate all statements to SMT
        for statement in self.statements:
            body += statement.smt()

        allows = self.id + '.allows'
        denies = self.id + '.denies'
        neutral = self.id + '.neutral'
        
        body += comment('Policy: ' + self.id)
        body += declare(allows, 'Bool')
        body += declare(denies, 'Bool')
        body += declare(neutral, 'Bool')
        body += '(assert (= {} (and'.format(allows)
        body += ' (not {}) (or'.format(denies)

        for statement in self.statements:
            body += ' ' + statement.id + '.allows'
        
        body += '))))\n'
        body += '(assert (= {} (or'.format(denies)

        for statement in self.statements:
            body += ' ' + statement.id + '.denies'

        body += ')))\n'
        body += '(assert (= {} (and'.format(neutral)
        body += ' (not {})'.format(allows)
        body += ' (not {}))))\n\n'.format(denies)

        return body