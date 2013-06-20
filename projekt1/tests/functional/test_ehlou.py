from projekt1.tests import *

class TestEhlouController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='ehlou', action='index'))
        # Test response...
