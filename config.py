import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL ='https://newsapi.org/v2/sources?apiKey=ebfc7f378b3644929cb1c49457b7d575'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_ARTICLE_URL = 'https://newsapi.org/v2/everything?q=articles&apiKey=ebfc7f378b3644929cb1c49457b7d575'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}