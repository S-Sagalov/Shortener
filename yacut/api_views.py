from flask import jsonify, request

from . import app, db
from .models import URLMap
from .validators import validate_data


@app.route('/api/id/', methods=['POST'])
def create_short_url():
    data = request.get_json()
    validated_data = validate_data(data)
    url = URLMap()
    url.from_dict(validated_data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id//<string:short_link>/', methods=['GET'])
def get_original_link(short_link):
    url = URLMap.query.filter_by(short=short_link).first()
    if not url:
        return jsonify({'message': 'Указанный id не найден'}), 404
    return jsonify({'url': url.original})
