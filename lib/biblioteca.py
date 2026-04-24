from models.usuarios import UsuarioModel
from models.libros import LibroModel
from models.prestamos import PrestamoModel
from lib.tipos import *

class Biblioteca:
    def __init__(self):
        self._libros: list[Libro] = []
        self._libros_id: dict[int, Libro] = {}
        self._usuarios: dict[int, Usuario] = {}
        
        self.cargar_bd()
        
    @property
    def usuarios(self): 
        usuarios = [UsuarioSeguro(usuario) for usuario in self._usuarios.values()]
        return usuarios

    @property
    def libros(self):
        return self._libros
    
    def cargar_bd(self):
        usuarios = UsuarioModel.obtener_usuarios()
        libros = LibroModel.obtener_libros()
        prestamos = PrestamoModel.obtener_prestamos()
        
        if (usuarios == None or libros == None or prestamos == None):
            raise Exception("Error al cargar la informacion de la base de datos")
        
        for usuario in usuarios:
            self._usuarios[usuario.id] = usuario
            
        for libro in libros:
            self._libros.append(libro)
            self._libros_id[libro.id] = libro
            
        for (usuario_id, libro_id) in prestamos:
            libro = self._libros_id[libro_id]
            libro.libre = False
            self._usuarios[usuario_id].prestamos[libro_id] = libro
        
    def crear_libro(self, input: LibroInput):
        libro = LibroModel.crear_libro(input)
        if libro is None:
            raise Exception("Error al guardar libros en la base de datos")
        return libro
        
    def agregar_libro(self, libro: LibroInput):
        nuevo_libro = self.crear_libro(libro)
        self._libros.append(nuevo_libro)
        self._libros_id[nuevo_libro.id] = nuevo_libro
        
    def obtener_libro(self, id=0):
        return self._libros_id[id]
    
    def editar_libro(self, nuevo_libro: LibroInput, id=0):
        libro = self.obtener_libro(id)
        libro.actualizar_libro(nuevo_libro)
        LibroModel.editar_libro(libro)
        return libro
    
    def eliminar_libro(self, id=-1):
        if id == -1: return self._libros.pop()
        ids = [libro.id for libro in self._libros]
        idx = ids.index(id)
        libro = self._libros.pop(idx)
        if not LibroModel.eliminar_libro(libro.id):
            raise Exception("Error al eliminar libros de la base de datos")
        
        return self._libros_id.pop(libro.id)
    
    def registrar_usuario(self, input: UsuarioInput):
        usuario = UsuarioModel.crear_usuario(input)
        if usuario is None:
            return None
        self._usuarios[usuario.id] = usuario
        
        return usuario
        
    def ingresar_usuario(self, nombre: str, contraseña: str):
        usuario = UsuarioModel.obtener_usuario_por_nombre(nombre)

        if usuario == None:
            return None
        
        if usuario._contraseña != contraseña:
            return None
        
        usuario = self._usuarios[usuario.id]
        return usuario
    
    def prestar_libro(self, libro_id: int, usuario: Usuario):
        libro = self.obtener_libro(libro_id)
        if not libro.libre: return False
        
        if PrestamoModel.prestar_libro(usuario, libro) is None:
            raise Exception("Error al guardar prestamos de la base de datos")
        return True
    
    def devolver_libro(self, libro_id: int, usuario: Usuario):
        libro = self.buscar_prestamo(usuario, libro_id)
        if libro is None: return False
        
        if not PrestamoModel.devolver_libro(usuario, libro):
            raise Exception("Error al eliminar prestamos de la base de datos")
        
        return True
    
    def buscar_prestamo(self, usuario: Usuario, libro_id: int):
        return usuario.prestamos.get(libro_id)
    
    def __str__(self) -> str:
        return f"Biblioteca Ibero \n Libros: \n {"\n ".join([f"- {libro}" for libro in self._libros])}"
    
def formatear_descripcion(descripcion: str):
    lineas = descripcion.splitlines()
    return '\n'.join([linea.strip() for linea in lineas])