import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get("SECRET_KEY", "tV#Um9F!ErXB6ydv6YTeyVtyFjxA5r")
LOGLEVEL = os.environ.get('DJANGO_LOGLEVEL', 'info').upper()
# Config for database
SQL_ENGINE = os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3")
SQL_DATABASE = os.environ.get("SQL_DATABASE",
                              os.path.join(BASE_DIR, "db.sqlite3"))
SQL_USER = os.environ.get("SQL_USER", "user")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD", "password")
SQL_HOST = os.environ.get("SQL_HOST", "localhost")
SQL_PORT = os.environ.get("SQL_PORT", "5432")
# Config for sentry
DSN_SENTRY = os.environ.get("DSN_SENTRY", "")
# Config for AWS
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION', "")
# Config for celery
REDIS_URI = os.environ.get("REDIS_URI", "")
