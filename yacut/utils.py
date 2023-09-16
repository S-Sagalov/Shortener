from random import choices

from settings import POSSIBLE_SYMBOLS, LINK_LENGTH
from .models import URLMap


def create_unique_short_link():
    while True:
        short_id = ''.join(choices(POSSIBLE_SYMBOLS, k=LINK_LENGTH))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
