#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the module."""

from decimal import Decimal
import datetime
import uuid
import json


def json_extract(json_in, keys):
    json_dict = json.loads(json_in)
    dict_out = dict((k, json_dict[k]) for k in keys if k in json_dict)

    return dict_out


def dict_extract(dict_in, keys):
    dict_out = dict((k, dict_in[k]) for k in keys if k in dict_in)

    return dict_out


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


if __name__ == '__main__':
    # json_in = json.dumps({'name':'marat', 'year':'69', 'month': 'July'})
    json_in = '{"name": "marat", "year": "69", "month": "July"}'
    print(json_in)
    print(json_extract(json_in, ['name']))
