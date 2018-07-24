from .meeting import Meeting
from .meeting_resource import *


def add_self_to_api(api):
    api.add_resource(MeetingListResource, '/organization/<opp_id>/meeting')
    api.add_resource(MeetingResource, '/organization/<opp_id>/meeting/<meeting_id>')
    api.add_resource(MeetingAttendeesResource, '/organization/<opp_id>/meeting/<meeting_id>/attendees')