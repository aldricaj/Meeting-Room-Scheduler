from .. import run_query, Event
from . import Room

def get_one(org_id, room_number):
    query = '''
        SELECT org_id, room_number, room.av_type_id, room.av_type_name
        FROM room, av_type
        WHERE room.av_type_id = av_type.av_type_id 
        AND org_id = %(org_id)s
        AND room_number = %(room_number)s;
    '''
    params = {'org_id':org_id, 'room_number': room_number}

    return run_query(query, params, Room)[0]

def get_many(org_id):
    query = '''
        SELECT org_id, room_number, room.av_type_id, room.av_type_name
        FROM room, av_type
        WHERE room.av_type_id = av_type.av_type_id;
    '''
    params = {'org_id':org_id }

    return run_query(query, params, Room)

def create(room_obj):
    query = '''
        INSERT INTO room(org_id, room_number, av_type_id)
        VALUES (%(org_id)s, %(room_number)s, %(av_type_id)s);

        SELECT org_id, room_number, room.av_type_id, room.av_type_name
        FROM room, av_type
        WHERE room.av_type_id = av_type.av_type_id 
        AND org_id = %(org_id)s
        AND room_number = %(room_number)s;
    '''
    return run_query(query, room_obj.__dict__, Room)

def update(room_obj):
    pass

def get_schedule(org_id, room_number):
    query = '''
        SELECT 
            meeting_id, 
            meeting_start AS start, 
            meeting_end AS end, 
            meeting_title AS title, 
            room_number,
            owner_username
        FROM Meeting
        WHERE
            meeting.org_id = %(org_id)s 
            AND room_number = %(room_number)s;
    '''

    params = {'org_id': org_id, 'room_number':room_number}

    return run_query(query, params, Event)
