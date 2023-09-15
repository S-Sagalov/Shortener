from flask import url_for

from datetime import datetime

from . import db

REQUIRED_FIELDS = ('original', 'short')
class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(url=self.original,
                    short_link=url_for('short_link_view',
                                       short_link=self.short,
                                       _external=True))

    # Вероятно, стоит выделить в отдельный модуль, так как присутствует
    # некоторая логика
    def from_dict(self, data):
        for field in REQUIRED_FIELDS:
            setattr(self, field, data.get(field))
