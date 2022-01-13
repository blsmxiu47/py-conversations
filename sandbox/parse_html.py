import requests_cache
from bs4 import BeautifulSoup
import pdb


def decompose(body, attr_list):
    for attr in attr_list:
        for tag in body.select(attr):
            tag.decompose()


def parse_html(html):
    tree = BeautifulSoup(html, 'lxml')

    body = tree.body
    if body is None:
        return None

    attrs_to_decompose = [
        'script',
        'style',
        'nav',
        'footer'
    ]
    decompose(body, attrs_to_decompose)

    text = body.get_text(separator='\n')
    pdb.set_trace()

    return text

if __name__=='__main__':
    session = requests_cache.CachedSession(
        'http_cache', backend='filesystem'
    )
    url = 'https://www.motherjones.com/environment/2022/01/wildfires-arctic-climate-change-melting-permafrost-thermokarst-sinkholes/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }
    response = session.get(url, headers=headers)

    parse_html(response.text)
