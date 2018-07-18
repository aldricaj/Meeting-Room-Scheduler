from flask_restful import Resource

class PersonResource(Resource):
    def get(self, org_id, username):
        return "Not Implemented", 501

    def put(self, org_id, username):
        return "Not Implemented", 501

class PersonListResource(Resource):
    def get(self, org_id):
        return "Not Implemented", 501

    def post(self, org_id):
        return "Not Implemented", 501

class PersonScheduleResource(Resource):
    def get(self, org_id, username):
        return 'Not implemented', 501