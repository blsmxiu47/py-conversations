# import time
from dagster import op
import requests
import requests_cache
import logging
import lxml
from bs4 import BeautifulSoup
# from selenium import webdriver

@op
def scrape_googlenews():
    # topics = ['Wildfires']
    topic = 'wildfires'
    date_range = '1d'
    # languages = ['en-US']
    # geos = ['US']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }
    params = {
        'q': f'{topic} when:{date_range}',
        'hl': 'en-US',
        'gl': 'US',
        'ceid': 'US%3Aen'
    }
    session = requests_cache.CachedSession('http_cache', backend='filesystem') # TODO: Change to backend='sqlite'
    try:
        # e.g. 'https://news.google.com/search?q=Wildfires%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen'
        response = session.get('https://news.google.com/search', headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error('Http Error:',errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error('Error Connecting:',errc)
    except requests.exceptions.Timeout as errt:
        logging.error('Timeout:',errt)
    except requests.exceptions.TooManyRedirects as errtmr:
        logging.error('Too Many Redirects:',errtmr)
    except requests.exceptions.RequestException as err:
        logging.error('Sorry.. Some request exception occurred',err)

    soup = BeautifulSoup(response.text, 'lxml')
    query_results = soup.select('main > c-wiz > div:nth-of-type(1) > div')
    results = []
    for result in query_results[:2]:
        article = result.select('article')[0]
        title = article.select('article h3 > a')[0].get_text()
        link = article.find('a', href=True)['href']
        subheading = article.select('div > div')[0]
        source = subheading.find('a').text
        time = subheading.find('time')['datetime']

        results.append({
            'article': article,
            'title': title,
            'link': link,
            'subheading': subheading,
            'source': source,
            'time': time
            })
        # print(f'{title}\n{link}\n{source}\n{time}\n')
        
    return results

