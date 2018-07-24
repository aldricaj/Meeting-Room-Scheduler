from .room import Room
from .room_resource import *


def add_self_to_api(api):
    api.add_resource(RoomListResource, '/organization/<opp_id>/room')
    api.add_resource(RoomResource, '/organization/<opp_id>/room/<room_number>')
    api.add_resource(RoomScheduleResource, '/organization/<opp_id>/room/<room_number>/schedule')
