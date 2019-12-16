# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import json
from playhouse.shortcuts import model_to_dict
from pacifica.session.utils import json_encode, valid_uuid
from pacifica.session.model import SessionModel, model_create

def model_to_json(session):
    """ convert model to json."""
    return json.dumps(model_to_dict(session), default=json_encode)


def session_create():
    """ Create new session."""
    session = SessionModel.create()
    return model_to_dict(session)


if __name__ == '__main__':
    handle, filename, _ = model_create()
    print(filename)
    record = session_create()
    print(record)
    uuid_string = str(record['session_id'])

    print('valid uuid=', valid_uuid(uuid_string))
