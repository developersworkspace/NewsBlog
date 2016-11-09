import feedparser
from dateutil import parser
from newsblog.models import Article
import datetime

class BaseRss(object):

    _url, _rss, _ignoreSummary = None, None, None

    def __init__(self, url, ignoreSummary = False):
        self._url = url
        self._ignoreSummary = ignoreSummary
        self._rss = self.getRssFeed()

    def getRssFeed(self):
        return feedparser.parse(self._url)

    def getArticles(self):

        articles = []

        for item in self._rss['items']:
            dt =  None
            try:
                dt = parser.parse(item['published']).replace(tzinfo=None)
            except:
                dt = datetime.datetime.now()
                
            articles.append(Article(self.getTitle(), item['title'], '' if self._ignoreSummary else item['summary'], dt, item['link']))

        articles.sort(key=lambda r: r.timestamp, reverse=True)
        return articles

    def getTitle(self):
        return self._rss['channel']['title']