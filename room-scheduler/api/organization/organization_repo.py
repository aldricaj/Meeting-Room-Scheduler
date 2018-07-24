from .. import run_query
from . import Organization

def get_one(org_id):
    query = '''
        SELECT org_id, org_name
        FROM organization
        WHERE org_id = %s;
    '''

    param = [org_id]

    result = run_query(query, param, Organization)

    return result



def get_many():
    query = '''
        SELECT org_id, org_name
        FROM organization;
    '''

    result = run_query(query, None, Organization)

    return result


def update(organization):
    pass

def create(organization):
    query = '''
        INSERT INTO organization(org_name)
        VALUES (%(org_name)s);

        SELECT org_id, org_name
        FROM organization
        WHERE org_id = LASTVAL();
    '''
    params = organization.__dict__
    return run_query(query, params)