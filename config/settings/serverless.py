from .base import *

INSTALLED_APPS += ["django_s3_sqlite"]

zappa_sqlite_conf = {
    "ENGINE": "django_s3_sqlite",
    "BUCKET": env("SQLITE_S3_BUCKET", default="generic-django-s3-bucket"),
    "AWS_S3_ACCESS_KEY": env("AWS_S3_ACCESS_KEY"),
    "AWS_S3_ACCESS_SECRET": env("AWS_S3_ACCESS_SECRET"),
}
db_conf = DATABASES["default"]
db_conf.update(zappa_sqlite_conf)
