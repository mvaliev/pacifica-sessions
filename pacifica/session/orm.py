# pylint: disable=protected-access
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import sys
import uuid
from collections import namedtuple
from datetime import datetime
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from peewee import UUIDField, SqliteDatabase, TextField, IntegerField
# warning database type dependency here
from playhouse.sqlite_ext import JSONField
from pacifica.session.globals import DB_FILE_DEFAULT

orm_record = namedtuple('orm_record', 'handle file models')

THIS = sys.modules[__name__]

# never import this directly
THIS._orm_record = None


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
        """peewee metaclasss"""
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
        """peewee metaclasss"""
        table_name = 'files'


def orm_create(db_name=DB_FILE_DEFAULT):
    """ Setup sqlite database."""

    # pylint: disable=protected-access
    if not THIS._orm_record:
        print('creating new db')
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

        THIS._orm_record = orm_record(sqlite, db_name, models)

    return THIS._orm_record


def orm_clear():
    """ Removes everything in the database, except the file itself """

    if THIS._orm_record:
        THIS._orm_record.handle.drop_tables(THIS._orm_record.models, safe=True)
        THIS._orm_record = None


if __name__ == '__main__':
    print(orm_create())
    orm_clear()
    print(orm_create())
    session = SessionModel.create(status='closed')
