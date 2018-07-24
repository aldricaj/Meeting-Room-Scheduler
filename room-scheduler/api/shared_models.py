from . import to_json

from dataclasses import dataclass
import datetime

@dataclass
class Event:
    meeting_id:int
    start: datetime.datetime
    end: datetime.datetime
    title: str
    room_number: str
    owner_username: str