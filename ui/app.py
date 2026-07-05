import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("YT-DLP Downloader")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        # Configure the main window grid
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
            font=("Segoe UI", 26, "bold")
        )
        title.pack(pady=(30, 40))

        buttons = [
            "🏠 Home",
            "📥 Queue",
            "📜 History",
            "⚙ Settings"
        ]

        for text in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                width=170
            )
            btn.pack(pady=8)

    def create_main_area(self):

        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        title = ctk.CTkLabel(
            self.main,
            text="Download Video",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w", pady=(20, 20))

        self.url = ctk.CTkEntry(
            self.main,
            height=42,
            placeholder_text="Paste a YouTube or video URL..."
        )
        self.url.pack(fill="x", padx=20)

        analyze = ctk.CTkButton(
            self.main,
            text="Analyze Video",
            width=180
        )
        analyze.pack(pady=20)