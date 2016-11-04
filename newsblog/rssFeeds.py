from newsblog.baseRss import BaseRss

class DailyMaverick(BaseRss):

    def __init__(self):
        super().__init__('http://www.dailymaverick.co.za/rss')


class News24(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.news24.com/articles/news24/TopStories/rss')


class BBC(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.bbci.co.uk/news/rss.xml')


class EWN(BaseRss):

    def __init__(self):
        super().__init__('http://ewn.co.za/RSS%20Feeds/Latest%20News')


class TechCrunch(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.feedburner.com/TechCrunch', True)


class CNET(BaseRss):

    def __init__(self):
        super().__init__('https://www.cnet.com/rss/all')

class TheVerge(BaseRss):

    def __init__(self):
        super().__init__('http://www.theverge.com/rss/index.xml', True)

class SkyNews(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.skynews.com/feeds/rss/home.xml')

class FoxNews(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.foxnews.com/foxnews/latest?format=xml')

class MarketWatch(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.marketwatch.com/marketwatch/topstories?format=xml')

class Mashable(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.mashable.com/Mashable?format=xml')

class LifeHacker(BaseRss):

    def __init__(self):
        super().__init__('http://feeds.gawker.com/lifehacker/full?format=xml')









   






