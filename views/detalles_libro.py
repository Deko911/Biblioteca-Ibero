import customtkinter as ctk

from lib.biblioteca import Biblioteca, Libro
from lib.imagenes import imagenes
from lib.config import fuentes, colores

from views.view import View
from views.editar_libro import EditarLibroView
from views.dialogs import enviar_confirmacion, enviar_popup

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class DetallesLibroView(View): 
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        self.libro: Libro | None = None
        
        self.libro_icono = ctk.CTkImage(imagenes['libro_icono_light'], imagenes['libro_icono_dark'], (200, 200))
        
    def generar_ui(self):
        if self.app.usuario is None or self.libro is None: return
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        if self.libro is None: return
        
        label = ctk.CTkLabel(self.frame, text=f"{self.libro.nombre}", font=fuentes["title_font"])
        label.pack(pady=20)
        
        frame_boton = ctk.CTkFrame(self.frame, fg_color='transparent', width=10)
        frame_boton.pack(fill='x')
        frame_boton.columnconfigure(0, weight=1)
        
        volver_boton = ctk.CTkButton(frame_boton, text='Volver', font=fuentes["normal_font"], command=self.app.pantalla_principal)
        volver_boton.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        
        detalles_frame = ctk.CTkScrollableFrame(self.frame, fg_color='transparent')
        detalles_frame.pack(pady=5, fill='both', expand=True)
        
        ctk.CTkLabel(detalles_frame, image=self.libro_icono, text='').pack()
        ctk.CTkLabel(detalles_frame, text=f'Autor: {self.libro.autor}', font=fuentes["normal_font"]).pack(anchor='w', padx=20)
        ctk.CTkLabel(detalles_frame, text=f'Año de publicación: {self.libro.año}', font=fuentes["normal_font"]).pack(anchor='w', padx=20)
        ctk.CTkLabel(detalles_frame, text=f'Estado: {"Disponible" if self.libro.libre else "Prestado"}', font=fuentes["normal_font"], 
                    text_color=colores["libre"] if self.libro.libre else colores["prestado"]).pack(anchor='w', padx=20)
        ctk.CTkLabel(detalles_frame, text=f'Descripción: ', font=fuentes["normal_font"]).pack(anchor='w', padx=20)
        ctk.CTkLabel(detalles_frame, text=self.libro.descripcion, font=fuentes["details_font"], justify='left', wraplength=(self.app.width - 250)).pack(anchor='w', padx=30, pady=(0, 15))
        
        estado_botones = 'normal' if self.libro.libre else 'disabled'
        
        if self.biblioteca.buscar_prestamo(self.app.usuario, self.libro.id) is not None:
            ctk.CTkButton(detalles_frame, text='Devolver Libro', width=200, height=40, fg_color=colores["prestar_boton"], hover_color=colores["prestar_boton_hover"], 
                          command=lambda: self.devolver_libro()).pack(pady=10)
        else:
            ctk.CTkButton(detalles_frame, text='Prestar Libro', width=200, height=40, fg_color=colores["prestar_boton"], hover_color=colores["prestar_boton_hover"],
                      command=lambda: self.prestar_libro(), state=estado_botones).pack(pady=10)
        
        botones_frame = ctk.CTkFrame(detalles_frame, fg_color='transparent')
        botones_frame.pack(fill='x')
        botones_frame.columnconfigure(0, weight=1)
        botones_frame.columnconfigure(1, weight=1)
        
        ctk.CTkButton(botones_frame, text='Editar Libro', width=200, height=40,
                      command=lambda: self.editar_libro(), state=estado_botones).grid(row=0, column=0)
        ctk.CTkButton(botones_frame, text='Eliminar Libro', width=200, height=40, fg_color="#d32525", hover_color="#b60000", 
                      command=lambda: self.eliminar_libro(), state=estado_botones).grid(row=0, column=1)
    
    def devolver_libro(self):
        if self.libro is None or self.app.usuario is None: return
        
        if not enviar_confirmacion(self.app, '¿Esta seguro de devolver este libro?'): return
        
        resultado = self.biblioteca.devolver_libro(self.libro.id, self.app.usuario)
        if not resultado:
            enviar_popup(self.app, "No se pudo devolver el libro.")
            return
        self.generar_ui()
    
    def prestar_libro(self): 
        if self.libro is None or self.app.usuario is None: return
        
        if not enviar_confirmacion(self.app, '¿Esta seguro de prestar este libro?'): return
        
        resultado = self.biblioteca.prestar_libro(self.libro.id, self.app.usuario)
        if not resultado:
            enviar_popup(self.app, "El libro ya ha sido prestado.")
            return
        self.generar_ui()
    
    def ver_libro(self, libro: Libro):
        self.libro = libro
        self.generar_ui()
    
    def editar_libro(self):
        if not self.libro or not self.libro.libre: return
        self.app.editar_libro(self.libro)
    
    def eliminar_libro(self):
        if self.libro is None or not self.libro.libre: return
        if not enviar_confirmacion(self.app, '¿Esta seguro de eliminar este libro?'):
            return
        self.biblioteca.eliminar_libro(self.libro.id)
        self.app.actualizar_frames()
        self.app.pantalla_principal()
        