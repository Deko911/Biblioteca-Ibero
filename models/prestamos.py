from typing import Tuple

from db.db import cursor
from lib.tipos import Usuario, Libro
from models.libros import LibroModel

class PrestamoModel:
    
    @staticmethod
    def prestar_libro(usuario: Usuario, libro: Libro) -> Tuple[int, int] | None:
        if LibroModel.obtener_libro_por_id(libro.id) == None:
            return None
        sql = "INSERT INTO Prestamo (usuario_id, libro_id) VALUES (?, ?)"
        try:
            cursor.execute(sql, (usuario.id, libro.id))
            usuario.prestamos[libro.id] = libro
            libro.libre = False
            LibroModel.editar_libro(libro)
            return (usuario.id, libro.id)
        except:
            if not usuario.prestamos.get(libro.id) is None:
                usuario.prestamos.pop(libro.id)
            libro.libre = True
            return None
    
    @staticmethod
    def devolver_libro(usuario: Usuario, libro: Libro) -> bool:
        sql = "DELETE FROM Prestamo WHERE usuario_id = ? AND libro_id = ?"
        try:
            cursor.execute(sql, (usuario.id, libro.id))
            usuario.prestamos.pop(libro.id)
            libro.libre = True
            LibroModel.editar_libro(libro)
            return True
        except:
            usuario.prestamos[libro.id] = libro
            libro.libre = False
            return False
    
    @staticmethod
    def obtener_prestamos() -> list[Tuple[int, int]] | None:
        sql = "SELECT * FROM Prestamo"
        prestamos = []
        try:
            filas = cursor.execute(sql)
            for fila in filas:
                prestamos.append((fila[0], fila[1]))
            return prestamos
        except:
            return None
    