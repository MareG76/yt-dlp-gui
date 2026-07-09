from pathlib import Path
import threading

import customtkinter as ctk

from core.analyzer import Analyzer
from core.downloader import Downloader
from services.thumbnail_service import ThumbnailService

from ui import theme
from ui.components.url_bar import UrlBar
from ui.components.video_card import VideoCard
from ui.components.download_panel import DownloadPanel
from ui.components.progress_panel import ProgressPanel

from tkinter import filedialog

class HomePage(ctk.CTkFrame):
    """Main page of the application."""

    def __init__(self, master):
        super().__init__(master)

        self.analyzer = Analyzer()
        self.downloader = Downloader()
        self.thumbnail_service = ThumbnailService()

        self.current_video = None

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="Download Video",
            font=theme.TITLE_FONT,
        )
        title.pack(
            anchor="w",
            padx=theme.PADDING,
            pady=(theme.PADDING, theme.PADDING),
        )

        # URL Bar
        self.url_bar = UrlBar(
            self,
            self.analyze_video,
        )

        self.url_bar.pack(
            fill="x",
            padx=theme.PADDING,
        )

        # Video Card
        self.video_card = VideoCard(self)

        self.video_card.pack(
            fill="x",
            padx=theme.PADDING,
            pady=theme.PADDING,
        )

        # Download Panel
        self.download_panel = DownloadPanel(
            self,
            self.download_video,
            self.browse_folder,
        )

        self.download_panel.pack(
            fill="x",
            padx=theme.PADDING,
            pady=(0, theme.PADDING),
        )

        # Progress Panel
        self.progress_panel = ProgressPanel(self)

        self.progress_panel.pack(
            fill="x",
            padx=theme.PADDING,
            pady=(0, theme.PADDING),
        )

    def analyze_video(self):
        url = self.url_bar.get().strip()

        if not url:
            return

        self.progress_panel.set_status("Analyzing...")
        self.progress_panel.update_progress(0, "-", "-")

        try:
            video = self.analyzer.analyze(url)
            self.current_video = video

            image = self.thumbnail_service.download(video.thumbnail)

            self.video_card.set_thumbnail(image)
            self.video_card.show(video)

            self.progress_panel.set_status("Ready to download")

        except Exception as error:
            self.progress_panel.set_status("Analysis failed")
            print(error)

    def download_video(self):
        if self.current_video is None:
            print("Please analyze a video first.")
            return

        thread = threading.Thread(
            target=self.start_download,
            daemon=True,
        )

        thread.start()

    def start_download(self):
        folder = self.download_panel.folder.get().strip()

        if not folder:
            folder = str(Path("downloads").resolve())

        quality = self.download_panel.quality.get()

        self.after(
            0,
            lambda: self.progress_panel.set_status("Downloading...")
        )

        try:
            self.downloader.download(
                self.current_video.webpage_url,
                folder,
                quality,
                self.progress_hook,
            )

            self.after(
                0,
                lambda: self.progress_panel.set_status("Download completed!")
            )

        except Exception as error:
            self.after(
                0,
                lambda: self.progress_panel.set_status("Download failed")
            )

            print(error)

    def browse_folder(self):
        folder = filedialog.askdirectory()

        if folder:
            self.download_panel.folder.delete(0, "end")
            self.download_panel.folder.insert(0, folder)
    
    def progress_hook(self, d):
        status = d.get("status")

        if status == "downloading":

            total = (
                d.get("total_bytes")
                or d.get("total_bytes_estimate")
                or 0
            )

            downloaded = d.get("downloaded_bytes", 0)

            if total > 0:
                percent = downloaded / total * 100
            else:
                percent = 0

            speed = d.get("speed")

            if speed:
                speed_text = f"{speed / 1024 / 1024:.2f} MB/s"
            else:
                speed_text = "-"

            eta = d.get("eta")

            if eta is None:
                eta_text = "-"
            else:
                minutes = eta // 60
                seconds = eta % 60
                eta_text = f"{minutes:02}:{seconds:02}"

            self.after(
                0,
                lambda p=percent, s=speed_text, e=eta_text:
                self.progress_panel.update_progress(
                    p,
                    s,
                    e,
                ),
            )

        elif status == "finished":

            self.after(
                0,
                lambda: self.progress_panel.set_status(
                    "Processing downloaded file..."
                ),
            )