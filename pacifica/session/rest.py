# pylint: disable=invalid-name
# pylint: disable=inconsistent-return-statements
# !/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the module."""

import json
import cherrypy
from pacifica.session.orm import session_create, session_list_all, session_list


# pylint: disable=too-few-public-methods
from pacifica.session.utils import json_extract, dict_extract


class SessionDispatch():
    """ routing for session class. """
    exposed = True

    def __init__(self):
        self.files = FileDispatch()
        self.meta = MetaDispatch()

    def _cp_dispatch(self, vpath):
        if len(vpath) >= 1:
            session_id = vpath.pop(0)
            cherrypy.request.params['session_id'] = session_id
            return self

    @staticmethod
    @cherrypy.tools.json_in()
    def GET(session_id=None):
        """GET method"""
        if session_id:
            result = session_list(session_id)
        else:
            result = session_list_all()
        return result

    @staticmethod
    @cherrypy.tools.json_in()
    # @cherrypy.tools.json_out()
    def POST():
        """POST method"""
        input_dict = cherrypy.request.json
        input_dict = dict_extract(input_dict,['name'])
        record = session_create(input_dict)
        return record


class FileDispatch():
    """/files route"""
    exposed = True

    @staticmethod
    def GET(session_id=None):
        """GET method"""
        return F'Files session_id={session_id}'


class MetaDispatch():
    """ /meta route """
    exposed = True

    @staticmethod
    def GET(session_id=None):
        """GET method"""
        return F'Metadata session_id={session_id}'


if __name__ == '__main__':
    from pacifica.session.globals import CP_CONFIG_FILE
    from pacifica.session.orm import ORMState

    ORMState.create(clear=True)
    #
    config_file = CP_CONFIG_FILE
    cherrypy.config.update(config_file)
    cherrypy.tree.mount(SessionDispatch(), '/sessions', config_file)

    # set localhost and port if needed
    cherrypy.server.socket_host = '127.0.0.1'
    cherrypy.server.socket_port = 8068

    cherrypy.engine.start()
    cherrypy.engine.wait(cherrypy.engine.states.STARTED)
    cherrypy.engine.block()
