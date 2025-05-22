from dotenv import load_dotenv
import beautifulsoup4
import requests


load_dotenv()


class Scrape_utils(): 

    def make_url(movie): 
        return f"{torrent_site}/srch?search={movie}"

    def get_page(url): 
        response 