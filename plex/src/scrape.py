import requests
import re
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class TorrentFinder:
    def __init__(self):
        self.base_domain = 'thepiratebay0.org'

    def fetch_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    def search_torrents(self, query, category_code):
        try:
            url = f'https://{self.base_domain}/search/{query}/1/99/{category_code}'
            logging.info(f'Searching torrents with query: {query}, category: {category_code}')
            html = self.fetch_html(url)
            logging.debug(f'HTML content: {html[:500]}')
            soup = BeautifulSoup(html, 'html.parser')

            results = []
            for trs in soup.find_all('tr'):
                tds = trs.find_all('td')
                if len(tds) > 1:
                    logging.debug(f'Table row content: {tds}')
                    
                    magnet_tag = tds[1].find('a', href=True, title="Download this torrent using magnet")
                    magnet = magnet_tag['href'] if magnet_tag else None

                    title_tag = tds[1].find('a', class_='detLink')
                    title = title_tag.get('title', '').replace('Details for ', '') if title_tag else None

                    size_match = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1]))
                    size = size_match.group(0) if size_match else None

                    seeders = tds[2].text if len(tds) > 2 else None
                    leechers = tds[3].text if len(tds) > 3 else None

                    result = {
                        'title': title,
                        'magnet': magnet,
                        'size': size,
                        'seeders': seeders,
                        'leechers': leechers
                    }
                    result = {k: v.replace('\xa0', ' ') if v else v for k, v in result.items()}
                    results.append(result)
            return results

        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching torrents: {e}', exc_info=True)
            return []