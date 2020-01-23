# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import logging
import json
import os
import uuid
from peewee import SqliteDatabase

from playhouse.shortcuts import model_to_dict, PostgresqlDatabase

from pacifica.session.globals import DB_FILE_DEFAULT, GLOBAL_CONFIG
from pacifica.session.utils import json_encode
from pacifica.session.model import SessionModel, FileModel, SessionMetaModel, FileMetaModel

logger = logging.getLogger(__name__)

logger.info('test')
_MODELS = (SessionModel, FileModel, SessionMetaModel, FileMetaModel)


class ORMState:
    """Container for orm state."""
    _db_handle = None
    _db_name = None
    _db_models = None

    @classmethod
    def create(cls, db_name, db_type, host=None, user=None, password=None,
               port=5432, models=_MODELS):
        """ Setup ORM."""

        if db_type == 'sqlite':
            logger.info(F'Opening connection to sqlite')
            db = SqliteDatabase(db_name,
                                pragmas={
                                    'journal_mode': 'wal',
                                    'cache_size': -1 * 64000,  # 64MB
                                    'foreign_keys': 1,
                                    'ignore_check_constraints': 0,
                                }
                                )
        elif db_type == 'postgres':

            db = PostgresqlDatabase(name, user=user, password=password,
                                    host=host, port=port)
        else:
            logger.error(F'Unknown database type {db_type}')
            raise ValueError

        db.bind(models)
        db.create_tables(models, safe=True)

        cls._db_handle = db
        cls._db_name = db_name
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


def session_create(params):
    """ Create new session."""
    name = params.get('name', None)
    description = params.get('description', None)
    session = SessionModel.create(name=name,description=description)
    return model_to_json(session)


def session_list_all():
    """Get list of all sessions."""
    session_list = []
    for session in SessionModel.select():
        session_list.append(model_to_dict(session))

    return json.dumps(session_list, default=json_encode)


def session_list(uuid_string):
    """Get session corresponding to given uuid."""
    session = SessionModel.get_by_id(uuid.UUID(uuid_string))
    return model_to_json(session)


if __name__ == '__main__':

    logger = logging.getLogger()
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    simple_formatter = logging.Formatter('\n %(message)s')
    console.setFormatter(simple_formatter)
    logger.addHandler(console)

    print(DB_FILE_DEFAULT)
    ORMState.create(DB_FILE_DEFAULT,'sqlite')

    record = session_create({'name': 'name'})
    uuid_string = json.loads(record)['session_id']
    print(session_list(uuid_string))
