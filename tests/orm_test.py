#!/usr/bin/python
# -*- coding: utf-8 -*-
"""model test module."""

import os
from pacifica.session.orm import ORMState


def test_orm_create(tmpdir):
    """Test ORM creation"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    ORMState.create(tmp_db,'sqlite')

    tables = ORMState.get_tables()
    assert set(tables) == {'files', 'sessions', 'file_meta', 'session_meta'}


# def test_orm_create_twice(tmpdir):
#     """Test ORM repeated creation"""
#     tmp_db = os.path.join(tmpdir, 'session.db')
#
#     ORMState.create(db_name=tmp_db)
#     db1 = ORMState.get_database()
#
#     ORMState.create(db_name=tmp_db)
#     db2 = ORMState.get_database()
#
#     assert db1 == db2

#
# def test_model_clear_empty():
#     """test clearing non-existing model"""
#     model_clear()
#
#
# def test_model_clear_existing(tmpdir):
#     """test clearing existing model"""
#     tmp_db = os.path.join(tmpdir, 'session.db')
#     model_create(tmp_db)
#
#     SessionModel.create(status='open')
#
#     model_clear()
#
#     assert ModelState.handle is None
#     assert ModelState.file is None
#     assert ModelState.models is None
