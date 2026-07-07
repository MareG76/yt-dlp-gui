import customtkinter as ctk

from ui.pages.home_page import HomePage
from ui.components.sidebar import Sidebar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("YT-DLP Downloader")
        self.geometry("1200x750")
        self.minsize(1000, 650)

        # Configure window layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns",
        )

        self.home_page = HomePage(self)
        self.home_page.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20,
        )

    

if __name__ == "__main__":
    app = App()
    app.mainloop()