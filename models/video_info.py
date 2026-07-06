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

    @property
    def duration_text(self) -> str:
        hours = self.duration // 3600
        minutes = (self.duration % 3600) // 60
        seconds = self.duration % 60

        if hours:
            return f"{hours}:{minutes:02}:{seconds:02}"

        return f"{minutes}:{seconds:02}"

    @property
    def upload_date_text(self) -> str:
        if not self.upload_date:
            return ""

        d = self.upload_date

        return f"{d[:4]}-{d[4:6]}-{d[6:]}"