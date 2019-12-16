#!/usr/bin/python
# -*- coding: utf-8 -*-
"""orm test module."""

import os
from pacifica.session.orm import orm_create, ORMState, orm_clear, SessionModel


def test_orm_create(tmpdir):
    """Test orm creation"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    database, _, _ = orm_create(tmp_db)

    tables = database.get_tables()
    assert set(tables) == {'files', 'sessions'}

    # test repeated creation
    database1, _, _ = orm_create(tmp_db)
    assert database1 == database


def test_orm_clear_empty():
    """test clearing non-existing ORM"""
    orm_clear()


def test_orm_clear_existing(tmpdir):
    """test clearing existing ORM"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    orm_create(tmp_db)

    SessionModel.create(status='open')

    orm_clear()

    assert ORMState.handle is None
    assert ORMState.file is None
    assert ORMState.models is None
