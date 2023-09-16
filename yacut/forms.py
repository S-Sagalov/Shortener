from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional, Regexp

from settings import SHORT_LINK_REGEXP_PATTERN


class URLsForm(FlaskForm):
    original_link = URLField(
        'Исходная "длинная" ссылка',
        validators=[DataRequired(message='Обязательное поле')])
    custom_id = StringField('желаемая "короткая" ссылка',
                            validators=[Optional(),
                                        Regexp(SHORT_LINK_REGEXP_PATTERN)])
    submit = SubmitField('Преобразовать')
