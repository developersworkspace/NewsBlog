from flask import Blueprint, render_template, jsonify
from newsblog.mysql.repositories import ArticleRepository, ExchangeRateRepository

page = Blueprint('home_page', __name__, template_folder='templates', static_folder='static')

@page.route('/', defaults={'page': 1})
@page.route('/<int:page>')
def index(page):
    
    articles = ArticleRepository().findArticlesFiltered(None, page)

    return render_template('index.html', articles = articles, currentPage = page, nextPage = page + 1, previousPage = page - 1)

@page.route('/filtered/<feedName>', defaults={'page': 1})
@page.route('/filtered/<feedName>/<int:page>')
def filtered(feedName, page):

    articles = ArticleRepository().findArticlesFiltered(feedName, page)
    
    return render_template('filtered.html', articles = articles, currentPage = page, nextPage = page + 1, previousPage = page - 1, feedName = feedName)

@page.route('/exchangerate/getdata')   
def getExchangeRateData():
    result = ExchangeRateRepository().getData()

    return jsonify(result)