from newsblog.scrapers import XECom
import pymysql
from time import time, sleep
import datetime

while(True):
    exchangeRates = XECom().getExchangeRates()

    connection = pymysql.connect(host='hjlmedicalservicescc.dedicated.co.za', port=3306, user='sadfmcoz_barend', passwd='MidericK96', db='sadfmcoz_dwtest')     
    cursor = connection.cursor()

    for exchangeRate1 in exchangeRates:
        fromCurrency = exchangeRate1

        for exchangeRate2 in exchangeRates[exchangeRate1]:
            toCurrency = exchangeRate2
            rate = float(exchangeRates[exchangeRate1][exchangeRate2])
            
            cursor.execute('SELECT `rate` FROM `exchangeRates` WHERE `fromCurrencyCode` = "{0}" AND `toCurrencyCode` = "{1}" ORDER BY `timestamp` DESC'.format(fromCurrency, toCurrency))
            r = cursor.fetchone()

            if (r is None or round(r[0], 2) != round(rate,2)):
                cursor.execute('INSERT INTO `exchangeRates` (`fromCurrencyCode`, `toCurrencyCode`, `rate`, `timestamp`) VALUES ("{0}", "{1}", {2}, "{3}")'.format(fromCurrency, toCurrency, rate, datetime.datetime.now()))
                print('{0} - {1} => {2} ({3})'.format(fromCurrency, toCurrency, round(rate,2), round(r[0], 2)))

    cursor.execute('SELECT COUNT(*) AS `Count` FROM `exchangeRates`')
    data = cursor.fetchone()

    print('{0} exchange rates in database'.format(data[0]))

    connection.commit()

    sleep(60)