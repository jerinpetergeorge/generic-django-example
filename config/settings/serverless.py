from .base import *

INSTALLED_APPS += ["django_s3_sqlite"]

zappa_sqlite_conf = {
    "ENGINE": "django_s3_sqlite",
    "BUCKET": env("SQLITE_S3_BUCKET", default="generic-django-s3-bucket"),
    "AWS_S3_ACCESS_KEY": env("AWS_S3_ACCESS_KEY", default=None),
    "AWS_S3_ACCESS_SECRET": env("AWS_S3_ACCESS_SECRET", default=None),
}
db_conf = DATABASES["default"]
db_conf.update(zappa_sqlite_conf)
