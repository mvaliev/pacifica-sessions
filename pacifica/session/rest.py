#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This is the module."""


import cherrypy
from pacifica.session.orm import session_create

# pylint: disable=too-few-public-methods
class SessionDispatch():
    """ routing for session class. """
    exposed = True

    # pylint: disable=inconsistent-return-statements
    def __init__(self):
        self.files = FileDispatch()
        self.meta = MetaDispatch()

    def _cp_dispatch(self, vpath):
        if len(vpath) >= 1:
            session_id = vpath.pop(0)
            cherrypy.request.params['session_id'] = session_id
            return self

    # pylint: disable=invalid-name
    @staticmethod
    def GET(session_id=None):
        """GET method"""
        return F'Session session_id={session_id}'

    # pylint: disable=invalid-name
    @staticmethod
    def POST():
        """POST method"""
        record = session_create()
        return str(record['session_id'])

class FileDispatch():
    """/files route"""
    exposed = True

    # pylint: disable=invalid-name
    @staticmethod
    def GET(session_id=None):
        """GET method"""
        return F'Files session_id={session_id}'

class MetaDispatch():
    """ /meta route """
    exposed = True

    # pylint: disable=invalid-name
    @staticmethod
    def GET(session_id=None):
        """GET method"""
        return F'Metadata session_id={session_id}'

if __name__ == '__main__':
    from pacifica.session.globals import CP_CONFIG_FILE

    cherrypy.quickstart(SessionDispatch(), '/', CP_CONFIG_FILE)
