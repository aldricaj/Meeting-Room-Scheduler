from flask_restful import Resource

class OrganizationResource(Resource):
    def get(self, org_id):
        return "Not Implemented", 501

class OrganizationListResource(Resource):
    def get(self):
        return "Not Implemented", 501

    def post(self):
        return "Not Implemented", 501