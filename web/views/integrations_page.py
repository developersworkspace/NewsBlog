from flask import Blueprint, url_for, redirect, request
from newsblog.mysql.repositories import IntegrationRepository

page = Blueprint('integrations_page', __name__, template_folder='templates', static_folder='static')

@page.route('/subscribe/<type>', methods = ['POST'])
def subscribe(type):

    url = request.form['url']

    IntegrationRepository('../test.db').createIntegration(type, url)
    
    return redirect(url_for('home_page.index'))
