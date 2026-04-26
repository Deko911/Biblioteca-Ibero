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
    LibroInput("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Relata las aventuras de Alonso Quijano, un hidalgo que pierde la cordura por leer novelas de caballería y decide convertirse en caballero andante. Acompañado por su fiel escudero Sancho Panza, enfrenta molinos de viento creyendo que son gigantes, en una obra que mezcla humor, crítica social y reflexión sobre la realidad y la imaginación."),
    LibroInput("Orgullo y prejuicio", "Jane Austen", 1813, "Narra la relación entre Elizabeth Bennet y el señor Darcy en una sociedad inglesa marcada por las normas sociales y el matrimonio. A través de malentendidos y prejuicios, la novela explora temas como el amor, la clase social y el crecimiento personal."),
    LibroInput("Moby Dick", "Herman Melville", 1851, "Cuenta la historia del capitán Ahab y su obsesión por cazar a la gran ballena blanca Moby Dick. Narrada por Ismael, la novela combina aventura marítima con profundas reflexiones filosóficas sobre el destino, la naturaleza y la obsesión humana."),
    LibroInput("Crimen y castigo", "Fiódor Dostoyevski", 1866, "Sigue a Raskólnikov, un estudiante que comete un asesinato creyendo estar moralmente justificado. La obra explora su conflicto psicológico, la culpa y la redención, profundizando en la mente humana y la moralidad."),
    LibroInput("1984", "George Orwell", 1949, "Describe una sociedad totalitaria donde el gobierno controla todos los aspectos de la vida mediante vigilancia constante y manipulación de la verdad. A través de Winston Smith, la novela muestra la lucha individual contra la opresión y la pérdida de libertad."),
    LibroInput("Cien años de soledad", "Gabriel García Márquez", 1967, "Relata la historia de la familia Buendía a lo largo de varias generaciones en el pueblo ficticio de Macondo. Combina lo real con lo fantástico en un estilo de realismo mágico, explorando el tiempo, la soledad y el destino."),
    LibroInput("Fahrenheit 451", "Ray Bradbury", 1953, "Ambientada en un futuro donde los libros están prohibidos, sigue a Guy Montag, un bombero cuya labor es quemarlos. A medida que cuestiona su papel, descubre el valor del conocimiento y la libertad de pensamiento."),
    LibroInput("El Hobbit", "J.R.R. Tolkien", 1937, "Narra la aventura de Bilbo Bolsón, un hobbit que es reclutado por un grupo de enanos para recuperar su tesoro de un dragón. En el viaje, Bilbo descubre su valentía y astucia en un mundo lleno de criaturas fantásticas."),
    LibroInput("El señor de los anillos", "J.R.R. Tolkien", 1954, "Sigue la misión de Frodo Bolsón para destruir un anillo con poder maligno. Acompañado por aliados de distintas razas, enfrenta fuerzas oscuras en una épica lucha entre el bien y el mal en la Tierra Media."),
    LibroInput("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Cuenta la historia de Harry Potter, un niño huérfano que descubre que es mago y comienza su educación en Hogwarts. Allí enfrenta misterios y descubre su conexión con un oscuro enemigo."),
    LibroInput("El código Da Vinci", "Dan Brown", 2003, "Un thriller que sigue a Robert Langdon mientras investiga un asesinato en el Louvre. La historia combina arte, historia y conspiraciones sobre secretos ocultos en la Iglesia."),
    LibroInput("Los juegos del hambre", "Suzanne Collins", 2008, "En un futuro distópico, Katniss Everdeen se ofrece como voluntaria para participar en un evento televisado donde jóvenes deben luchar hasta la muerte. La novela explora la supervivencia, el poder y la rebelión."),
    LibroInput("Dune", "Frank Herbert", 1965, "Ambientada en un planeta desértico, sigue a Paul Atreides en un conflicto político y ecológico por el control de la especia, el recurso más valioso del universo. Combina ciencia ficción con filosofía y política."),
    LibroInput("Fundación", "Isaac Asimov", 1951, "Describe la caída de un imperio galáctico y los esfuerzos de un grupo de científicos para preservar el conocimiento humano. Introduce conceptos como la psicohistoria y la predicción del futuro social."),
    LibroInput("El nombre de la rosa", "Umberto Eco", 1980, "Ambientada en una abadía medieval, sigue a un monje que investiga una serie de misteriosos asesinatos. Combina elementos de novela policial con filosofía, religión y simbolismo."),
    LibroInput("La sombra del viento", "Carlos Ruiz Zafón", 2001, "Un joven descubre un libro olvidado que lo lleva a investigar la vida de su autor. Ambientada en Barcelona, la historia mezcla misterio, romance y amor por la literatura."),
    LibroInput("El perfume", "Patrick Süskind", 1985, "Cuenta la vida de un hombre con un sentido del olfato extraordinario que desarrolla una obsesión por crear el perfume perfecto. Su búsqueda lo lleva a cometer actos extremos."),
    LibroInput("El principito", "Antoine de Saint-Exupéry", 1943, "A través de un relato aparentemente infantil, explora temas profundos como la amistad, el amor y el sentido de la vida. Narra el encuentro entre un aviador y un pequeño príncipe de otro planeta."),
    LibroInput("La carretera", "Cormac McCarthy", 2006, "Relata el viaje de un padre y su hijo a través de un mundo devastado tras un evento apocalíptico. La historia destaca la relación entre ambos y la lucha por sobrevivir en condiciones extremas."),
    LibroInput("El cuento de la criada", "Margaret Atwood", 1985, "Presenta una sociedad teocrática donde las mujeres han perdido sus derechos. A través de la protagonista, muestra la opresión, la resistencia y el control social."),
    LibroInput("Neuromante", "William Gibson", 1984, "Sigue a un hacker en un mundo dominado por corporaciones y tecnología avanzada. Es una obra clave del ciberpunk que explora la inteligencia artificial y la realidad virtual."),
    LibroInput("Ready Player One", "Ernest Cline", 2011, "En un futuro donde la gente escapa a un mundo virtual, un joven participa en una competencia global para encontrar un tesoro oculto. Combina cultura pop con aventura tecnológica."),
    LibroInput("La ladrona de libros", "Markus Zusak", 2005, "Narrada por la Muerte, cuenta la vida de una niña en la Alemania nazi que encuentra consuelo robando libros. Explora la guerra, la pérdida y el poder de las palabras."),
    LibroInput("American Gods", "Neil Gaiman", 2001, "Un exconvicto se ve envuelto en un conflicto entre dioses antiguos y modernos en Estados Unidos. La novela mezcla mitología, fantasía y crítica cultural."),
    LibroInput("Coraline", "Neil Gaiman", 2002, "Una niña descubre un mundo alternativo detrás de una puerta secreta en su casa. Aunque al principio parece perfecto, pronto revela un lado oscuro y peligroso."),
    LibroInput("El silencio de los inocentes", "Thomas Harris", 1988, "La agente del FBI Clarice Starling busca la ayuda del brillante pero peligroso Hannibal Lecter para capturar a un asesino en serie. La historia combina tensión psicológica, investigación criminal y un inquietante juego mental entre ambos personajes."),
    LibroInput("El psicoanalista", "John Katzenbach", 2002, "Un reconocido psicoanalista recibe una amenaza que lo obliga a descubrir la identidad de un misterioso enemigo. Si falla, perderá todo lo que ama. La novela desarrolla un intenso thriller psicológico lleno de giros inesperados."),
    LibroInput("La chica del tren", "Paula Hawkins", 2015, "Rachel observa cada día a una pareja desde el tren hasta que un día la mujer desaparece. A partir de entonces, se ve involucrada en un misterio donde nada es lo que parece y su memoria resulta poco confiable."),
    LibroInput("Perdida", "Gillian Flynn", 2012, "Cuando Amy desaparece en su aniversario de bodas, todas las sospechas recaen sobre su esposo. La historia alterna perspectivas para revelar secretos, mentiras y manipulaciones en una relación aparentemente perfecta."),
    LibroInput("El club de la pelea", "Chuck Palahniuk", 1996, "Un hombre insatisfecho con su vida conoce a Tyler Durden, con quien crea un club clandestino donde los hombres luchan para liberar sus frustraciones. La novela cuestiona la identidad, el consumismo y la masculinidad moderna."),
    LibroInput("La vida de Pi", "Yann Martel", 2001, "Un joven sobrevive a un naufragio y queda a la deriva en un bote junto a un tigre. La historia mezcla aventura, supervivencia y reflexiones sobre la fe y la percepción de la realidad."),
    LibroInput("El curioso incidente del perro a medianoche", "Mark Haddon", 2003, "Un joven con una mente excepcional decide investigar la muerte de un perro. Su búsqueda lo lleva a descubrir secretos familiares y enfrentar sus propios límites."),
    LibroInput("La elegancia del erizo", "Muriel Barbery", 2006, "En un edificio parisino, una portera culta y una niña brillante esconden sus verdaderas identidades. La novela reflexiona sobre la apariencia, la inteligencia y el sentido de la vida."),
    LibroInput("El médico", "Noah Gordon", 1986, "Sigue la vida de un joven que viaja desde Inglaterra hasta Persia para aprender medicina en la Edad Media. La historia combina aventura, conocimiento y el choque de culturas."),
    LibroInput("Shantaram", "Gregory David Roberts", 2003, "Un fugitivo australiano se refugia en Bombay, donde construye una nueva vida en los bajos fondos. La novela mezcla crimen, amor y búsqueda espiritual en un entorno vibrante."),
    LibroInput("El jardín secreto", "Frances Hodgson Burnett", 1911, "Una niña huérfana descubre un jardín abandonado que transforma su vida y la de quienes la rodean. Es una historia sobre crecimiento personal, naturaleza y sanación."),
    LibroInput("Mujercitas", "Louisa May Alcott", 1868, "Sigue la vida de cuatro hermanas durante la guerra civil estadounidense, explorando sus sueños, dificultades y crecimiento personal."),
    LibroInput("El llamado de la selva", "Jack London", 1903, "Un perro doméstico es llevado al salvaje norte y aprende a sobrevivir en condiciones extremas. La historia muestra la lucha entre civilización e instinto."),
    LibroInput("Colmillo blanco", "Jack London", 1906, "Relata la vida de un lobo que aprende a convivir con humanos. La novela explora la naturaleza, la violencia y la domesticación."),
    LibroInput("El tiempo entre costuras", "María Dueñas", 2009, "Una joven modista se ve envuelta en el espionaje durante la Guerra Civil española. Combina historia, romance y política."),
    LibroInput("El mapa del tiempo", "Félix J. Palma", 2008, "Una mezcla de ciencia ficción y literatura victoriana donde los viajes en el tiempo cambian el destino de varios personajes."),
    LibroInput("La casa holandesa", "Ann Patchett", 2019, "Dos hermanos crecen marcados por la pérdida de su hogar familiar. La historia explora la memoria, la familia y el paso del tiempo."),
    LibroInput("El priorato del naranjo", "Samantha Shannon", 2019, "Una fantasía épica con dragones, reinos enfrentados y una antigua amenaza que resurge. Destaca por sus personajes complejos y su mundo detallado."),
    LibroInput("Circe", "Madeline Miller", 2018, "Reinterpreta la historia de la hechicera Circe desde la mitología griega, mostrando su evolución y lucha por encontrar su lugar en el mundo."),
    LibroInput("La canción de Aquiles", "Madeline Miller", 2011, "Relata la historia de Aquiles y Patroclo, explorando su relación en medio de la guerra de Troya con un enfoque humano y emocional."),
    LibroInput("Proyecto Hail Mary", "Andy Weir", 2021, "Un astronauta despierta sin memoria en una misión para salvar a la humanidad. A medida que recupera recuerdos, enfrenta desafíos científicos y decisiones críticas."),
    LibroInput("El problema de los tres cuerpos", "Liu Cixin", 2006, "La humanidad entra en contacto con una civilización alienígena. La novela combina ciencia, política y filosofía en un complejo primer contacto."),
    LibroInput("La quinta estación", "N.K. Jemisin", 2015, "En un mundo inestable, ciertas personas pueden controlar la energía de la tierra. La historia aborda temas de opresión, supervivencia y poder."),
    LibroInput("El archivo de las tormentas", "Brandon Sanderson", 2010, "Una saga épica en un mundo azotado por tormentas donde varios personajes luchan por el destino de su civilización."),
    LibroInput("Mistborn: El imperio final", "Brandon Sanderson", 2006, "En un mundo dominado por un tirano inmortal, un grupo planea una revolución utilizando poderes mágicos únicos."),
    LibroInput("Elantris", "Brandon Sanderson", 2005, "Una ciudad mágica cae en desgracia y sus habitantes quedan atrapados en una maldición. La historia combina política, religión y redención."),
    LibroInput("El juego de Ender", "Orson Scott Card", 1985, "Un niño prodigio es entrenado para liderar la defensa de la humanidad contra una amenaza alienígena."),
    LibroInput("Snow Crash", "Neal Stephenson", 1992, "En un futuro dominado por corporaciones, un hacker investiga un virus que afecta tanto al mundo digital como al real."),
    LibroInput("Criptonomicon", "Neal Stephenson", 1999, "Alterna entre la Segunda Guerra Mundial y la era moderna, explorando criptografía, tecnología y conspiraciones."),
    LibroInput("El hombre en el castillo", "Philip K. Dick", 1962, "Imagina un mundo donde las potencias del Eje ganaron la Segunda Guerra Mundial, explorando realidades alternativas."),
    LibroInput("¿Sueñan los androides con ovejas eléctricas?", "Philip K. Dick", 1968, "Un cazador de androides cuestiona qué significa ser humano en un mundo postapocalíptico."),
    LibroInput("La larga marcha", "Stephen King", 1979, "Un grupo de jóvenes participa en una competencia donde deben caminar sin detenerse, enfrentando el agotamiento y la muerte."),
    LibroInput("El instituto", "Stephen King", 2019, "Niños con habilidades especiales son secuestrados para experimentos secretos. Uno de ellos planea escapar."),
    LibroInput("Doctor Sueño", "Stephen King", 2013, "Secuela de El resplandor, sigue a Danny Torrance enfrentando nuevos peligros relacionados con sus poderes."),
    LibroInput("El visitante", "Stephen King", 2018, "Un crimen brutal lleva a una investigación que revela elementos sobrenaturales inquietantes."),
    LibroInput("La milla verde", "Stephen King", 1996, "Un guardia de prisión conoce a un recluso con poderes extraordinarios. La historia mezcla drama, injusticia y lo sobrenatural."),
    LibroInput("La catedral del mar", "Ildefonso Falcones", 2006, "Ambientada en la Barcelona medieval, sigue la vida de un hombre mientras se construye una gran catedral."),
    LibroInput("El infinito en un junco", "Irene Vallejo", 2019, "Ensayo sobre la historia de los libros y su importancia en la cultura humana."),
    LibroInput("Sapiens", "Yuval Noah Harari", 2011, "Recorre la historia de la humanidad desde sus orígenes hasta la actualidad, analizando cómo evolucionaron las sociedades."),
    LibroInput("Homo Deus", "Yuval Noah Harari", 2015, "Explora el futuro de la humanidad y los posibles avances tecnológicos que cambiarán nuestra existencia."),
    LibroInput("Hábitos atómicos", "James Clear", 2018, "Explica cómo pequeños cambios diarios pueden generar grandes resultados en la vida personal y profesional."),
    LibroInput("El poder del ahora", "Eckhart Tolle", 1997, "Propone vivir en el presente como clave para alcanzar la paz interior y la realización personal."),
    LibroInput("Padre rico, padre pobre", "Robert Kiyosaki", 1997, "Ofrece lecciones sobre educación financiera y cómo cambiar la mentalidad respecto al dinero."),
    LibroInput("Los 7 hábitos de la gente altamente efectiva", "Stephen Covey", 1989, "Presenta principios para mejorar la efectividad personal y profesional."),
    LibroInput("Cómo ganar amigos e influir sobre las personas", "Dale Carnegie", 1936, "Guía clásica sobre habilidades sociales y comunicación efectiva."),
    LibroInput("El arte de la guerra", "Sun Tzu", -500, "Antiguo tratado militar que ofrece estrategias aplicables a conflictos, negocios y liderazgo."),
    LibroInput("Meditaciones", "Marco Aurelio", 180, "Reflexiones personales del emperador romano sobre la vida, la disciplina y la filosofía estoica.")
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