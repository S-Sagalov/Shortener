from flask import flash, redirect, render_template, url_for, abort

from . import app, db
from .forms import URLsForm
from .models import URLMap
from .utils import create_unique_short_link


@app.route('/', methods=['GET', 'POST'])
def add_short_link_view():
    form = URLsForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if custom_id:
        if URLMap.query.filter_by(short=custom_id).first():
            flash(f'Имя {custom_id} уже занято!')
            # по-сути дублирование кода с валидацией, однако для api нужны
            # кавычки вокруг custom_id, а тут нет
            return render_template('index.html', form=form)
    else:
        custom_id = create_unique_short_link()
    url = URLMap(original=form.original_link.data,
                 short=custom_id)
    db.session.add(url)
    db.session.commit()
    flash(
        f'{url_for("short_link_view", short_link=custom_id, _external=True)}',
        'short_url')
    return render_template('index.html', form=form)


@app.route('/<string:short_link>')
def short_link_view(short_link):
    url = URLMap.query.filter_by(short=short_link).first()
    if not url:
        abort(404)
    return redirect(url.original)
