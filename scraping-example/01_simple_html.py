import json
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

from scraping.scrapingutils.util import create_folder_if_not_exists, short_url


def render_html(url, target_folder):
    full_name = target_folder + "/" + short_url(url) + '.html'
    html = ''
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('error parsing the url,', e.reason)
        exit(-1)
    except URLError as e:
        print("server cannot be found")
        exit(-1)
    else:
        print("it worked")

    bs_obj = BeautifulSoup(html.read(), 'lxml')

    with open(full_name, 'w', encoding='utf-8') as file:
        file.writelines(str(bs_obj))

    return bs_obj


def main():
    # read config
    with open("config.json") as handle:
        config = json.loads(handle.read())

    create_folder_if_not_exists(config['targetFolder'])

    print(datetime.now().strftime('%Y%m%d%H%M%S'))

    for url in config['urls']:
        render_html(url, config['targetFolder'])


if __name__ == '__main__':
    main()
