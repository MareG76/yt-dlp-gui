import io

import requests
from PIL import Image


class ThumbnailService:
    """Downloads thumbnail images."""

    @staticmethod
    def download(url: str) -> Image.Image | None:
        if not url:
            return None

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            return Image.open(io.BytesIO(response.content))

        except Exception:
            return None