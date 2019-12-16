#!/usr/bin/python
# -*- coding: utf-8 -*-
"""model test module."""

import os
from pacifica.session.model import model_create, ModelState, model_clear, SessionModel


def test_model_create(tmpdir):
    """Test model creation"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    database, _, _ = model_create(tmp_db)

    tables = database.get_tables()
    assert set(tables) == {'files', 'sessions'}

    # test repeated creation
    database1, _, _ = model_create(tmp_db)
    assert database1 == database


def test_model_clear_empty():
    """test clearing non-existing model"""
    model_clear()


def test_model_clear_existing(tmpdir):
    """test clearing existing model"""
    tmp_db = os.path.join(tmpdir, 'session.db')
    model_create(tmp_db)

    SessionModel.create(status='open')

    model_clear()

    assert ModelState.handle is None
    assert ModelState.file is None
    assert ModelState.models is None
