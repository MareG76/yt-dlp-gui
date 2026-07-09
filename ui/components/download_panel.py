from pathlib import Path

from tkinter import filedialog

import customtkinter as ctk


class DownloadPanel(ctk.CTkFrame):
    """Download controls."""

    def __init__(self, master, download_callback, browse_callback):
        super().__init__(master)

        self.download_callback = download_callback
        self.browse_callback = browse_callback

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="Download Options",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        self.quality = ctk.CTkOptionMenu(
            self,
            values=[
                "Best Video + Audio",
                "Best Video",
                "Best Audio",
                "MP3",
            ],
        )
        self.quality.pack(fill="x", padx=20)

        folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        folder_frame.pack(fill="x", padx=20, pady=15)

        folder_frame.grid_columnconfigure(0, weight=1)

        self.folder = ctk.CTkEntry(
            folder_frame,
            placeholder_text="Download Folder",
        )
        self.folder.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10),
        )

        default_folder = str(Path("downloads").resolve())
        self.folder.insert(0, default_folder)

        browse_button = ctk.CTkButton(
            folder_frame,
            text="Browse...",
            width=110,
            command=self.browse_callback,
        )

        browse_button.grid(
            row=0,
            column=1,
        )

        self.download_button = ctk.CTkButton(
            self,
            text="Download",
            command=self.download_callback,
        )
        self.download_button.pack(
            fill="x",
            padx=20,
            pady=(0, 20),
        )