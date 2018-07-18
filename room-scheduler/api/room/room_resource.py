from flask_restful import Resource

class RoomResource(Resource):
    def get(self, org_id, room_number):
        return "Not Implemented", 501

    def put(self, org_id, room_number):
        return "Not Implemented", 501

class RoomListResource(Resource):
    def get(self, org_id):
        return "Not Implemented", 501

    def post(self, org_id):
        return "Not Implemented", 501

class RoomScheduleResource(Resource):
    def get(self, org_id, room_number):
        return 'Not implemented', 501