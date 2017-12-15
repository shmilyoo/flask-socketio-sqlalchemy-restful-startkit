from flask import Flask, g


def create_app(config_file, async_mode, name=__name__):
    app = Flask(name)
    app.config.from_object(config_file)

    from app.models import db
    db.init_app(app)

    from app.sio import socketIO, init_sockets
    init_sockets()
    socketIO.init_app(app, async_mode=async_mode)

    @app.before_first_request
    def before_first_req():
        print('first request')

    @app.before_request
    def before_req():
        print('before request')

    @app.route('/')
    def index():
        return ''

    @app.teardown_request
    def teardown_req(e):
        print('teardown')

    return app
