from .. import run_query, Event
from . import Meeting, MeetingAttendee

def get_one(org_id, meeting_id):
    query = '''
        SELECT 
            meeting_id,
            org_id,
            owner_username,
            meeting_start,
            meeting_end,
            meeting_title,
            room_number
        FROM meeting
        WHERE org_id = %(org_id)s
        AND meeting_id = %(meeting_id)s;
    '''

    params = {'org_id': org_id, 'meeting_id': meeting_id}

    return run_query(query, params, Meeting)

def get_many(org_id):
    query = '''
        SELECT 
            meeting_id,
            org_id,
            owner_username,
            meeting_start,
            meeting_end,
            meeting_title,
            room_number
        FROM meeting
        WHERE org_id = %(org_id)s;
    '''

    params = {'org_id': org_id }

    return run_query(query, params, Meeting)

def create(meeting_obj):
    query = '''
        INSERT INTO meeting(meeting_id,
            org_id,
            owner_username,
            meeting_start,
            meeting_end,
            meeting_title,
            room_number)
        VALUES (%(org_id)s, %(owner_username)s, %(meeting_start)s, %(meeting_end)s
        %(meeting_title)s, %(room_number)s);

        SELECT 
            meeting_id,
            org_id,
            owner_username,
            meeting_start,
            meeting_end,
            meeting_title,
            room_number
        FROM meeting
        WHERE org_id = %(org_id)s
        AND meeting_id = %(meeting_id)s;
    '''

    params = meeting_obj.__dict__

    return run_query(query, params, Meeting) 



def update(meeting_obj):
    pass

def get_attendees(org_id, meeting_id):
    query = '''
        SELECT person.org_id, person.username, first_name, last_name, email
        FROM MeetingAttendees, person
        WHERE person.org_id = MeetingAttendees.org_id 
        AND person.username = MeetingAttendees.username
        AND MeetingAttendees.org_id = 
    '''
    pass
	
def add_attendees(org_id, meeting_id):
    pass