from app import create_app
from app.sio import socketIO

app = create_app('app.config', 'gevent')

if __name__ == '__main__':
    socketIO.run(
        app,
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'])
