# sqlite for tests so the suite runs without postgres createdb rights.
# Run: manage.py test --settings=config.settings_test
from .settings import *  # noqa: F403

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
