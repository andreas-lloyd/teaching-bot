import datetime

import peewee
import yaml

with open('creds-db.yaml') as yaml_file:
    credentials = yaml.load(yaml_file, Loader=yaml.FullLoader)

db = peewee.PostgresqlDatabase(credentials['db_url'])

class BaseModel(peewee.Model):
    class Meta:
        database = db
        legacy_table_names = False

class Users(BaseModel):
    created_at = peewee.DateTimeField()

class PlatformUsers(BaseModel):
    user_id = peewee.ForeignKeyField(User, backref='user')
    created_at = peewee.DateTimeField()
    platform_name = peewee.TextField()
    platform_id = peewee.CharField(unique=True)

class Content(BaseModel):
    created_at = peewee.DateTimeField()
    content_type = peewee.TextField()
    content_description = peewee.TextField()
    content_url = peewee.TextField()

class ContentRecommendation(BaseModel):
    created_at = peewee.DateTimeField()
    user_id = peewee.ForeignKeyField(User, backref='user')
    content_id = peewee.ForeignKeyField(Content, backref='content')

def create_tables():
    with db:
        db.create_tables([Users, PlatformUsers, Content, ContentRecommendation])