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
    articles= get_article(id)
    return render_template ('index.html', title=title, source = source, articles=articles)