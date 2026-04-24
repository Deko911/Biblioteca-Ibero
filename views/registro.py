import customtkinter as ctk

from lib.biblioteca import Biblioteca, UsuarioInput
from lib.config import fuentes

from views.view import View
from views.dialogs import enviar_popup


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import App

class RegistroView(View): 
    def __init__(self, parent: ctk.CTkBaseClass, controller: App, biblioteca: Biblioteca):
        super().__init__(parent, controller, biblioteca)
        
        self.app = controller
        self.biblioteca = biblioteca
        
        self.frame = None
        
        self.generar_ui()
        
    def generar_ui(self):
        if not self.frame is None: self.frame.destroy()
        
        self.frame = ctk.CTkFrame(self, fg_color='transparent')
        self.frame.pack(fill='both', expand=True)
        
        title = ctk.CTkLabel(self.frame, text="Ingresar Usuario", font=fuentes["title_font"])
        title.pack(pady=20)
        
        ctk.CTkLabel(self.frame, text="Nombre de usuario", font=fuentes["normal_font"]).pack(pady=5, padx=40, anchor="w")
        self.nombre_input = ctk.CTkEntry(self.frame, placeholder_text="Ingrese su nombre", font=fuentes["input_font"])
        self.nombre_input.pack(pady=10, padx=40, anchor="w", fill="x")
        self.nombre_input.bind('<Return>', self.manejar_enter)
        
        ctk.CTkLabel(self.frame, text="Contraseña", font=fuentes["normal_font"]).pack(pady=5, padx=40, anchor="w")
        self.contraseña1_input = ctk.CTkEntry(self.frame, placeholder_text="Ingrese su contraseña", font=fuentes["input_font"], show="*")
        self.contraseña1_input.pack(pady=10, padx=40, anchor="w", fill="x")
        self.contraseña1_input.bind('<Return>', self.manejar_enter)   
        
        ctk.CTkLabel(self.frame, text="Confirmar Contraseña", font=fuentes["normal_font"]).pack(pady=5, padx=40, anchor="w")
        self.contraseña2_input = ctk.CTkEntry(self.frame, placeholder_text="Confirme su contraseña", font=fuentes["input_font"], show="*")
        self.contraseña2_input.pack(pady=10, padx=40, anchor="w", fill="x")
        self.contraseña2_input.bind('<Return>', self.manejar_enter)
        
        ingresar_button = ctk.CTkButton(self.frame, text="¿Ya tiene un usuario?", font=fuentes["button_font"], command=lambda: self.app.mostrar_frame_str('IngresoView'), fg_color="transparent")
        ingresar_button.pack(pady=10, padx=40, anchor="w")
        
        registrar_button = ctk.CTkButton(self.frame, text="Registrar", font=fuentes["button_font"], command=self.registrar_usuario)
        registrar_button.pack(pady=10, padx=40, anchor="w", fill="x")
        
    def actualizar_frame(self):
        pass
    
    def registrar_usuario(self):
        nombre = self.nombre_input.get()
        contraseña1 = self.contraseña1_input.get()
        contraseña2 = self.contraseña2_input.get()
        
        if not nombre or not contraseña1 or not contraseña2:
            enviar_popup(self.app, "Por favor complete todos los campos.")
            return
        
        if contraseña1 != contraseña2:
            enviar_popup(self.app,"Las contraseñas no coinciden.")
            return  
        
        usuarioInput = UsuarioInput(nombre, contraseña1)
        
        usuario = self.biblioteca.registrar_usuario(usuarioInput)
        if usuario is None:
            enviar_popup(self.app, f"Usuario '{nombre}' ya existe.")
            return
        self.app.usuario = usuario
        
        enviar_popup(self.app, f"Usuario '{nombre}' creado exitosamente.", False)
        self.app.vistas_protegidas()
        self.app.pantalla_principal()
    
    def manejar_enter(self, event):
        self.registrar_usuario()
        