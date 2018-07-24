from .meeting_resource import *

from .. import to_json
from dataclasses import dataclass
import datetime

def add_self_to_api(api):
    api.add_resource(MeetingListResource, '/organization/<opp_id>/meeting')
    api.add_resource(MeetingResource, '/organization/<opp_id>/meeting/<meeting_id>')
    api.add_resource(MeetingAttendeesResource, '/organization/<opp_id>/meeting/<meeting_id>/attendees')

@dataclass
class Meeting:
    meeting_id: int
    org_id: int
    owner_username: str
    meeting_start: datetime.datetime
    meeting_end: datetime.datetime
    meeting_title: str
    room_number: str

    def get_json(self):
        return to_json(self.__dict__)

@dataclass
class MeetingAttendee:
    username:str
    first_name:str
    last_name:str
    email:str

    def get_json(self):
        return to_json(self.__dict__)
