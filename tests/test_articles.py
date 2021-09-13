import unittest
from app.n_article_model import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Allan Smith',"Everybody thought it was Tottenhams game but its the underdogs, its Lanzini's game",'2020/9/12','https://www.lanzinicomeback.com','https://www.sampleimg','Westham', 'The hammers have it')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))