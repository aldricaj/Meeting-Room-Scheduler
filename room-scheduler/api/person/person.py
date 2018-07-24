
from .. import to_json
from dataclasses import dataclass

@dataclass 
class Person:
    org_id:int
    username:str
    first_name:str
    last_name:str
    email:str
    role_id: int
    role_name: str

    def get_json(self):
        return to_json(self.__dict__)