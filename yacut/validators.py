import re

from settings import SHORT_LINK_REGEXP_PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import create_unique_short_link


def custom_id_validator(short_link):
    if not short_link:
        return
    if URLMap.query.filter_by(short=short_link).first():
        return f'Имя "{short_link}" уже занято.'
    regex = re.compile(SHORT_LINK_REGEXP_PATTERN)
    match = regex.match(short_link)
    if not match:
        return 'Указано недопустимое имя для короткой ссылки'


def original_link_validator(original_link):
    if not original_link:
        return '\"url\" является обязательным полем!'


def validate_data(data):
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    short = data.get('custom_id')
    original = data.get('url')
    if short:
        error = custom_id_validator(short)
        if error:
            raise InvalidAPIUsage(error)
    else:
        short = create_unique_short_link()
    error = original_link_validator(original)
    if error:
        raise InvalidAPIUsage(error)

    return {'original': original, 'short': short}
