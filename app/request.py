import urllib.request, json
from n_article_model import Article
from n_source_model import Source

#getting API_KEY
api_key = None
#getting news source url
source_url = None
#getting articles url
articles_url = None

def configure_request(app):
    global api_key, source_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_API_SOURCE_URL']
    articles_url = app.config['NEWS_API_ARTICLE_URL']