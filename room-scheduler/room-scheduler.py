from flask import Flask, render_template
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
        # We only want /ping in DEV
        @app.route('/')
        def root():
            return render_template('login.html',cssFilename='login.css')
        @app.route('/dashboard')
        def dashboard():
            MeetingRoom = {'roomNumber':'Room 581'}
            Meeting = {'meetingName':'Trello Meeting', 'startTime':'12:30', 'endTime':'2:30'}
            return render_template('dashboard.html',cssFilename='dashboard.css',MeetingRoom=MeetingRoom,Meeting=Meeting)
        @app.route('/new-organization')
        def newOrg():
            return render_template('newOrg.html',cssFilename='newOrg.css')
        @app.route('/admin-page')
        def adminPage():
            return render_template('adminPage.html',cssFilename='adminPage.css')
        @app.route('/logout')
        def logout():
            return render_template('logout.html')


    HTTP_SERVER = WSGIServer(('', 5080), app)
    HTTP_SERVER.serve_forever()

if __name__=="__main__":
    main()