import customtkinter as ctk

from core.analyzer import Analyzer
from services.thumbnail_service import ThumbnailService
from ui.components.video_card import VideoCard


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT-DLP Downloader")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        # Services
        self.analyzer = Analyzer()
        self.thumbnail_service = ThumbnailService()

        # Configure layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns",
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="YT-DLP",
            font=("Segoe UI", 26, "bold"),
        )

        title.pack(pady=(30, 40))

        buttons = [
            "🏠 Home",
            "📥 Queue",
            "📜 History",
            "⚙ Settings",
        ]

        for text in buttons:
            button = ctk.CTkButton(
                self.sidebar,
                text=text,
                width=170,
            )

            button.pack(pady=8)

    def create_main_area(self):
        self.main = ctk.CTkFrame(self)

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20,
        )

        title = ctk.CTkLabel(
            self.main,
            text="Download Video",
            font=("Segoe UI", 28, "bold"),
        )

        title.pack(anchor="w", pady=(20, 20))

        self.url = ctk.CTkEntry(
            self.main,
            height=42,
            placeholder_text="Paste a YouTube or video URL...",
        )

        self.url.pack(
            fill="x",
            padx=20,
        )

        analyze_button = ctk.CTkButton(
            self.main,
            text="Analyze Video",
            width=180,
            command=self.analyze_video,
        )

        analyze_button.pack(pady=20)

        self.video_card = VideoCard(self.main)

        self.video_card.pack(
            fill="x",
            padx=20,
            pady=20,
        )

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


if __name__ == "__main__":
    app = App()
    app.mainloop()