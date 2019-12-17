# pylint: disable=too-few-public-methods
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""The model module defining data model for session api."""
import uuid
from datetime import datetime
from peewee import Model, CharField, DateTimeField, ForeignKeyField
from peewee import UUIDField, TextField, IntegerField
# warning database type dependency here
from playhouse.sqlite_ext import JSONField


class SessionModel(Model):
    """Data model for session."""

    session_id = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    status = CharField(index=True, default='open', null=False)
    name = TextField(null=True)
    created = DateTimeField(default=datetime.now, index=True)
    updated = DateTimeField(default=datetime.now, index=True)
    deleted = DateTimeField(null=True, index=True)
    description = TextField(null=True)
    system = TextField(null=True)

    class Meta:
        """peewee meta class"""
        table_name = 'sessions'


class FileModel(Model):
    """Data model for file."""

    file_id = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    session_id = ForeignKeyField(SessionModel, column_name='session_id', backref='files')
    status = CharField(index=True)
    basename = CharField()
    dirname = CharField()
    ctime = DateTimeField()
    mtime = DateTimeField()
    mimetype = CharField()
    size = IntegerField()
    description = TextField(null=True)

    class Meta:
        """peewee metaclass"""
        table_name = 'files'


class SessionMetaModel(Model):
    """Data model for session."""

    session_meta_id = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    session_id = ForeignKeyField(SessionModel, backref='files')
    created = DateTimeField(default=datetime.now, index=True)
    updated = DateTimeField(default=datetime.now, index=True)
    deleted = DateTimeField(null=True, index=True)
    json_blob = JSONField(null=True)

    class Meta:
        """peewee meta class"""
        table_name = 'session_meta'


class FileMetaModel(Model):
    """Data model for session."""

    file_meta_id = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    file_id = ForeignKeyField(FileModel, backref='files')
    created = DateTimeField(default=datetime.now, index=True)
    updated = DateTimeField(default=datetime.now, index=True)
    deleted = DateTimeField(null=True, index=True)
    json_blob = JSONField(null=True)

    class Meta:
        """peewee meta class"""
        table_name = 'file_meta'



