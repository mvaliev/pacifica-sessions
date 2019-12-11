#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the test module."""

import cherrypy
import pytest
import requests
from pacifica.session.rest import Root
from pacifica.session.globals import CP_CONFIG_FILE, CP_CONFIG_FILE_DEFAULT, get_proj_dir
from pacifica.session import _PROJ_DIR

@pytest.fixture(scope="module")
def run_server():
    """server setup."""
    config_file = CP_CONFIG_FILE
    print("CP_CONFIG_FILE_DEFAULT=",CP_CONFIG_FILE_DEFAULT)
    print("_PROJ_DIR=",_PROJ_DIR)
    print("_PROJ_DIR=",get_proj_dir())
    cherrypy.config.update(config_file)
    cherrypy.tree.mount(Root(), '/', config_file)

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
def test_post(run_server):
    """test post"""
    endpoint = '/dispatch/marat'
    url = run_server
    resp = requests.post(F'{url}{endpoint}')
    assert resp.text == 'marat'
