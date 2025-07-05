from torrentp import TorrentDownloader
import asyncio
import os
import re
import time
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class FlexOp:

    
    @staticmethod
    def rename_for_plex(file_path):
        
        match = re.search(r"(.*?)S(\d{2})E(\d{2})", file_path, re.IGNORECASE)
        if not match:
            logging.warning("File name does not match the expected format.")
            return

        show_name = match.group(1).replace(".", " ").strip()
        season_num = match.group(2)
        episode_num = match.group(3)

        
        new_name = f"{show_name} - S{season_num}E{episode_num}{os.path.splitext(file_path)[1]}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)

        
        os.rename(file_path, new_path)
        logging.info(f"Renamed '{file_path}' to '{new_path}'")

    
    @staticmethod
    def get_last_downloaded_file(directory):
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            return None
        
        files.sort(key=os.path.getmtime, reverse=True)
        return files[0]  

    
    @staticmethod
    async def download(magnet, path):
        torrent_file = TorrentDownloader(magnet, path)
        await torrent_file.start_download()
        return torrent_file
    
    def clean_return(lista):
        tmp = 0
        if not lista: 
            logging.ERROR("NOT LIST")
            
            return 

      
            
        magnets_dict = {
    t['title']: t['magnet'] for t in lista if t['title'] and t['magnet']
    }
        return magnets_dict
