
import tkinter as tk
import ttkbootstrap as ttk
from components.maFrame import zeframe
from ttkbootstrap.constants import *
from pytube import YouTube

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.style = ttk.Style('vapor')
        self.title('Youtube Téléchargeur')
        self.geometry('800x400')
        self.minsize(width=500, height=250)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Insertion de la Frame principale
        self.ze_frame = zeframe(self)
        self.ze_frame.grid(column=0, row=0)

app = App()
app.mainloop()
