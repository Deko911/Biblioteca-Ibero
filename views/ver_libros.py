import customtkinter as ctk

from lib.biblioteca import Biblioteca, Libro
from lib.imagenes import imagenes
from lib.config import fuentes

from views.view import View

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class VerLibrosView(View): 

    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        
        self.libro_icono = ctk.CTkImage(imagenes['libro_icono_light'], imagenes['libro_icono_dark'], (100, 100))
        
        self.generar_ui()
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        label = ctk.CTkLabel(self.frame, text="Ver Libros", font=fuentes["title_font"])
        label.pack(pady=20)
        
        num_cols =  max(1, self.app.width // 400)
        
        max_width = (self.app.width - 400) // num_cols
        
        
        libros_grid = ctk.CTkScrollableFrame(self.frame)
        libros_grid.pack(pady=5, fill='both', expand=True)
        
        
        for col in range(num_cols):
            libros_grid.grid_columnconfigure(col, weight=1, uniform="col")
            
        #Vista limitada a 20 libros
        for i, libro in enumerate(self.biblioteca.libros[:20]):
            libro_frame = ctk.CTkFrame(libros_grid, fg_color='#333333')
            pady = (10, 10) if i // num_cols == 0 else (0, 10)
            libro_frame.grid(row=i // num_cols, column=i % num_cols, sticky="nsew", pady=pady, padx=5)
            ctk.CTkLabel(libro_frame, text=f"Nombre: {libro.nombre}", font=fuentes["preview_name_font"], wraplength=max_width - 10, justify='left').pack(pady=(10, 0))
            ctk.CTkLabel(libro_frame, image=self.libro_icono, text='').pack()
            ctk.CTkLabel(libro_frame, text=f"Autor: {libro.autor}", font=fuentes["preview_autor_font"], wraplength=max_width - 10, justify='left').pack()
            self.detectar_hover(libro_frame, libro)
            
            
    def detectar_hover(self, frame: ctk.CTkBaseClass, libro: Libro):
        for widget in [frame] + frame.winfo_children():
            widget.bind("<Enter>", lambda _: hover_libro(frame))
            widget.bind("<Leave>", lambda _: unhover_libro(frame))
            widget.bind("<Button-1>", lambda _: click_libro(libro, self.app))
    
def hover_libro(frame):
    frame.configure(fg_color='#222222')
    
def unhover_libro(frame):
    frame.configure(fg_color='#333333')
        
def click_libro(libro: Libro, app: App):
    app.mostrar_libro(libro)