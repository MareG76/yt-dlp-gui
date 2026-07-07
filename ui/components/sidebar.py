import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """Application sidebar."""

    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)

        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(
            self,
            text="YT-DLP",
            font=("Segoe UI", 26, "bold"),
        )
        title.pack(pady=(30, 40))

        self.home_button = ctk.CTkButton(
            self,
            text="🏠 Home",
        )
        self.home_button.pack(pady=8, padx=20, fill="x")

        self.queue_button = ctk.CTkButton(
            self,
            text="📥 Queue",
        )
        self.queue_button.pack(pady=8, padx=20, fill="x")

        self.history_button = ctk.CTkButton(
            self,
            text="📜 History",
        )
        self.history_button.pack(pady=8, padx=20, fill="x")

        self.settings_button = ctk.CTkButton(
            self,
            text="⚙ Settings",
        )
        self.settings_button.pack(pady=8, padx=20, fill="x")