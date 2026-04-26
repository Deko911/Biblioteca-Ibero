import customtkinter as ctk

from lib.biblioteca import Biblioteca, Libro
from lib.imagenes import imagenes
from lib.config import fuentes

from views.view import View

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App
    
class LibroCard(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkScrollableFrame, libro: Libro, row=0, column=0, pady=(0, 0), padx=(0, 0), wraplength=0, icono=None):
        super().__init__(parent, fg_color='#333333')
        self.grid(row=row, column=column, sticky="nsew", pady=pady, padx=padx)
        
        self.nombre = ctk.CTkLabel(self, text=f"Nombre: {libro.nombre}", font=fuentes["preview_name_font"], wraplength=wraplength, justify='left')
        self.nombre.pack(pady=(10, 0))
        
        self.imagen = ctk.CTkLabel(self, image=icono, text='')
        self.imagen.pack()
        
        self.autor = ctk.CTkLabel(self, text=f"Autor: {libro.autor}", font=fuentes["preview_autor_font"], wraplength=wraplength - 10, justify='left')
        self.autor.pack()
        
        self.visible = True
        
    def actualizar(self, libro: Libro, wraplength=0):
        self.nombre.configure(text=f"Nombre: {libro.nombre}", wraplength=wraplength)
        self.autor.configure(text=f"Autor: {libro.autor}", wraplength=wraplength)
        
    def cambiar_visibilidad(self, mostrar: bool):
        self.visible = mostrar
        if mostrar:
            self.grid()
        else:
            self.grid_remove()
        

class VerLibrosView(View): 

    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        self.app = controller
        self.biblioteca = biblioteca
        self.libros_ui: list[LibroCard] = []
        
        self.frame = None
        self.libros_info = None
        self.columnas = 0
        
        self.libro_icono = ctk.CTkImage(imagenes['libro_icono_light'], imagenes['libro_icono_dark'], (100, 100))
        
        self.libros_grid = None
        self.barra_busqueda = None
        self.texto_busqueda = ""
        self.resultados = self.biblioteca.libros
        
        self.generar_ui()
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        label = ctk.CTkLabel(self.frame, text="Ver Libros", font=fuentes["title_font"])
        label.pack(pady=20)
        
        self.barra_busqueda = ctk.CTkEntry(self.frame, placeholder_text="Buscar por nombre de libro...", font=fuentes["details_font"])
        self.barra_busqueda.insert(0, self.texto_busqueda)
        self.barra_busqueda.pack(pady=(0, 10), padx=20, fill='x')
        self.barra_busqueda.bind("<KeyRelease>", self.on_busqueda_cambiada)
        self.barra_busqueda.focus()
        
        self.libros_info = ctk.CTkLabel(self.frame, font=fuentes["details_font"])
        self.libros_info.pack()
        if len(self.resultados) > 20:
            self.libros_info.configure(text=f"Se encontraron {len(self.biblioteca.libros)} libros, resultados limitados a 20.")
        elif len(self.resultados) == 0:
            self.libros_info.configure(text="No se encontraron libros.")
        else:
            self.libros_info.configure(text="")
        
        num_cols =  max(1, self.app.width // 400)
        self.columnas = num_cols
        max_width = (self.app.width - 400) // num_cols
        
        self.libros_grid = ctk.CTkScrollableFrame(self.frame)
        self.libros_grid.pack(pady=5, fill='both', expand=True)
        
        for col in range(num_cols):
            self.libros_grid.grid_columnconfigure(col, weight=1, uniform="col")
            
        #Vista limitada a 20 libros
        for i, libro in enumerate(self.resultados[:20]):
            pady = (10, 10) if i // num_cols == 0 else (0, 10)
            libro_frame = LibroCard(self.libros_grid, libro, row=i // num_cols, column=i % num_cols, pady=pady, padx=5, wraplength=max_width - 10, icono=self.libro_icono)
            self.detectar_hover(libro_frame, libro)
            self.libros_ui.append(libro_frame)
    
    def actualizar_frame(self):
        self.actualizar_resultados()
        num_cols =  max(1, self.app.width // 400)
        max_width = (self.app.width - 400) // num_cols
        if not num_cols == self.columnas:
            self.columnas = num_cols
            self.generar_ui()
            return
        
        if self.libros_info is None or self.libros_grid is None:
            return
        
        self.libros_grid._parent_canvas.yview_moveto(0)
        
        if len(self.resultados) > 20:
            self.libros_info.configure(text=f"Se encontraron {len(self.biblioteca.libros)} libros, resultados limitados a 20.")
        elif len(self.resultados) == 0:
            self.libros_info.configure(text="No se encontraron libros.")
        else:
            self.libros_info.configure(text="")
        
        for i, libro_card in enumerate(self.libros_ui):
            if i >= len(self.resultados):
                libro_card.cambiar_visibilidad(False)
            else: 
                libro = self.resultados[i]
                libro_card.actualizar(libro, wraplength=max_width - 10)
                libro_card.cambiar_visibilidad(True)
                self.detectar_hover(libro_card, libro)
        
   
    def detectar_hover(self, frame: ctk.CTkBaseClass, libro: Libro):
        for widget in [frame] + frame.winfo_children():
            widget.unbind("<Enter>")
            widget.unbind("<Leave>")
            widget.unbind("<Button-1>")
            widget.bind("<Enter>", lambda _: hover_libro(frame))
            widget.bind("<Leave>", lambda _: unhover_libro(frame))
            widget.bind("<Button-1>", lambda _: click_libro(libro, self.app))
    
    def actualizar_resultados(self):
        if self.barra_busqueda is None:
            return
        texto = self.barra_busqueda.get()
        self.texto_busqueda = texto
        if texto.strip() == "":
            self.resultados = self.biblioteca.libros
        else:
            self.resultados = self.biblioteca.buscar_libros(texto)
            
    def on_busqueda_cambiada(self, event=None):
        self.actualizar_frame()
    
def hover_libro(frame):
    frame.configure(fg_color='#222222')
    
def unhover_libro(frame):
    frame.configure(fg_color='#333333')
        
def click_libro(libro: Libro, app: App):
    app.mostrar_libro(libro)