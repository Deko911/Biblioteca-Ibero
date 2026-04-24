from db.db import cursor
from lib.tipos import Libro, LibroInput

class LibroModel:
    
    @staticmethod
    def obtener_libros() -> list[Libro] | None:
        sql = "SELECT * FROM Libro ORDER BY nombre ASC"
        libros = []
        try:
            cursor.execute(sql)
            filas = cursor.fetchall()
            for fila in filas:
                libro = Libro(*fila)
                libros.append(libro)
            return libros
        except:
            return None
        
    @staticmethod
    def obtener_libro_por_id(id: int) -> Libro | None:
        sql = "SELECT * FROM Libro WHERE id = ?"
        try:
            cursor.execute(sql, (id,))
            fila = cursor.fetchone()
            return Libro(*fila)
        except:
            return None
        
    @staticmethod
    def crear_libro(libro: LibroInput) -> Libro | None:
        sql = "INSERT INTO Libro (nombre, autor, anio, descripcion, libre) VALUES (?, ?, ?, ?, TRUE)"
        try:
            cursor.execute(sql, (libro.nombre, libro.autor, libro.año, libro.descripcion))
        except:
            return None
        
        id = cursor.lastrowid
        if id is None:
            return None
        
        return Libro(id, libro.nombre, libro.autor, libro.año, libro.descripcion, True)
    
    @staticmethod
    def editar_libro(libro: Libro) -> bool:
        sql = "UPDATE Libro SET nombre = ?, autor = ?, anio = ?, descripcion = ?, libre = ? WHERE id = ?"
        try:
            cursor.execute(sql, (libro.nombre, libro.autor, libro.año, libro.descripcion, libro.libre, libro.id))
        except:
            return False
        return True

    @staticmethod
    def eliminar_libro(id: int) -> bool:
        sql = "DELETE FROM Libro WHERE id = ?"
        try:
            cursor.execute(sql, (id,))
        except:
            return False
        return True

