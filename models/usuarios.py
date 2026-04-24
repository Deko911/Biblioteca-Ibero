from db.db import cursor
from lib.tipos import Usuario, UsuarioInput

class UsuarioModel:

    @staticmethod
    def obtener_usuarios() -> list[Usuario] | None:
        sql = "SELECT * FROM Usuario"
        usuarios = []
        try:
            cursor.execute(sql)
            filas = cursor.fetchall()
            for fila in filas:
                usuarios.append(Usuario(*fila))
            return usuarios
        except:
            return None

    
    @staticmethod
    def obtener_usuario_por_nombre(nombre: str) -> Usuario | None:
        sql = "SELECT * FROM Usuario WHERE nombre = ?"
        try:
            cursor.execute(sql, (nombre,))
            fila = cursor.fetchone()
            if fila == None:
                return None
                
            return Usuario(*fila)
        except:
            return None
    
    @staticmethod
    def crear_usuario(usuario: UsuarioInput) -> Usuario | None:
        sql = "INSERT INTO Usuario (nombre, contrasena) VALUES (?, ?)"
        try:
            cursor.execute(sql, (usuario.nombre, usuario._contraseña))
        except:
            return None
        
        id = cursor.lastrowid
        if id is None:
            return None
        
        return Usuario(id, usuario.nombre, usuario._contraseña)