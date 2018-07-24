from .. import run_query, Event
from . import Person

def get_one(org_id, username):
    query = '''
        SELECT org_id, username, first_name, last_name, email, role_id, role_name
        FROM person, role
        WHERE person.role = role.role_id 
        AND org_id = %(org_id)s AND username = %(username)s;
    '''

    params = { 'org_id': org_id, 'username':username }

    return run_query(query, params, Person)

def get_many(org_id):
    pass

def create(person_obj):
    pass

def update(person_obj):
    pass

def get_schedule(org_id, username):
    pass