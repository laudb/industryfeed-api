from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

ALLOWED_HOST = os.environ.get("ALLOWED_HOST")
if ALLOWED_HOST:
    ALLOWED_HOSTS.append(ALLOWED_HOST)

CORS_ALLOWED_ORIGINS = []

CORS_ALLOWED_ORIGIN = os.environ.get("CORS_ALLOWED_ORIGIN")
if CORS_ALLOWED_ORIGIN:
    CORS_ALLOWED_ORIGINS.append(CORS_ALLOWED_ORIGIN)

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DB_CONNECTION_STRING"),
        conn_max_age=int(os.getenv("DB_CONNECTION_MAX_AGE")),
        conn_health_checks=os.getenv("DB_CONNECTION_HEALTCH_CHECKS"),
    )
}
