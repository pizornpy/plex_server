from torrentp import TorrentDownloader
import asyncio
import os
import re
import time
import logging

class FlexOp:
    # Function to rename files for Plex
    @staticmethod
    def rename_for_plex(file_path):
        # Extract information from the file name using regex
        match = re.search(r"(.*?)S(\d{2})E(\d{2})", file_path, re.IGNORECASE)
        if not match:
            logging.warning("File name does not match the expected format.")
            return

        show_name = match.group(1).replace(".", " ").strip()
        season_num = match.group(2)
        episode_num = match.group(3)

        # Create the new file name
        new_name = f"{show_name} - S{season_num}E{episode_num}{os.path.splitext(file_path)[1]}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)

        # Rename the file
        os.rename(file_path, new_path)
        logging.info(f"Renamed '{file_path}' to '{new_path}'")

    # Function to get the most recently modified file in a directory
    @staticmethod
    def get_last_downloaded_file(directory):
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            return None
        # Sort files by modification time
        files.sort(key=os.path.getmtime, reverse=True)
        return files[0]  # Return the most recent file

    # Function to download a torrent
    @staticmethod
    async def download(magnet, path):
        torrent_file = TorrentDownloader(magnet, path)
        await torrent_file.start_download()
        return torrent_file