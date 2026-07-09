import customtkinter as ctk


class UrlBar(ctk.CTkFrame):
    """URL entry with Paste and Analyze buttons."""

    def __init__(self, master, analyze_callback):
        super().__init__(master, fg_color="transparent")

        self.analyze_callback = analyze_callback

        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(
            self,
            height=40,
            placeholder_text="Paste a YouTube or video URL...",
        )
        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10),
        )

        self.paste_button = ctk.CTkButton(
            self,
            text="📋 Paste",
            width=100,
            command=self.paste,
        )
        self.paste_button.grid(
            row=0,
            column=1,
            padx=(0, 10),
        )

        self.analyze_button = ctk.CTkButton(
            self,
            text="Analyze",
            width=120,
            command=self.analyze_callback,
        )
        self.analyze_button.grid(
            row=0,
            column=2,
        )

        # Press Enter to analyze
        self.entry.bind("<Return>", lambda e: self.analyze_callback())

    def paste(self):
        try:
            text = self.clipboard_get()

            self.entry.delete(0, "end")
            self.entry.insert(0, text)

        except Exception:
            pass

    def get(self):
        return self.entry.get()