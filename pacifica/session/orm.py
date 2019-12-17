# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import json
import uuid
from peewee import SqliteDatabase
from playhouse.shortcuts import model_to_dict

from pacifica.session.globals import DB_FILE_DEFAULT
from pacifica.session.utils import json_encode
from pacifica.session.model import SessionModel, FileModel, SessionMetaModel, FileMetaModel

_MODELS = (SessionModel, FileModel, SessionMetaModel, FileMetaModel)


class ORMState:
    """Container for orm state."""
    _db_handle = None
    _db_file = None
    _db_models = None

    @classmethod
    def clear(cls):
        """clear ORMState"""
        cls._db_handle = None
        cls._db_file = None
        cls._db_models = None

    @classmethod
    def create(cls, db_name=DB_FILE_DEFAULT, clear=False, models=_MODELS):
        """ Setup ORM."""

        if clear:
            cls.clear()
        if cls._db_file != db_name:
            db = SqliteDatabase(db_name,
                                pragmas={
                                    'journal_mode': 'wal',
                                    'cache_size': -1 * 64000,  # 64MB
                                    'foreign_keys': 1,
                                    'ignore_check_constraints': 0,
                                }
                                )

            db.bind(models)
            db.create_tables(models, safe=True)

            cls._db_handle = db
            cls._db_file = db_name
            cls._db_models = models

    @classmethod
    def get_tables(cls):
        return ORMState._db_handle.get_tables()

    @classmethod
    def get_database(cls):
        return ORMState._db_handle


def model_to_json(session):
    """ convert model to json."""
    return json.dumps(model_to_dict(session), default=json_encode)


def session_create(name=None, description=None):
    """ Create new session."""
    session = SessionModel.create()
    return model_to_json(session)


def session_list_all():
    session_list = []
    for session in SessionModel.select():
        session_list.append(model_to_dict(session))

    return json.dumps(session_list, default=json_encode)


def session_list(uuid_string):
    session_list = []
    session = SessionModel.get_by_id(uuid.UUID(uuid_string))
    return model_to_json((session))


if __name__ == '__main__':
    ORMState.create()
    record = session_create()
    uuid_string = json.loads(record)['session_id']
    print(session_list(uuid_string))
