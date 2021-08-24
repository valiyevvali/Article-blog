from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.valiyevvali.com','127.0.0.1']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'prod.sqlite3',
    }
}

sentry_sdk.init(
    dsn=env('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True
)

AWS_ACCESS_KEY_ID=env('ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME='vblogv'
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS={
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION='static'
STATIC_URL= 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)
STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'


DEFAULT_FILE_STORAGE='config.storage_backend.MediaStorage'