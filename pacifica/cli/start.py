#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the module."""
import cherrypy

from pacifica.session.globals import config, CP_CONFIG_FILE
from pacifica.session.orm import ORMState
from pacifica.session.rest import SessionDispatch

db = config['postgres']
ORMState.create(db['dbname'],'postgres',
                user=db['user'],
                password=db['password'],
                host=db['host'])

# simple sanity check
tables = ORMState.get_tables()

cherrypy.config.update(CP_CONFIG_FILE)
cherrypy.tree.mount(SessionDispatch(), '/sessions', CP_CONFIG_FILE)

# set localhost and port if needed
cherrypy.server.socket_host = '127.0.0.1'
cherrypy.server.socket_port = 8068

cherrypy.engine.start()
cherrypy.engine.wait(cherrypy.engine.states.STARTED)
cherrypy.engine.block()

