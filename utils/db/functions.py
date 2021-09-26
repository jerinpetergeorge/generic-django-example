from django.db import connection


def get_db_vendor():
    return connection.vendor
