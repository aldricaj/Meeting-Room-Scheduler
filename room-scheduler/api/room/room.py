from .. import to_json
from dataclasses import dataclass

@dataclass
class Room:
    org_id: int
    room_number: str
    av_type_id: int
    av_type_txt: str

    def get_json(self):
        return to_json(self.__dict__)