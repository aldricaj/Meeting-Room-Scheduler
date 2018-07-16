
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
        # not a big fan of the look of this, but I don't think there is a way to avoid
        
        @self.app.route('/api/organization', methods=['POST'])
        def handle_root_org():
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>', methods=['GET'])
        def handle_org_w_id(org_id):
            return 'not implemented', 501
        
        @self.app.route('/api/organization/<org_id>/user', methods=['GET', 'POST'])
        def handle_root_user(org_id):
            return 'not implemented', 501
        
        @self.app.route('/api/organization/<org_id>/user/<username>', methods=['GET', 'PUT'])
        def handle_user_w_id(org_id, username):
            return 'not implemented', 501
        
        @self.app.route('/api/organization/<org_id>/user/<username>/schedule', methods=['GET'])
        def handle_user_schedule(org_id, username):
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>/room', methods=['GET', 'POST'])
        def handle_room_root(org_id):
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>/room/<room_number>', methods=['GET', 'PUT'])
        def handle_room_w_id(org_id, room_number):
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>/room/<room_number>/schedule', methods=['GET'])
        def handle_room_scehdule(org_id, room_number):
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>/meeting', methods=['GET', 'POST'])
        def handle_meeting(org_id):
            return 'not implemented', 501
        
        @self.app.route('/api/organization/<org_id>/meeting/<meeting_id>', methods=['GET', 'PUT'])
        def handle_meeting_w_id(org_id, meeting_id):
            return 'not implemented', 501

        @self.app.route('/api/organization/<org_id>/meeting/<meeting_id>/attendees', methods=['GET', 'POST'])
        def handle_meeting_attendees(org_id, meeting_id):
            return 'not implemented', 501

    def _load_ui_routes(self):
        ''' Loads routes for ui '''
        pass