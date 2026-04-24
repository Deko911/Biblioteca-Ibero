import customtkinter as ctk

from lib.biblioteca import Biblioteca, Libro, LibroInput, formatear_descripcion
from lib.imagenes import imagenes
from lib.config import fuentes

from views.view import View
from views.dialogs import enviar_confirmacion, enviar_popup

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class EditarLibroView(View): 
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        self.libro: Libro | None = None
        
        self.libro_icono = ctk.CTkImage(imagenes['libro_icono_light'], imagenes['libro_icono_dark'], (200, 200))
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        if self.libro is None: return
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        title = ctk.CTkLabel(self.frame, text="Editar Libro", font=fuentes["title_font"])
        title.pack(pady=20)
        
        frame_boton = ctk.CTkFrame(self.frame, fg_color='transparent', width=10)
        frame_boton.pack(fill='x')
        frame_boton.columnconfigure(0, weight=1)
        
        volver_boton = ctk.CTkButton(frame_boton, text='Volver', font=fuentes["normal_font"], command=self.app.pantalla_principal)
        volver_boton.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        
        scrollable_frame = ctk.CTkScrollableFrame(self.frame)
        scrollable_frame.pack(fill="both", expand=True, padx=0, pady=0)
        scrollable_frame.grid_columnconfigure(0, weight=1)
        
        nombre_label = ctk.CTkLabel(scrollable_frame, text="Nombre del libro", font=fuentes["normal_font"])
        nombre_label.pack(pady=5, padx=40, anchor="w")
        self.nombre_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el nombre", font=fuentes["input_font"])
        self.nombre_input.insert(0, self.libro.nombre)
        self.nombre_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.nombre_input.bind('<Return>', self.manejar_enter)
        
        autor_label = ctk.CTkLabel(scrollable_frame, text="Nombre del Autor", font=fuentes["normal_font"])
        autor_label.pack(pady=5, padx=40, anchor="w")
        self.autor_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el autor", font=fuentes["input_font"])
        self.autor_input.insert(0, self.libro.autor)
        self.autor_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.autor_input.bind('<Return>', self.manejar_enter)
        
        año_label = ctk.CTkLabel(scrollable_frame, text="Año de publicación", font=fuentes["normal_font"])
        año_label.pack(pady=5, padx=40, anchor="w")
        self.año_input = ctk.CTkEntry(scrollable_frame, placeholder_text="Ingrese el año de publicación", font=fuentes["input_font"])
        self.año_input.insert(0, self.libro.año)
        self.año_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.año_input.bind('<Return>', self.manejar_enter)
        
        descripcion_label = ctk.CTkLabel(scrollable_frame, text="Descripcion del libro", font=fuentes["normal_font"])
        descripcion_label.pack(pady=5, padx=40, anchor="w")
        self.descripcion_input = ctk.CTkTextbox(scrollable_frame, font=fuentes["input_font"])
        self.descripcion_input.insert("0.0", self.libro.descripcion)
        self.descripcion_input.pack(pady=(5, 20), padx=40, anchor="w", fill="x")
        self.descripcion_input.bind('<Return>', self.manejar_enter)
        
        crear_boton = ctk.CTkButton(scrollable_frame, text="Guardar", font=fuentes["button_font"], command=self.ingresar_formulario)
        crear_boton.pack(pady=20)
        
    def manejar_enter(self, event):
        if event.state & 0x0001:  # Shift está activo
            return
        self.ingresar_formulario()
        
    def ingresar_formulario(self):
        if self.libro is None:
            return
        if not self.nombre_input or not self.autor_input or not self.año_input or not self.descripcion_input:
            raise Exception("campos de entrada no inicializados.")
        
        nombre = self.nombre_input.get()
        autor = self.autor_input.get()
        año_input = self.año_input.get()
        descripcion = self.descripcion_input.get("0.0", 'end').strip()
        descripcion = formatear_descripcion(descripcion)
        
        if nombre == "":
            enviar_popup(self.app, "Por favor ingrese el nombre del libro.", True)
            return
        if autor == "":
            enviar_popup(self.app, "Por favor ingrese el nombre del autor del libro.", True)
            return
        try:
            año = int(año_input)
            if año <= 0: raise Exception("Año invalido")
        except:
            enviar_popup(self.app, "Año inválido. Por favor ingrese un año válido.", True)
            return
        if descripcion == "" or descripcion == "Ingrese la descripción del libro":
            enviar_popup(self.app, "Por favor ingrese la descripción del libro.", True)
            return
        
        libro_input = LibroInput(nombre, autor, año, descripcion)
        
        if not enviar_confirmacion(self.app, '¿Estas seguro de editar este libro?'):
            return

        self.libro = self.biblioteca.editar_libro(libro_input, self.libro.id)
        enviar_popup(self.app, "Libro modificado exitosamente", False)
        
        self.app.pantalla_principal()
        
    def editar_libro(self, libro: Libro):
        self.libro = libro
        self.generar_ui()
        
    def actualizar_frame(self):
        pass
        