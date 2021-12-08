import logging

import requests

from . import session


def handle_request(url, headers=None, params=None):
    try:
        response = session.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logging.error("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        logging.error("Timeout:", errt)
    except requests.exceptions.TooManyRedirects as errtmr:
        logging.error("Too Many Redirects:", errtmr)
    except requests.exceptions.RequestException as err:
        logging.error("Sorry.. Some request exception occurred", err)

    return response
