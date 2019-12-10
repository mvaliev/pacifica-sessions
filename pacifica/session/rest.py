"""CherryPy module containing classes for rest interface."""
from json import dumps
import cherrypy
# from cherrypy import HTTPError
from pacifica.session.globals import CP_CONFIG_FILE

def error_page_default(**kwargs):
    """The default error page should always enforce json."""
    cherrypy.response.headers['Content-Type'] = 'application/json'
    return dumps({
        'status': kwargs['status'],
        'message': kwargs['message'],
        'traceback': kwargs['traceback'],
        'version': kwargs['version']
    })


# pylint: disable=too-few-public-methods
class Dispatch:
    """CherryPy EventMatch endpoint."""

    exposed = True

    @staticmethod
    # pylint: disable=invalid-name
    def GET():
        """Get the event ID and return it."""
        # return str(example_task.delay(method, *numbers))
        return F'GET received'

    @staticmethod
    # pylint: disable=invalid-name
    def POST(name):
        """Get the event ID and return it."""
        # return str(example_task.delay(method, *numbers))
        return name


# pylint: disable=too-few-public-methods
class Status:
    """CherryPy Receive Event object."""

    exposed = True

    @staticmethod
    # pylint: disable=invalid-name
    def GET(uuid):
        """Receive the event and dispatch it to backend."""
        return F'GET {uuid}'
        # try:
        #     return str(ExampleModel.get(uuid=uuid).value)
        # except DoesNotExist:
        #     raise HTTPError('404', 'Not Found')
# pylint: enable=too-few-public-methods


# pylint: disable=too-few-public-methods
class Root:
    """CherryPy Root Object."""

    exposed = True
    dispatch = Dispatch()
    status = Status()
# pylint: enable=too-few-public-methods

if __name__ == '__main__':
    from pacifica.session import _PROJ_DIR
    print(_PROJ_DIR)
    CONFIG_FILE = CP_CONFIG_FILE
    cherrypy.quickstart(Root(), '/', CONFIG_FILE)
