from bs4 import BeautifulSoup
import requests

class XECom(object):

    def getPageSource(self):

        response = requests.get('http://www.xe.com/')
        return response.content

    def getExchangeRates(self):

        soup = BeautifulSoup(self.getPageSource(), "html.parser")

        cells = soup.find_all('td', { 'class': 'rateCell'})

        results = {}

        for cell in cells:

            value = cell.find('a').decode_contents(formatter="html") if cell.find('a') else None
            if (value is None):
                continue

            data = cell.find('a')['rel'][0]
            fromCurrency = data.split(',')[0]
            toCurrency = data.split(',')[1]
            
            if (fromCurrency not in results):
                results[fromCurrency] = {}

            results[fromCurrency][toCurrency] = value

        return results


