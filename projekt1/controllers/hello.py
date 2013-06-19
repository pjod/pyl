from projekt1.lib.base import *
from pylons import Response, url


class HelloController(BaseController):

    def index(self):
        return Response('witam grzyba;>')

    def serverinfo(self):
        return render('/szablon.txt')