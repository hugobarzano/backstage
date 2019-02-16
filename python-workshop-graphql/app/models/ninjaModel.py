from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)


class Ninja(Document):
    meta = {'collection': 'ninja'}
    name = StringField()
    enrolled = DateTimeField(default=datetime.now)
