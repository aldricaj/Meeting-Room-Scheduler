from flask import Flask
from gevent.pywsgi import WSGIServer

def main():
    ''' Starts the app reading in config (when I make it) '''  
    
    # TODO load configs here
    enviorment = 'DEV'

    app = Flask(__name__)
    
    if enviorment == 'DEV':
        # We only want /ping in DEV
        @app.route('/ping')
        def ping():
            '''Heartbeat function'''
            return 'pong'
        ping() #this is really to make pylint happy

    HTTP_SERVER = WSGIServer(('', 5080), app)
    HTTP_SERVER.serve_forever()

if __name__=="__main__":
    main()