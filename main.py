
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

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


class zeframe(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ttk.Label(self, text='Hello world')
        self.label.pack()
app = App()
app.mainloop()
