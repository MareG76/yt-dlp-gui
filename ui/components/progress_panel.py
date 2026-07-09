import customtkinter as ctk


class ProgressPanel(ctk.CTkFrame):
    """Shows download progress."""

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="Download Progress",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(anchor="w", padx=20, pady=(20, 10))

        self.status = ctk.CTkLabel(
            self,
            text="Waiting...",
            anchor="w",
        )
        self.status.pack(fill="x", padx=20)

        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=20, pady=10)
        self.progress.set(0)

        self.percent = ctk.CTkLabel(
            self,
            text="0%",
        )
        self.percent.pack()

        self.speed = ctk.CTkLabel(
            self,
            text="Speed: -",
        )
        self.speed.pack()

        self.eta = ctk.CTkLabel(
            self,
            text="ETA: -",
        )
        self.eta.pack(pady=(0, 20))

    def update_progress(self, percent, speed, eta):

        self.progress.set(percent / 100)

        self.percent.configure(
            text=f"{percent:.1f}%"
        )

        self.speed.configure(
            text=f"Speed: {speed}"
        )

        self.eta.configure(
            text=f"ETA: {eta}"
        )

    def set_status(self, text):
        self.status.configure(text=text)