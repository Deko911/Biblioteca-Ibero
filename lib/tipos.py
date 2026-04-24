class Libro:
    def __init__(self, id: int, nombre: str, autor: str, año: int, descripcion: str, libre: bool):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.descripcion = descripcion
        self.libre = libre
        
    def __str__(self) -> str:
        estado = "Disponible" if self.libre else "Prestado"
        return f"Id: {self.id} - Nombre: {self.nombre} - Autor: {self.autor} - Año: {self.año} - Estado: {estado}"
    
    def actualizar_libro(self, input: LibroInput):
        self.nombre = input.nombre
        self.autor = input.autor
        self.año = input.año
        self.descripcion = input.descripcion
        
class LibroInput:
    def __init__(self, nombre: str, autor: str, año: int, descripcion: str):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.descripcion = descripcion
        
class Usuario:
    def __init__(self, id: int, nombre: str, contraseña: str):
        self.id = id
        self.nombre = nombre
        self._contraseña = contraseña
        self.prestamos: dict[int, Libro] = {}
        
class UsuarioInput:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self._contraseña = contraseña
        self.prestamos: dict[int, Libro] = {}
        
class UsuarioSeguro:
    def __init__(self, usuario: Usuario):
        self.id = usuario.id
        self.nombre = usuario.nombre
        self.prestamos = usuario.prestamos