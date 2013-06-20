#import logging
import projekt1.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
#from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
#from routes import url_for
from projekt1.lib.base import BaseController, render
from projekt1.model.form import RegisterForm


#from projekt1.lib.base import *

#log = logging.getLogger(__name__)


class EhlouController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/ehlou.mako')
        # or, return a string
        response.content_type = 'text/html'
        #return 'Hello from the index() action!'
        c.name = "blablabla"
        return render('pierwszy.mako')

    def register(self):
        return render('register.mako')

    @validate(schema=RegisterForm(), form="register")
    def create(self):
        c.login = request.POST['login']
        c.email = request.POST['email']
        c.password = request.POST['password']
        c.password_confirmation = request.POST['password_confirmation']
        return render('create.mako')





    def aj(environ, start_response):
        start_response('200 OK', [('Content-type', 'text/html')])
        return ['<html><body>dupa:></body></html>']

    def view(self, year, month, day):
        return "This is the page for %s/%s/%s" % (year, month, day)

    def dupa(self):
        return render('/ehlou.mako')

    def environ(self):
        result = '<html><body><h1>Environ</h1>'
        for key, value in request.environ.items():
            result += '%s: %r <br />' % (key, value)
        result += '</body></html>'
        return result