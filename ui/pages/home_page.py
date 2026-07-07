import customtkinter as ctk

from core.analyzer import Analyzer
from services.thumbnail_service import ThumbnailService
from ui.components.video_card import VideoCard


class HomePage(ctk.CTkFrame):
    """Main page of the application."""

    def __init__(self, master):
        super().__init__(master)

        self.analyzer = Analyzer()
        self.thumbnail_service = ThumbnailService()

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Download Video",
            font=("Segoe UI", 28, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(20, 20))

        self.url = ctk.CTkEntry(
            self,
            height=42,
            placeholder_text="Paste a YouTube or video URL...",
        )
        self.url.pack(fill="x", padx=20)

        analyze_button = ctk.CTkButton(
            self,
            text="Analyze Video",
            command=self.analyze_video,
        )
        analyze_button.pack(pady=20)

        self.video_card = VideoCard(self)
        self.video_card.pack(fill="x", padx=20, pady=20)

    def analyze_video(self):
        url = self.url.get().strip()

        if not url:
            return

        try:
            video = self.analyzer.analyze(url)

            image = self.thumbnail_service.download(video.thumbnail)

            self.video_card.set_thumbnail(image)
            self.video_card.show(video)

        except Exception as error:
            print(error)