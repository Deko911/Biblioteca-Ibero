import customtkinter as ctk

from lib.biblioteca import Biblioteca, UsuarioInput
from lib.biblioteca import LibroInput
from app import App

biblioteca = Biblioteca()

app = App(biblioteca)

app.mainloop()