import customtkinter as ctk

from models.video_info import VideoInfo


class VideoCard(ctk.CTkFrame):
    """Displays information about the analyzed video."""

    def __init__(self, master):
        super().__init__(master, corner_radius=12)

        self.grid_columnconfigure(1, weight=1)

        # Thumbnail placeholder
        self.thumbnail = ctk.CTkLabel(
            self,
            text="Thumbnail\ncoming soon",
            width=180,
            height=110,
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
            font=("Segoe UI", 18, "bold"),
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
            anchor="w",
        )
        self.date.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(0, 20),
            pady=(5, 20),
        )

    def show(self, video: VideoInfo) -> None:
        """Populate the card with video information."""

        self.title.configure(text=video.title)
        self.channel.configure(text=f"Channel: {video.uploader}")
        self.duration.configure(text=f"Duration: {video.duration_text}")
        self.date.configure(text=f"Upload Date: {video.upload_date_text}")