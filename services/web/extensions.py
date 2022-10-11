from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from celery import Celery

# singletons for import in app factory
db = SQLAlchemy()
migrate = Migrate()
celery = Celery()
cache = Cache(config={"CACHE_TYPE": "SimpleCache"})
