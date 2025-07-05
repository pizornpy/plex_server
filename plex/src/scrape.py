from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests


load_dotenv()


class Scrape_utils(): 

    def make_url(movie): 
        return f"{torrent_site}/srch?search={movie}/"

    def get_magnet_links(search_query):
        base_url = f"https://1337x.to/search/{search_query}/1/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(base_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.select('a[href^="/torrent/"]')
        torrent_page = "https://1337x.to" + links[0]['href']

        page = requests.get(torrent_page, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        magnet_link = soup.select_one('a[href^="magnet:"]')['href']

        return magnet_link
