from .room_resource import *
from .. import to_json

from dataclasses import dataclass

def add_self_to_api(api):
    api.add_resource(RoomListResource, '/organization/<opp_id>/room')
    api.add_resource(RoomResource, '/organization/<opp_id>/room/<room_number>')
    api.add_resource(RoomScheduleResource, '/organization/<opp_id>/room/<room_number>/schedule')

@dataclass
class Room:
    org_id: int
    room_number: str
    av_type_id: int
    av_type_txt: str

    def get_json(self):
        return to_json(self.__dict__)
