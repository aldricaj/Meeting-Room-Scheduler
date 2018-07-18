import api.organization
import api.person
import api.room
import api.meeting
from flask_restful import Api


class Router():
    '''
        This serves as the main application router for flask, it'll 
        assign all routes needed for the application to work, connecting
        the controllers to the flask app

        Author: aldricaj
    '''

    def __init__(self, app):
        self.app = app
        self.api = Api(self.app)
        self._load_ui_routes()
        self._load_api_routes()

    def _load_api_routes(self):
        ''' Loads the routes for the app '''
        api.organization.add_self_to_api(self.api)
        api.person.add_self_to_api(self.api)
        api.room.add_self_to_api(self.api)
        api.meeting.add_self_to_api(self.api)
        
        
    def _load_ui_routes(self):
        ''' Loads routes for ui '''
        pass