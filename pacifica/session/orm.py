#!/usr/bin/python
# -*- coding: utf-8 -*-
"""The ORM module defining the SQL model for example."""
import uuid
from datetime import datetime
from peewee import Model, CharField, DateTimeField, UUIDField, SqliteDatabase
from playhouse.db_url import connect


db = SqliteDatabase('session.db')

def database_setup(reset=False):
    """Setup the database."""
    SessionModel.database_setup(reset=reset)


class SessionModel(Model):
    """Example saving some name data."""

    uuid = UUIDField(primary_key=True, default=uuid.uuid4, index=True)
    status = CharField()
    created = DateTimeField(default=datetime.now, index=True)
    updated = DateTimeField(default=datetime.now, index=True)
    deleted = DateTimeField(null=True, index=True)

    # pylint: disable=too-few-public-methods
    class Meta:
        """The meta class that contains db connection."""

        database = db
    # pylint: enable=too-few-public-methods

    @classmethod
    def database_setup(cls,reset=False):
        """Setup the database by creating all tables."""

        if cls.table_exists() and reset:
            cls.drop_table()

        if not cls.table_exists():
            cls.create_table()



    @classmethod
    def database_reset(cls):
        """Setup the database by creating all tables."""
        if cls.table_exists():
            cls.drop_table()

    @classmethod
    def connect(cls):
        """Connect to the database."""
        cls._meta.database.connect(True)

    @classmethod
    def close(cls):
        """Close the connection to the database."""
        cls._meta.database.close()

    @classmethod
    def atomic(cls):
        """Do the database atomic action."""
        return cls._meta.database.atomic()

if __name__ == '__main__':
    database_setup(reset=True)
    session = SessionModel.create(status='closed')
    session.save()
