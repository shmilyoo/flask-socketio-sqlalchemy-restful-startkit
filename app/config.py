SECRET_KEY = 'flask-socketio-key'
HOST = '0.0.0.0'
PORT = 5000
DEBUG = True

DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_DB = 'db_name'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB
