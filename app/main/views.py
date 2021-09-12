from flask import render_template, redirect, url_for
from . import main
from ..request import get_sources, get_article

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to News Catch Up the number one news website'
    source = get_sources()
    return render_template ('index.html', title=title, source = source)

@main.route('/sources/<id>')
def sources(id):
    '''
    View root page function that returns the sources page and its data
    '''
    articles= get_article(id)
    
    return render_template ('articles.html', articles=articles)

