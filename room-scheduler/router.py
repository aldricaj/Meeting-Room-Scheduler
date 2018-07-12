
class Router():
    '''
        This serves as the main application router for flask, it'll 
        assign all routes needed for the application to work, connecting
        the controllers to the flask app

        Author: aldricaj
    '''

    def __init__(self, app):
        self.app = app
        self._load_ui_routes()
        self._load_api_routes()

    def _load_api_routes(self):
        ''' Loads the routes for the app '''
        pass

    def _load_ui_routes(self):
        ''' Loads routes for ui '''
        pass