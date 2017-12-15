from app.sio import socketIO
from threading import Lock
import time

thread = None
thread_lock = Lock()
client_number = 0


def init_socket_events():
    print('init socket events')

    @socketIO.on('connect')
    def connect():
        global client_number
        client_number += 1
        print('connected: ' + str(client_number))
        global thread
        with thread_lock:
            if thread is None:
                thread = socketIO.start_background_task(
                    target=background_thread)
                print('back task started')

    @socketIO.on('disconnect')
    def disconnect():
        global client_number
        client_number -= 1
        print('disconnected: ' + str(client_number))


def background_thread():
    print('start backend send')
    while True:
        print('back number' + str(client_number))
        if client_number:
            socketIO.emit('backendSend', 'back', broadcast=True)
        time.sleep(2)
