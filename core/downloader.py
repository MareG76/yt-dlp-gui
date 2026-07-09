from pathlib import Path

import yt_dlp


class Downloader:

    def download(
        self,
        url: str,
        folder: str,
        quality: str,
        progress_callback=None,
    ):

        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)

        format_map = {
            "Best Video + Audio": "bestvideo+bestaudio/best",
            "Best Video": "bestvideo",
            "Best Audio": "bestaudio",
            "MP3": "bestaudio",
        }

        options = {
            "outtmpl": str(folder / "%(title)s.%(ext)s"),
            "format": format_map.get(quality, "best"),
        }

        if quality == "MP3":
            options["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ]

        if progress_callback:
            options["progress_hooks"] = [progress_callback]

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])