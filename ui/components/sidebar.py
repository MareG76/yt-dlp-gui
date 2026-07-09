import customtkinter as ctk

from ui import theme


class Sidebar(ctk.CTkFrame):
    """Application sidebar."""

    def __init__(self, master):
        super().__init__(
            master,
            width=theme.SIDEBAR_WIDTH,
            corner_radius=0,
            fg_color=theme.SIDEBAR,
        )

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="YT-DLP",
            font=theme.HEADING_FONT,
        )
        title.pack(pady=(30, 40))

        self.home_button = ctk.CTkButton(
            self,
            text="🏠 Home",
            fg_color="transparent",
            hover_color=theme.ACCENT,
            anchor="w",
        )
        self.home_button.pack(fill="x", padx=20, pady=6)

        self.queue_button = ctk.CTkButton(
            self,
            text="📥 Queue",
            fg_color="transparent",
            hover_color=theme.ACCENT,
            anchor="w",
        )
        self.queue_button.pack(fill="x", padx=20, pady=6)

        self.history_button = ctk.CTkButton(
            self,
            text="📜 History",
            fg_color="transparent",
            hover_color=theme.ACCENT,
            anchor="w",
        )
        self.history_button.pack(fill="x", padx=20, pady=6)

        self.settings_button = ctk.CTkButton(
            self,
            text="⚙ Settings",
            fg_color="transparent",
            hover_color=theme.ACCENT,
            anchor="w",
        )
        self.settings_button.pack(fill="x", padx=20, pady=6)