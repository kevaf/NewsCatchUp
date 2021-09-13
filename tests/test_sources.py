import unittest
from app.n_source_model import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('id', 'name', 'description', 'url', 'sample category', 'French', 'sample country')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))