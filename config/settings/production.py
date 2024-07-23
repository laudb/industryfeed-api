from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["https://industryfeed.netlify.app/"]

CORS_ALLOWED_ORIGINS = ["https://industryfeed.netlify.app/"]
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DB_CONNECTION_STRING"),
        conn_max_age=int(os.getenv("DB_CONNECTION_MAX_AGE")),
        conn_health_checks=os.getenv("DB_CONNECTION_HEALTCH_CHECKS"),
    )
}
