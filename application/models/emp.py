from application import db
from mongoengine import Document, StringField, IntField,DateTimeField
from datetime import datetime


class Employee(Document):
    name = StringField(required=True, max_length=50)
    emp_id=IntField(unique=True)
    email=StringField(max_length=50,unique=True)
    age = IntField(required=True)
    created_at = DateTimeField(default=datetime.utcnow())
    
    