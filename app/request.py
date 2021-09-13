import urllib.request, json
from .n_article_model import Article
from .n_source_model import Source

#getting API_KEY
api_key = None
#getting news source url
source_url = None
#getting articles url
articles_url = None

def configure_request(app):
    global api_key, source_url, articles_url
    api_key= app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    articles_url= app.config['NEWS_API_ARTICLE_URL']

def get_sources():
    """
    function that gets the response from json to our url request 
    """
    get_sources_url= source_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data= url.read()
        get_sources_response= json.loads(get_sources_data)

        source_results= None

        if get_sources_response['sources']:
            source_result_list= get_sources_response['sources']
            source_results= process_results(source_result_list)
    
    return source_results

def process_results(source_list):
    """
    function that processes news results and transforms them to a list
    """

    source_results= []

    for source_res in source_list:
        id = source_res.get('id')
        name = source_res.get('name')
        description = source_res.get('description')
        url = source_res.get('url')
        country = source_res.get('country')
        category = source_res.get('category')
        language = source_res.get('language')

        if name:
            source_objects = Source(id, name, description, url, category, language, country)
            source_results.append(source_objects)
    
    return source_results

def get_article(id):
    get_article_url= 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=ebfc7f378b3644929cb1c49457b7d575'.format(id)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_url_data=url.read()
        get_article_url_response=json.loads(get_article_url_data)

        article_source_results= None

        if get_article_url_response['articles']:
            article_source_lists=get_article_url_response['articles']
            article_source_results = process_articles_results(article_source_lists)

    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results=[]
    for item in news:
        author= item.get('author')
        desc= item.get('description')
        time_posted= item.get('publishedAt')
        urlToImage= item.get('urlToImage')
        url= item.get('url')
        title= item.get('title')
        content=item.get('content')

        if url:
            item_objects = Article(author,desc,time_posted,url,urlToImage,title,content)
            article_source_results.append(item_objects)
    
    return article_source_results
