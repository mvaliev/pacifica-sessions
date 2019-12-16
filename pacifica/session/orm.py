# pylint: disable=too-few-public-methods
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import uuid
from datetime import datetime
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from peewee import UUIDField, SqliteDatabase, TextField, IntegerField
# warning database type dependency here
from playhouse.sqlite_ext import JSONField
from pacifica.session.globals import DB_FILE_DEFAULT


class ORMState:
    """Container for orm state."""
    handle = None
    file = None
    models = None

    @staticmethod
    def clear():
        """clear ORMState"""
        ORMState.handle = None
        ORMState.file = None
        ORMState.models = None


class SessionModel(Model):
    """Data model for session."""

    session_id = UUIDField(primary_key=True, column_name='uuid', default=uuid.uuid4, index=True)
    status = CharField(index=True)
    name = TextField(null=True)
    created = DateTimeField(default=datetime.now, index=True)
    updated = DateTimeField(default=datetime.now, index=True)
    deleted = DateTimeField(null=True, index=True)
    description = TextField(null=True)
    system = TextField(null=True)
    metadata = JSONField(null=True)

    class Meta:
        """peewee meta class"""
        table_name = 'sessions'


class FileModel(Model):
    """Data model for file."""

    session_id = ForeignKeyField(SessionModel, column_name='uuid', backref='files')
    status = CharField(index=True)
    basename = CharField()
    dirname = CharField()
    ctime = DateTimeField()
    mtime = DateTimeField()
    mimetype = CharField()
    size = IntegerField()
    description = TextField(null=True)
    metadata = JSONField(null=True)

    class Meta:
        """peewee metaclass"""
        table_name = 'files'


def orm_create(db_name=DB_FILE_DEFAULT):
    """ Setup sqlite database."""

    if ORMState.handle is None:
        models = [SessionModel, FileModel]
        sqlite = SqliteDatabase(db_name,
                                pragmas={
                                    'journal_mode': 'wal',
                                    'cache_size': -1 * 64000,  # 64MB
                                    'foreign_keys': 1,
                                    'ignore_check_constraints': 0,
                                }
                                )

        sqlite.bind(models)
        sqlite.create_tables(models, safe=True)

        ORMState.handle = sqlite
        ORMState.file = db_name
        ORMState.models = models

    return ORMState.handle, ORMState.file, ORMState.models


def orm_clear():
    """ Removes everything in the database, except the file itself """

    if ORMState.handle:
        ORMState.handle.drop_tables(ORMState.models, safe=True)
        ORMState.clear()


if __name__ == '__main__':
    orm_clear()
    # print(orm_create())
    # orm_clear()
    # print(orm_create())
    # session = SessionModel.create(status='closed')
    # # print(ORMState.handle)
