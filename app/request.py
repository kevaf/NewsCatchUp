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

def get_sources():
    """
    function that gets the response from json to our url request 
    """
    get_sources_url = source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_result_list = get_sources_response['sources']
            source_results = process_results(source_result_list)
    
    return source_results


