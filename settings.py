import os
from string import ascii_lowercase, ascii_uppercase

LINK_LENGTH = 6
MAX_LINK_LENGTH = 16
POSSIBLE_SYMBOLS = ascii_lowercase + ascii_uppercase + '0123456789'
SHORT_LINK_REGEXP_PATTERN = r'^([a-zA-Z0-9]{1,16})$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')
