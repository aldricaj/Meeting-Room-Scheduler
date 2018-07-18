from flask_restful import Resource

class MeetingResource(Resource):
    def get(self, org_id, meeting_id):
        return "Not Implemented", 501

    def put(self, org_id, meeting_id):
        return "Not Implemented", 501

class MeetingListResource(Resource):
    def get(self, org_id):
        return "Not Implemented", 501

    def post(self, org_id):
        return "Not Implemented", 501

class MeetingAttendeesResource(Resource):
    def get(self, org_id, meeting_id):
        return 'Not implemented', 501
        
    def post(self, org_id, meetin_id):
        return 'Not implemented', 501