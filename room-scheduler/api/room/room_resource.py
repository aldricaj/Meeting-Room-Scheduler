from .room_repo import *
from . import Room

from flask_restful import Resource
from flask import request

class RoomResource(Resource):
    def get(self, org_id, room_number):
        return get_one(org_id, room_number), 200

    def put(self, org_id, room_number):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        room = Room(**request.json)
        room.org_id = org_id

        return update(room).to_json(), 200

class RoomListResource(Resource):
    def get(self, org_id):
        return get_many(org_id)

    def post(self, org_id):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        new_room = Room(**request.json)
        new_room.org_id = org_id

        return create(new_room).to_json(), 200

class RoomScheduleResource(Resource):
    def get(self, org_id, room_number):
        return get_schedule(org_id, room_number), 200