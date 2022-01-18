# Functions for backend (i.e. translating policy model to SMT).

from policy_model import *
from aws_constraints import *
from azure_constraints import *
from gcp_constraints import *
from expressions import expr

def visit_policy_model(obj, domain, from_domain, smt_lib, enc, cnstr):
    """
    Construct a policy model tree and visit it

    Args:
        obj (dict): policy or policies
        domain (dict): not supported
        from_domain (bool): not supported
        smt_lib (bool): use SMT-LIB syntax
        enc (bool): use action encoding
        cnstr (bool): add resource type constraints

    Returns:
        str: SMT encoding of policies
    """

    header = ''
    body = ''

    # Add all SMT translations for the policies
    if 'policies' in obj.keys():
        p0 = obj['policies'][0]
        lang = p0['Version'] if 'Version' in p0 else 'aws'
        body += Policy('p0', obj['policies'][0], smt_lib, enc).smt()
        body += Policy('p1', obj['policies'][1], smt_lib, enc).smt()    
    else:
        lang = obj['Version'] if 'Version' in obj else 'aws'
        body += Policy('p0', obj, smt_lib, enc).smt()

    # Add all SMT translations for the domain
    if 'Principal' in domain.keys():
        body += Principal('', domain['Principal'], False, smt_lib).smt()
    
    if 'Resource' in domain.keys():
        body += Resource('', domain['Resource'], False, smt_lib).smt()

    if 'Condition' in domain.keys():
        for i in domain['Condition']:
            body += '(assert (and {}.exists (or'.format(i.replace(':', '.'))

            for j in domain['Condition'][i]:
                if j.isdigit():
                    dtype = 'Int'
                elif j in ['true', 'false']:
                    dtype = 'Bool' 
                else:
                    dtype = 'String'

                body += ' ' + expr(i.replace(':', '.'), j, dtype = dtype, smt_lib = smt_lib)
            
            body += ')))\n'
        body += '\n'

    # Add all declarations to the header of the SMT formula
    for declaration in static_declarations:
        header += declaration

    if not from_domain:
        for declaration in declarations:
            header += declaration

    # Add resource type constraints
    if cnstr:
        if lang == 'aws':
            body += aws_type_constraints(namespaces, smt_lib, enc)
        elif lang == 'azure':
            body += azure_type_constraints(actions, smt_lib, enc)
        elif lang == 'gcp':
            body += gcp_type_constraints(actions, smt_lib, enc)

    smt = header + '\n' + ''.join(assertions) + '\n' + body + '\n'
    
    return smt
