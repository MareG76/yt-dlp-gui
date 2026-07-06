from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from models.video_info import VideoInfo


class Analyzer:
    def analyze(self, url: str) -> VideoInfo:

        options = {
            "quiet": True,
            "skip_download": True,
            "no_warnings": True,
        }

        try:
            with YoutubeDL(options) as ydl:
                info = ydl.extract_info(url, download=False)

        except DownloadError as e:
            raise RuntimeError(f"Could not analyze video:\n{e}")

        return VideoInfo(
            title=info.get("title", ""),
            uploader=info.get("uploader", ""),
            duration=info.get("duration", 0),
            upload_date=info.get("upload_date"),
            webpage_url=info.get("webpage_url", ""),
            thumbnail=info.get("thumbnail"),
        )