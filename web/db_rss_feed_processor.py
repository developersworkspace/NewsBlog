import sqlite3 as lite
from newsblog.rssFeeds import DailyMaverick, EWN, CNET, News24, BBC, TechCrunch, TheVerge, SkyNews, FoxNews, MarketWatch, Mashable, LifeHacker
from time import sleep

while(True):

    connection = lite.connect('../test.db')
    connection.row_factory = lite.Row
    cursor = connection.cursor()

    articles = []

    articles = articles + DailyMaverick().getArticles()
    articles = articles + EWN().getArticles()
    articles = articles + CNET().getArticles()
    articles = articles + News24().getArticles()
    articles = articles + BBC().getArticles()
    articles = articles + TechCrunch().getArticles()
    articles = articles + TheVerge().getArticles()
    articles = articles + SkyNews().getArticles()
    articles = articles + FoxNews().getArticles()
    articles = articles + MarketWatch().getArticles()
    articles = articles + Mashable().getArticles()
    articles = articles + LifeHacker().getArticles()

    for article in articles:
        cursor.execute('SELECT [link] FROM [articles] WHERE [link] = "{0}"'.format(article.link))
        r = cursor.fetchone()
        if (r is None):
            print(article.link)
            cursor.execute('INSERT INTO [articles] ([feedName], [link], [title], [summary], [timestamp]) VALUES ("{0}", "{1}", "{2}", "{3}", {4})'.format(article.feedName.replace('"',"'"), article.link.replace('"',"'"), article.title.replace('"',"'"), article.summary.replace('"',"'"), article.timestamp.timestamp()))

    cursor.execute('SELECT COUNT(*) AS [Count] FROM [articles]')
    data = cursor.fetchone()

    print('{0} articles in database'.format(data['Count']))

    connection.commit()

    sleep(180)
   
