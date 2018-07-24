from .. import to_json
from dataclasses import dataclass
import datetime

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
