from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLsForm(FlaskForm):
    original_link = URLField(
        'Исходная "длинная" ссылка',
        validators=[DataRequired(message='Обязательное поле')])
    custom_id = StringField('желаемая "короткая" ссылка',
                            validators=[Length(1, 16),
                                        Optional()])
    submit = SubmitField('Преобразовать')
