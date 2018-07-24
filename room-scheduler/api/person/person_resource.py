from .person_repo import *
from . import Person
from .. import from_json

from flask_restful import Resource
from flask import request

class PersonResource(Resource):
    def get(self, org_id, username):
        return get_one(org_id, username), 200

    def put(self, org_id, username):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        person = Person(**from_json(request.json))
        person.org_id = org_id

        return update(person).to_json(), 200

class PersonListResource(Resource):
    def get(self, org_id):
        return get_many(org_id)

    def post(self, org_id):
        if not request.is_json:
            return 'The request is not a json. Check your mimetype to make sure it identifies as application/JSON', 400

        new_person = Person(**from_json(request.json))
        new_person.org_id = org_id

        return create(new_person).to_json(), 200

class PersonScheduleResource(Resource):
    def get(self, org_id, username):
        return get_schedule(org_id, username), 200