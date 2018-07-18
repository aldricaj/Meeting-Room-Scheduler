from .org_resource import *
def add_self_to_api(api):
    api.add_resource(OrganizationListResource, '/organization')
    api.add_resource(OrganizationResource, '/organization/<opp_id>')