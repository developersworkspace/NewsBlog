from newsblog.scrapers import XECom
import sqlite3 as lite
from time import time, sleep

while(True):
    exchangeRates = XECom().getExchangeRates()

    connection = lite.connect('test.db')
    connection.row_factory = lite.Row
    cursor = connection.cursor()

    for exchangeRate1 in exchangeRates:
        fromCurrency = exchangeRate1

        for exchangeRate2 in exchangeRates[exchangeRate1]:
            toCurrency = exchangeRate2
            rate = float(exchangeRates[exchangeRate1][exchangeRate2])
            
            cursor.execute('SELECT [rate] FROM [exchangeRates] WHERE [fromCurrencyCode] = "{0}" AND [toCurrencyCode] = "{1}" ORDER BY [timestamp] DESC'.format(fromCurrency, toCurrency))
            r = cursor.fetchone()

            if (r is None or round(r['rate'], 2) != round(rate,2)):
                cursor.execute('INSERT INTO [exchangeRates] ([fromCurrencyCode], [toCurrencyCode], [rate], [timestamp]) VALUES ("{0}", "{1}", {2}, {3})'.format(fromCurrency, toCurrency, rate, time()))
                print('{0} - {1} => {2} ({3})'.format(fromCurrency, toCurrency, round(rate,2), round(r['rate'], 2)))

    cursor.execute('SELECT COUNT(*) AS [Count] FROM [exchangeRates]')
    data = cursor.fetchone()

    print('{0} exchange rates in database'.format(data['Count']))

    connection.commit()

    sleep(60)