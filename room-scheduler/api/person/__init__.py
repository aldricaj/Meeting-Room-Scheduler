from .person_resource import *

from .. import to_json
from dataclasses import dataclass

def add_self_to_api(api):
    api.add_resource(PersonListResource, '/organization/<opp_id>/person')
    api.add_resource(PersonResource, '/organization/<opp_id>/person/<username>')
    api.add_resource(PersonScheduleResource, '/organization/<opp_id>/person/<username>/schedule')

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
