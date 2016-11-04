class Article(object):

    feedName, title, summary, timestamp, link = None, None, None, None, None

    def __init__(self, feedName, title, summary, timestamp, link):
        self.feedName = feedName
        self.title = title
        self.summary = summary
        self.timestamp = timestamp
        self.link = link 