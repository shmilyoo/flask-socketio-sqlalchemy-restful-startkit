from flask_socketio import SocketIO

socketIO = SocketIO()


def init_sockets():
    from app.sio.socket_events import init_socket_events
    init_socket_events()
