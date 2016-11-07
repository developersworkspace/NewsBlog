import sqlite3 as lite
from newsblog.models import Article
import datetime

class ArticleRepository(object):

    connection, cursor = None, None

    def __init__(self, db):

        self.connection = lite.connect(db)
        self.connection.row_factory = lite.Row
        self.cursor = self.connection.cursor()

    def findArticles(self):

        self.cursor.execute('SELECT * FROM [articles] ORDER BY [timestamp] DESC LIMIT 10')
        data = self.cursor.fetchall()

        result = []

        for article in data:
            result.append(Article(article['feedName'], article['title'], article['summary'], datetime.datetime.fromtimestamp(article['timestamp']), article['link']))

        return result

    def findArticlesFiltered(self, feedName, page):

        if (feedName is not None):
            self.cursor.execute('SELECT * FROM [articles] WHERE [feedName] = "{0}" ORDER BY [timestamp] DESC LIMIT {1},10'.format(feedName, (page - 1) * 10))
        else:
            self.cursor.execute('SELECT * FROM [articles] ORDER BY [timestamp] DESC LIMIT {0},10'.format((page - 1) * 10))
        data = self.cursor.fetchall()

        result = []

        for article in data:
            result.append(Article(article['feedName'], article['title'], article['summary'], datetime.datetime.fromtimestamp(article['timestamp']), article['link']))

        return result

class IntegrationRepository(object):


    connection, cursor = None, None

    def __init__(self, db):

        self.connection = lite.connect(db)
        self.connection.row_factory = lite.Row
        self.cursor = self.connection.cursor()

    def createIntegration(self, type, url):

        self.cursor.execute('INSERT INTO [integrations] ([type], [url]) VALUES ("{0}", "{1}")'.format(type, url))

        self.connection.commit()

class ExchangeRateRepository(object):


    connection, cursor = None, None

    def __init__(self, db):

        self.connection = lite.connect(db)
        self.connection.row_factory = lite.Row
        self.cursor = self.connection.cursor()

    def getData(self):
        sql = "SELECT printf('%s - %s', [fromCurrencyCode], [toCurrencyCode]) AS [exchangeRate], strftime('%Y-%m-%d %H:00',datetime([timestamp], 'unixepoch')) AS [timestamp], round(AVG([rate]), 2) AS [rate] FROM [exchangeRates] WHERE [fromCurrencyCode] = 'ZAR' GROUP BY strftime('%Y-%m-%d %H:00',datetime([timestamp], 'unixepoch')), printf('%s - %s', [fromCurrencyCode], [toCurrencyCode]) ORDER BY [timestamp] ASC"

        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        
        labels = []
        dataSets = []

        for d in data:
            if (d['timestamp'] not in labels):
                labels.append(d['timestamp'])


        for d in data:
            exist = False
            for dataSet in dataSets:
                if (dataSet['label'] == d['exchangeRate']):
                    exist = True
                    dataSet['data'].append(d['rate'])

            if (exist is False):
                dataSets.append({
                    'label': d['exchangeRate'],
                    'data': [
                        d['rate']
                    ],
                    'fill': False,
                    #'pointRadius': 0
                })
        
        return  {
            'labels': labels,
            'datasets': dataSets,
            
        }