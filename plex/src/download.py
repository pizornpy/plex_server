from torrentp import TorrentDownloader
import asyncio
import os
import re
import time
from func import *
import logging
from scrape import TorrentFinder
from call_llm import *

scrape = TorrentFinder()




raw_results = scrape.search_torrents('batman', 207)
data = FlexOp.clean_return(raw_results)

# Mostrar solo los magnet links
if data:
    for title, magnet in data.items():
        print(f"{title}:\n{magnet}\n")
else:
    print("No se encontraron torrents con magnet.")

call_llm()



# # Directory where files are downloaded
# file_location = r"/mnt/c/Users/Juan/plex/media/tvshows"

# # Download the torrent file
# torrent_file = TorrentDownloader(
#     "magnet:?xt=urn:btih:58255314E9A12352EC0A0AB643A13C6CDD1819BC&dn=Arcane%20S02E01%201080p%20WEB%20H264-SuccessfulCrab&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.bittor.pw%3A1337%2Fannounce&tr=udp%3A%2F%2Fpublic.popcorn-tracker.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Fopen.demonii.com%3A1337%2Fannounce",
#     file_location
# )

# # Start the download
# asyncio.run(torrent_file.start_download())

# time.sleep(120)  

# # Get the last downloaded file
# last_downloaded_file = FlexOp.get_last_downloaded_file(file_location)
# if last_downloaded_file:
#     logging.info(f"Last downloaded file: {last_downloaded_file}")
#     FlexOp.rename_for_plex(last_downloaded_file)
# else:
#     logging.warning("No files found in the directory.")