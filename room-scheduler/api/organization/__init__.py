from .org_resource import *
from .. import to_json

from dataclasses import dataclass

def add_self_to_api(api):
    api.add_resource(OrganizationListResource, '/organization')
    api.add_resource(OrganizationResource, '/organization/<opp_id>')

@dataclass
class Organization:
    org_id: int 
    org_name: str

    def get_json(self):
        return to_json(self.__dict__)