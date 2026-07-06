from dataclasses import dataclass
from typing import Optional


@dataclass
class VideoInfo:
    title: str
    uploader: str
    duration: int
    upload_date: Optional[str]
    webpage_url: str
    thumbnail: Optional[str]