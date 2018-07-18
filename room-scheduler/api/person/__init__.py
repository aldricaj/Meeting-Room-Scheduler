from .person_resource import *

def add_self_to_api(api):
    api.add_resource(PersonListResource, '/organization/<opp_id>/person')
    api.add_resource(PersonResource, '/organization/<opp_id>/person/<username>')
    api.add_resource(PersonScheduleResource, '/organization/<opp_id>/person/<username>/schedule')