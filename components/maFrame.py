
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pytube import YouTube

class zeframe(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Champs pour l'URL
        self.champs_url = ttk.Entry(self, width=70)

        # Creation du placeHolder
        self.champs_url.insert(0, "Entrez l'URL à Télécharger")
        self.champs_url.pack()

        # Suprression du placeHolder quand User clique dans le champs_url
        self.champs_url.bind('<FocusIn>', self.remove)

        # Ajout du boutton Télécharger
        self.btn_tl = ttk.Button(self, text='Télécharger', bootstyle=(SUCCESS, OUTLINE))
        self.btn_tl.pack(pady=20)

    # Fonction pout retirer le placeHolder
    def remove(self, event):
        self.champs_url.delete(0, END)
    
