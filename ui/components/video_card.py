import customtkinter as ctk

from customtkinter import CTkImage
from PIL import Image

from models.video_info import VideoInfo
from ui import theme


class VideoCard(ctk.CTkFrame):
    """Displays information about the analyzed video."""

    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=theme.CARD_RADIUS,
            fg_color=theme.CARD,
        )

        self.grid_columnconfigure(1, weight=1)

        self.thumbnail = ctk.CTkLabel(
            self,
            text="",
            width=220,
            height=124,
        )
        self.thumbnail.grid(
            row=0,
            column=0,
            rowspan=4,
            padx=20,
            pady=20,
        )

        self.title = ctk.CTkLabel(
            self,
            text="Title",
            font=theme.HEADING_FONT,
            anchor="w",
        )
        self.title.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(0, 20),
            pady=(20, 5),
        )

        self.channel = ctk.CTkLabel(
            self,
            text="Channel",
            font=theme.BODY_FONT,
            anchor="w",
        )
        self.channel.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(0, 20),
            pady=5,
        )

        self.duration = ctk.CTkLabel(
            self,
            text="Duration",
            font=theme.BODY_FONT,
            anchor="w",
        )
        self.duration.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(0, 20),
            pady=5,
        )

        self.date = ctk.CTkLabel(
            self,
            text="Upload Date",
            font=theme.BODY_FONT,
            anchor="w",
        )
        self.date.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(0, 20),
            pady=(5, 20),
        )

    def show(self, video: VideoInfo):
        self.title.configure(text=video.title)
        self.channel.configure(text=f"Channel: {video.uploader}")
        self.duration.configure(text=f"Duration: {video.duration_text}")
        self.date.configure(text=f"Upload Date: {video.upload_date_text}")

    def set_thumbnail(self, image: Image.Image | None):
        if image is None:
            self.thumbnail.configure(text="No Thumbnail", image=None)
            return

        image = image.resize((220, 124))

        self.thumbnail_image = CTkImage(
            light_image=image,
            dark_image=image,
            size=(220, 124),
        )

        self.thumbnail.configure(
            image=self.thumbnail_image,
            text="",
        )