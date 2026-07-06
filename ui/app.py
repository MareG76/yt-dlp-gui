import customtkinter as ctk

from core.analyzer import Analyzer


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT-DLP Downloader")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        # Configure window grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main_area()

    def create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

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
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                width=170,
            )
            btn.pack(pady=8)

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
        self.url.pack(fill="x", padx=20)

        analyze = ctk.CTkButton(
            self.main,
            text="Analyze Video",
            width=180,
            command=self.analyze_video,
        )
        analyze.pack(pady=20)

        # ---------- Video Information ----------

        self.info_frame = ctk.CTkFrame(self.main)
        self.info_frame.pack(fill="x", padx=20, pady=20)

        self.title_label = ctk.CTkLabel(
            self.info_frame,
            text="Title: -",
            anchor="w",
        )
        self.title_label.pack(anchor="w", padx=15, pady=(15, 5))

        self.channel_label = ctk.CTkLabel(
            self.info_frame,
            text="Channel: -",
            anchor="w",
        )
        self.channel_label.pack(anchor="w", padx=15, pady=5)

        self.duration_label = ctk.CTkLabel(
            self.info_frame,
            text="Duration: -",
            anchor="w",
        )
        self.duration_label.pack(anchor="w", padx=15, pady=5)

        self.date_label = ctk.CTkLabel(
            self.info_frame,
            text="Upload Date: -",
            anchor="w",
        )
        self.date_label.pack(anchor="w", padx=15, pady=(5, 15))

    def analyze_video(self):
        url = self.url.get().strip()

        if not url:
            return

        try:
            video = Analyzer().analyze(url)

            self.title_label.configure(
                text=f"Title: {video.title}"
            )

            self.channel_label.configure(
                text=f"Channel: {video.uploader}"
            )

            self.duration_label.configure(
                text=f"Duration: {video.duration_text}"
            )

            self.date_label.configure(
                text=f"Upload Date: {video.upload_date_text}"
            )

        except Exception as e:
            self.title_label.configure(text=f"Error: {e}")
            self.channel_label.configure(text="")
            self.duration_label.configure(text="")
            self.date_label.configure(text="")