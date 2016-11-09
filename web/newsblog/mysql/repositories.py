from newsblog.models import Article
import datetime
import pymysql

class ArticleRepository(object):

    connection, cursor = None, None

    def __init__(self):
        self.connection = pymysql.connect(host='hjlmedicalservicescc.dedicated.co.za', port=3306, user='sadfmcoz_barend', passwd='MidericK96', db='sadfmcoz_dwtest')     
        self.cursor = self.connection.cursor()



    def findArticles(self):

        self.cursor.execute('SELECT `feedName`, `title`, `summary`, `timestamp`, `link` FROM `articles` ORDER BY `timestamp` DESC LIMIT 10')
        data = self.cursor.fetchall()

        result = []

        for article in data:
            result.append(Article(article[0], article[1], article[2], datetime.datetime.fromtimestamp(article[3]), article[4]))

        return result

    def findArticlesFiltered(self, feedName, page):

        if (feedName is not None):
            self.cursor.execute('SELECT `feedName`, `title`, `summary`, `timestamp`, `link` FROM `articles` WHERE `feedName` = "{0}" ORDER BY `timestamp` DESC LIMIT {1},10'.format(feedName, (page - 1) * 10))
        else:
            self.cursor.execute('SELECT `feedName`, `title`, `summary`, `timestamp`, `link` FROM `articles` ORDER BY `timestamp` DESC LIMIT {0},10'.format((page - 1) * 10))
        data = self.cursor.fetchall()

        result = []

        for article in data:
            result.append(Article(article[0], article[1], article[2], article[3], article[4]))

        return result

class IntegrationRepository(object):


    connection, cursor = None, None

    def __init__(self):
        self.connection = pymysql.connect(host='hjlmedicalservicescc.dedicated.co.za', port=3306, user='sadfmcoz_barend', passwd='MidericK96', db='sadfmcoz_dwtest')     
        self.cursor = self.connection.cursor()

    def createIntegration(self, type, url):

        self.cursor.execute('INSERT INTO `integrations` (`type`, `url`) VALUES ("{0}", "{1}")'.format(type, url))

        self.connection.commit()

class ExchangeRateRepository(object):


    connection, cursor = None, None

    def __init__(self):
        self.connection = pymysql.connect(host='hjlmedicalservicescc.dedicated.co.za', port=3306, user='sadfmcoz_barend', passwd='MidericK96', db='sadfmcoz_dwtest')     
        self.cursor = self.connection.cursor()

    def getData(self):

        self.cursor.execute("CALL `GetExchangeRateData`()")

        data = self.cursor.fetchall()
        
        labels = []
        dataSets = []

        for d in data:
            if (d[0] not in labels):
                labels.append(d[0])
            

        for x in [1, 2, 3]:
            dataSet = {
                'label': "ZAR-USD" if x == 1 else ("ZAR-EUR" if x == 2 else "ZAR-GBP"),
                'data': [],
                'radius': 1.5
            }
            for d in data:
                dataSet['data'].append(round(d[x], 2))

            dataSets.append(dataSet)
               
        
        return  {
            'labels': labels,
            'datasets': dataSets,
            
        }