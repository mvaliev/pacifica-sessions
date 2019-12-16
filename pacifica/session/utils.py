#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the module."""

from decimal import Decimal
import datetime
import uuid


def json_encode(obj):
    """Custom json encode."""
    datetime_format = "%Y/%m/%d %H:%M:%S"
    date_format = "%Y/%m/%d"
    time_format = "%H:%M:%S"
    if isinstance(obj, Decimal):
        return str(obj)

    if isinstance(obj, datetime.datetime):
        return obj.strftime(datetime_format)

    if isinstance(obj, datetime.date):
        return obj.strftime(date_format)

    if isinstance(obj, datetime.time):
        return obj.strftime(time_format)

    if isinstance(obj, uuid.UUID):
        return str(obj)

    raise TypeError("%r is not JSON serializable" % obj)


def valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

    """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
    except ValueError:
        return False

    return str(uuid_obj) == uuid_to_test
