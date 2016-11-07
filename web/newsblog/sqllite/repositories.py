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

        groupByFormat = '%Y-%m-%d %H:00'

        sql = "SELECT strftime('{0}',datetime(`timestamp`, 'unixepoch')) AS [timestamp], (SELECT `rate` AS `rate` FROM `exchangeRates` WHERE `timestamp` <= `exchangeRate`.`timestamp` AND `fromCurrencyCode` = 'ZAR' AND `toCurrencyCode` = 'USD' ORDER BY `timestamp` DESC LIMIT 1) AS `ZAR-USD`, (SELECT `rate` AS `rate` FROM `exchangeRates` WHERE `timestamp` <= `exchangeRate`.`timestamp` AND `fromCurrencyCode` = 'ZAR' AND `toCurrencyCode` = 'EUR' ORDER BY `timestamp` DESC LIMIT 1) AS `ZAR-EUR`, (SELECT `rate` AS `rate` FROM `exchangeRates` WHERE `timestamp` <= `exchangeRate`.`timestamp` AND `fromCurrencyCode` = 'ZAR' AND `toCurrencyCode` = 'GBP' ORDER BY `timestamp` DESC LIMIT 1) AS `ZAR-GBP` FROM `exchangeRates` AS `exchangeRate` GROUP BY strftime('{0}',datetime(`timestamp`, 'unixepoch')) ORDER BY `timestamp` ASC".format(groupByFormat)

        self.cursor.execute(sql)

        data = self.cursor.fetchall()
        
        labels = []
        dataSets = []

        for d in data:
            if (d['timestamp'] not in labels):
                labels.append(d['timestamp'])
            
        sets = ['ZAR-USD', 'ZAR-EUR', 'ZAR-GBP']

        for x in ['ZAR-USD', 'ZAR-EUR', 'ZAR-GBP']:
            dataSet = {
                'label': x,
                'data': [],
                'radius': 1.5
            }
            for d in data:
                dataSet['data'].append(d[x])

            dataSets.append(dataSet)
               
        
        return  {
            'labels': labels,
            'datasets': dataSets,
            
        }