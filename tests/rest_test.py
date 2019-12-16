#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the test module."""

import uuid
import cherrypy
import pytest
import requests

from pacifica.session.rest import SessionDispatch
from pacifica.session.globals import CP_CONFIG_FILE


@pytest.fixture(scope="module")
def run_server():
    """server setup."""
    config_file = CP_CONFIG_FILE
    cherrypy.config.update(config_file)
    cherrypy.tree.mount(SessionDispatch(), '/sessions', config_file)

    # set localhost and port if needed
    cherrypy.server.socket_host = '127.0.0.1'
    cherrypy.server.socket_port = 8069

    cherrypy.engine.start()
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)

    port = cherrypy.server.socket_port
    host = cherrypy.server.socket_host
    url = F'http://{host}:{port}'
    try:
        yield url
    finally:
        cherrypy.engine.exit()
        cherrypy.engine.block()


# pylint: disable=redefined-outer-name
def test_sessions_get(run_server):
    """test post"""
    session_id = None
    endpoint = F'/sessions'
    url = run_server
    resp = requests.get(F'{url}{endpoint}')
    ref_text = F'Session session_id={session_id}'
    assert resp.text == ref_text


def test_sessions_id_get(run_server):
    """test post"""
    session_id = uuid.uuid4()

    endpoint = F'/sessions/{session_id}'
    url = run_server
    resp = requests.get(F'{url}{endpoint}')
    ref_text = F'Session session_id={session_id}'
    assert resp.text == ref_text


def test_file_get(run_server):
    """test post"""
    session_id = uuid.uuid4()
    endpoint = F'/sessions/{session_id}/files'
    url = run_server
    resp = requests.get(F'{url}{endpoint}')
    ref_text = F'Files session_id={session_id}'
    assert resp.text == ref_text


def test_meta_get(run_server):
    """test post"""
    session_id = uuid.uuid4()
    endpoint = F'/sessions/{session_id}/meta'
    url = run_server
    resp = requests.get(F'{url}{endpoint}')
    ref_text = F'Metadata session_id={session_id}'
    assert resp.text == ref_text
