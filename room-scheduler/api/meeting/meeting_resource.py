from .meeting_repo import *
from . import Meeting

from flask_restful import Resource
from flask import request

class MeetingResource(Resource):
    def get(self, org_id, meeting_id):
        return get_one(org_id, meeting_id), 200

    def put(self, org_id, meeting_id):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        meeting = Meeting(**request.json)
        meeting.org_id = org_id

        return update(meeting).to_json(), 200

class MeetingListResource(Resource):
    def get(self, org_id):
        return get_many(org_id)

    def post(self, org_id):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        new_meeting = Meeting(**request.json)
        new_meeting.org_id = org_id

        return create(new_meeting).to_json(), 200

class MeetingAttendeesResource(Resource):
    def get(self, org_id, meeting_id):
        return get_attendees(org_id, meeting_id), 200
        
    def post(self, org_id, meeting_id):
        return add_attendee(org_id, meeting_id), 200