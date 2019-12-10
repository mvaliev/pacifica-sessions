#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the test module."""

import cherrypy
import pytest
import requests
from pacifica.session.rest import Root


@pytest.fixture(scope="module")
def run_server():
    config_file = "/Users/marat/codes/pacifica/pacifica-session/server.conf"
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


def test_post(run_server):
    endpoint = '/dispatch/marat'
    url = run_server
    s = requests.post(F'{url}{endpoint}')
    assert s.text == 'marat'

