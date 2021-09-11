class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,desc,time_posted,url,urlToImage,title,content):
        self.author = author
        self.desc = desc
        self.time_posted = time_posted
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
        self.content = content