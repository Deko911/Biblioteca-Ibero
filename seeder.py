from db.db import cursor
from models.usuarios import UsuarioModel
from models.libros import LibroModel
from models.prestamos import PrestamoModel
from lib.biblioteca import UsuarioInput, LibroInput

usuarios = [
    UsuarioInput("admin", "admin"),
    UsuarioInput("Diego", "diego123"),
    UsuarioInput('Andres', 'andres123'),
    UsuarioInput('Juan', 'juan123')
]

libros = [
    LibroInput("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Historia de un hidalgo que enloquece por leer libros de caballería"),
    LibroInput("Orgullo y prejuicio", "Jane Austen", 1813, "Romance y crítica social en la Inglaterra del siglo XIX"),
    LibroInput("Moby Dick", "Herman Melville", 1851, "Un capitán obsesionado con cazar una ballena blanca"),
    LibroInput("Crimen y castigo", "Fiódor Dostoyevski", 1866, "Un joven comete un asesinato y enfrenta su culpa"),
    LibroInput("Madame Bovary", "Gustave Flaubert", 1856, "La vida de una mujer insatisfecha en la sociedad burguesa"),
    LibroInput("La Odisea", "Homero", -800, "Viaje épico de regreso a casa tras la guerra de Troya"),
    LibroInput("Hamlet", "William Shakespeare", 1603, "Drama sobre la venganza de un príncipe danés"),
    LibroInput("El Gran Gatsby", "F. Scott Fitzgerald", 1925, "Crítica al sueño americano en los años 20"),
    LibroInput("1984", "George Orwell", 1949, "Distopía sobre un régimen totalitario vigilante"),
    LibroInput("Rebelión en la granja", "George Orwell", 1945, "Sátira política con animales en una granja"),
    LibroInput("Cien años de soledad", "Gabriel García Márquez", 1967, "Historia de la familia Buendía en Macondo"),
    LibroInput("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "Historia de amor que perdura décadas"),
    LibroInput("La metamorfosis", "Franz Kafka", 1915, "Un hombre despierta convertido en insecto"),
    LibroInput("El proceso", "Franz Kafka", 1925, "Un hombre es arrestado sin saber por qué"),
    LibroInput("Fahrenheit 451", "Ray Bradbury", 1953, "Un futuro donde los libros están prohibidos"),
    LibroInput("Un mundo feliz", "Aldous Huxley", 1932, "Sociedad futurista basada en el control y el placer"),
    LibroInput("Drácula", "Bram Stoker", 1897, "Historia clásica de vampiros"),
    LibroInput("Frankenstein", "Mary Shelley", 1818, "Un científico crea vida artificial"),
    LibroInput("El retrato de Dorian Gray", "Oscar Wilde", 1890, "Un hombre no envejece mientras su retrato sí"),
    LibroInput("Los miserables", "Victor Hugo", 1862, "Lucha social y redención en Francia"),
    LibroInput("La Iliada", "Homero", -750, "Relato épico de la guerra de Troya"),
    LibroInput("Anna Karenina", "León Tolstói", 1877, "Drama romántico en la aristocracia rusa"),
    LibroInput("Guerra y paz", "León Tolstói", 1869, "Historia de Rusia durante las guerras napoleónicas"),
    LibroInput("El señor de los anillos", "J.R.R. Tolkien", 1954, "Fantasía épica sobre la lucha contra el mal"),
    LibroInput("El Hobbit", "J.R.R. Tolkien", 1937, "Aventura de un hobbit en busca de tesoros"),
    LibroInput("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Un niño descubre que es mago"),
    LibroInput("Juego de tronos", "George R.R. Martin", 1996, "Lucha por el poder en un mundo medieval ficticio"),
    LibroInput("El código Da Vinci", "Dan Brown", 2003, "Misterio sobre sociedades secretas y arte"),
    LibroInput("Los juegos del hambre", "Suzanne Collins", 2008, "Distopía donde jóvenes luchan por sobrevivir"),
    LibroInput("Crepúsculo", "Stephenie Meyer", 2005, "Romance entre humana y vampiro"),
    LibroInput("It", "Stephen King", 1986, "Un grupo enfrenta a una entidad maligna"),
    LibroInput("El resplandor", "Stephen King", 1977, "Terror en un hotel aislado"),
    LibroInput("Carrie", "Stephen King", 1974, "Una adolescente con poderes telequinéticos"),
    LibroInput("La carretera", "Cormac McCarthy", 2006, "Viaje de padre e hijo en un mundo postapocalíptico"),
    LibroInput("Ensayo sobre la ceguera", "José Saramago", 1995, "Epidemia de ceguera afecta a la sociedad"),
    LibroInput("El alquimista", "Paulo Coelho", 1988, "Un joven busca su destino personal"),
    LibroInput("El principito", "Antoine de Saint-Exupéry", 1943, "Fábula sobre la vida y la amistad"),
    LibroInput("El nombre de la rosa", "Umberto Eco", 1980, "Misterio en una abadía medieval"),
    LibroInput("La sombra del viento", "Carlos Ruiz Zafón", 2001, "Misterio literario en Barcelona"),
    LibroInput("Rayuela", "Julio Cortázar", 1963, "Novela experimental sobre el amor y la vida"),
    LibroInput("Pedro Páramo", "Juan Rulfo", 1955, "Historia de un pueblo lleno de fantasmas"),
    LibroInput("La tregua", "Mario Benedetti", 1960, "Diario de un amor tardío"),
    LibroInput("El túnel", "Ernesto Sabato", 1948, "Obsesión y crimen en Buenos Aires"),
    LibroInput("Sobre héroes y tumbas", "Ernesto Sabato", 1961, "Exploración de la sociedad argentina"),
    LibroInput("La casa de los espíritus", "Isabel Allende", 1982, "Saga familiar con realismo mágico"),
    LibroInput("Paula", "Isabel Allende", 1994, "Memorias personales de una madre"),
    LibroInput("El perfume", "Patrick Süskind", 1985, "Un asesino obsesionado con los olores"),
    LibroInput("Lolita", "Vladimir Nabokov", 1955, "Relación polémica entre adulto y menor"),
    LibroInput("Ulises", "James Joyce", 1922, "Un día en la vida de un hombre en Dublín"),
    LibroInput("Retrato del artista adolescente", "James Joyce", 1916, "Crecimiento personal de un joven"),
    LibroInput("El guardián entre el centeno", "J.D. Salinger", 1951, "Rebeldía juvenil"),
    LibroInput("Las uvas de la ira", "John Steinbeck", 1939, "Familia migrante en la Gran Depresión"),
    LibroInput("De ratones y hombres", "John Steinbeck", 1937, "Amistad entre trabajadores agrícolas"),
    LibroInput("La divina comedia", "Dante Alighieri", 1320, "Viaje por el infierno, purgatorio y cielo"),
    LibroInput("El conde de Montecristo", "Alexandre Dumas", 1844, "Venganza tras una injusta prisión"),
    LibroInput("Los tres mosqueteros", "Alexandre Dumas", 1844, "Aventuras de espadachines en Francia"),
    LibroInput("Viaje al centro de la Tierra", "Jules Verne", 1864, "Aventura científica bajo la tierra"),
    LibroInput("Veinte mil leguas de viaje submarino", "Jules Verne", 1870, "Exploración en submarino"),
    LibroInput("La isla misteriosa", "Jules Verne", 1874, "Supervivencia en una isla"),
    LibroInput("El viejo y el mar", "Ernest Hemingway", 1952, "Un pescador lucha contra un pez gigante"),
    LibroInput("Por quién doblan las campanas", "Ernest Hemingway", 1940, "Guerra civil española"),
    LibroInput("El extranjero", "Albert Camus", 1942, "Indiferencia y absurdo existencial"),
    LibroInput("La peste", "Albert Camus", 1947, "Epidemia en una ciudad"),
    LibroInput("La náusea", "Jean-Paul Sartre", 1938, "Reflexión existencial"),
    LibroInput("El lobo estepario", "Hermann Hesse", 1927, "Crisis de identidad"),
    LibroInput("Siddhartha", "Hermann Hesse", 1922, "Búsqueda espiritual"),
    LibroInput("Demian", "Hermann Hesse", 1919, "Formación espiritual de un joven"),
    LibroInput("La insoportable levedad del ser", "Milan Kundera", 1984, "Relaciones y filosofía"),
    LibroInput("El Aleph", "Jorge Luis Borges", 1949, "Relatos sobre infinito y conocimiento"),
    LibroInput("Ficciones", "Jorge Luis Borges", 1944, "Cuentos filosóficos"),
    LibroInput("La ciudad y los perros", "Mario Vargas Llosa", 1963, "Juventud en academia militar"),
    LibroInput("La fiesta del chivo", "Mario Vargas Llosa", 2000, "Dictadura dominicana"),
    LibroInput("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981, "Asesinato anunciado"),
    LibroInput("La ladrona de libros", "Markus Zusak", 2005, "Narrada por la muerte en la Alemania nazi"),
    LibroInput("Los pilares de la tierra", "Ken Follett", 1989, "Construcción de una catedral"),
    LibroInput("Ready Player One", "Ernest Cline", 2011, "Aventura en realidad virtual"),
    LibroInput("Dune", "Frank Herbert", 1965, "Conflictos políticos en planeta desértico"),
    LibroInput("Neuromante", "William Gibson", 1984, "Origen del ciberpunk"),
    LibroInput("Fundación", "Isaac Asimov", 1951, "Imperio galáctico y ciencia"),
    LibroInput("Yo, robot", "Isaac Asimov", 1950, "Relatos sobre inteligencia artificial"),
    LibroInput("Solaris", "Stanislaw Lem", 1961, "Planeta inteligente"),
    LibroInput("La naranja mecánica", "Anthony Burgess", 1962, "Violencia juvenil en sociedad futurista"),
    LibroInput("El marciano", "Andy Weir", 2011, "Supervivencia en Marte"),
    LibroInput("El cuento de la criada", "Margaret Atwood", 1985, "Distopía sobre control social"),
    LibroInput("American Gods", "Neil Gaiman", 2001, "Mitología en el mundo moderno"),
    LibroInput("Coraline", "Neil Gaiman", 2002, "Aventura fantástica infantil")
]

prestamos = [
    (0, 0),
    (1, 1),
    (2, 2)
]

def seeder():
    # Crear/Reiniciar Tablas
    f = open('./tables.sql', 'r')
    script = f.read()
    cursor.executescript(script)
    
    # Crear Usuarios
    for usuario in usuarios:
        UsuarioModel.crear_usuario(usuario)
        
    # Crear Libros
    for libro in libros:
        LibroModel.crear_libro(libro)
        
    # Obtener todos los Usuarios    
    getUsuarios = UsuarioModel.obtener_usuarios()
    assert getUsuarios
    
    for usuario in getUsuarios:
        print(usuario.nombre)
        
    print("".center(30, "-"))
        
    # Obtener todos los Libros   
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro)

    print("".center(30, "-"))
        
    ##### PRUEBAS #####
    """ 
        
    # Obtener Usuario por nombre
    usuario_admin = UsuarioModel.obtener_usuario_por_nombre("admin")
    assert usuario_admin 
    
    print(usuario_admin.nombre)
    print("".center(30, "-"))
    
    usuario_no_existente = UsuarioModel.obtener_usuario_por_nombre("Jaime")
    assert not usuario_no_existente 

    # Editar Libro
        
    primerLibro = getLibros[0]
    primerLibro.libre = False
    
    LibroModel.editar_libro(primerLibro)
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    print("".center(30, "-"))
    
    # Eliminar Libro
    
    LibroModel.eliminar_libro(primerLibro.id)
    
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    print("".center(30, "-"))
    
    # Hacer prestamos
    for (usuario_id, libro_id) in prestamos:
        assert PrestamoModel.prestar_libro(getUsuarios[usuario_id], getLibros[libro_id])
    
    getLibros = LibroModel.obtener_libros()
    assert getLibros
    
    for libro in getLibros:
        print(libro.id, libro.nombre, libro.autor, libro.año, libro.libre)
        
    #Obtener Prestamos
    getPrestamos = PrestamoModel.obtener_prestamos()
    assert getPrestamos
    
    print(getPrestamos) """

if __name__ == "__main__":
    seeder()