#!/usr/bin/python
# -*- coding: utf-8 -*-
"""orm test module."""

import os
from pacifica.session.orm import orm_create

def test_orm_create(tmpdir):
    """Test orm creation"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    database = orm_create(tmp_db)

    tables = database.handle.get_tables()
    assert set(tables) == {'files', 'sessions'}

    # test repeated creation
    database1 = orm_create(tmp_db)
    assert database1 == database


#
# def test_create_session_model():
#     database_proxy.initialize(SqliteDatabase('session.db'))
#     database_setup(reset=True)
#     assert SessionModel.create(status='new', description='record 1')
#     with pytest.raises(IntegrityError):
#         assert SessionModel.create()
