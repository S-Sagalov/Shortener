from .models import URLMap
from settings import POSSIBLE_SYMBOLS, LINK_LENGTH

from random import choices


def create_unique_short_link():
    while True:
        short_id = ''.join(choices(POSSIBLE_SYMBOLS, k=LINK_LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
