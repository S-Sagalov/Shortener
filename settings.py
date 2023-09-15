import os
from string import ascii_lowercase, ascii_uppercase

LINK_LENGTH = 6
POSSIBLE_SYMBOLS = ascii_lowercase + ascii_uppercase + '0123456789'


# было бы логичнее использовать set, но не пускают автотесты

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',
                                        default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY')

