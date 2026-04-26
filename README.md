# Biblioteca - Proyecto de Estructuras de Datos

## Descripción General

Este proyecto es una aplicación de gestión de biblioteca desarrollada como parte de la asignatura de Estructuras de Datos en la Fundación Universitaria Iberoamericana, carrera de Ingeniería de Software. El objetivo principal es aplicar conceptos de estructuras de datos lineales, específicamente arreglos, para la administración de libros y usuarios.

## Integrantes del Grupo
- **Andrés Camilo Pérez Valderrama**
- **Diego Mauricio Ortiz Sánchez**
- **Juan Pablo Carrillo Chavez**

## Características Principales
- Registro y autenticación de usuarios.
- Visualización, creación, edición y eliminación de libros.
- Gestión de usuarios mediante base de datos SQLite.
- Gestión de libros mediante un árbol optimizado para búsquedas por nombre.
- Gestión de usuarios mediante base de datos SQLite.
- Gestión de préstamos y devoluciones de libros.
- Interfaz gráfica moderna y amigable (CustomTkinter).
- Script de inicialización de base de datos y datos de prueba (`seeder.py`).

## Estructura de Archivos

```
├── app.py                  # Archivo principal de la aplicación, coordina las vistas
├── main.py                 # Punto de entrada principal del sistema
├── requirements.txt        # Dependencias del proyecto
├── assets/                 # Recursos estáticos (imágenes, íconos, etc.)
├── lib/
│   ├── biblioteca.py       # Lógica principal de la biblioteca (gestión de libros y usuarios)
│   ├── config.py           # Configuración general del sistema
│   └── imagenes.py         # Gestión de imágenes
├── views/
│   ├── crear_libro.py      # Vista para crear libros
│   ├── detalles_libro.py   # Vista de detalles de un libro
│   ├── dialogs.py          # Diálogos y ventanas emergentes
│   ├── editar_libro.py     # Vista para editar libros
│   ├── ingreso.py          # Vista de inicio de sesión
│   ├── registro.py         # Vista de registro de usuarios
│   ├── ver_libros.py       # Vista para listar libros
│   ├── ver_usuarios.py     # Vista para listar usuarios
│   └── view.py             # Clase base para todas las vistas
```

## Instalación y Ejecución

1. **Clonar el repositorio**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Biblioteca-Ibero
   ```
2. **Crear y activar un entorno virtual (opcional pero recomendado)**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   source .venv/bin/activate  # En Linux/Mac
   ```
3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicializar la base de datos y cargar datos de prueba**
   ```bash
   python seeder.py
   ```
   Esto creará las tablas necesarias y cargará usuarios y libros de ejemplo.

5. **Ejecutar la aplicación**
   ```bash
   python main.py
   ```

## Datos de Prueba

### Usuarios de Prueba
- **admin** / **admin** (Administrador)
- **Diego** / **diego123**
- **Andres** / **andres123**
- **Juan** / **juan123**

### Libros de Prueba
Algunos de los libros precargados:
- "Cien años de soledad" - Gabriel García Márquez
- "Don Quijote de la Mancha" - Miguel de Cervantes
- "Orgullo y prejuicio" - Jane Austen
- "Moby Dick" - Herman Melville
- "Crimen y castigo" - Fiódor Dostoyevski
- "1984" - George Orwell
- "El Hobbit" - J.R.R. Tolkien
- "El señor de los anillos" - J.R.R. Tolkien
- "Harry Potter y la piedra filosofal" - J.K. Rowling
- ...y muchos más

Estos usuarios y libros están precargados para facilitar las pruebas y la exploración de la aplicación.

## Notas Técnicas
- El proyecto utiliza una estructura de **árbol** para almacenar y buscar libros de forma eficiente por nombre, y una base de datos SQLite local (`db/db.sqlite`) para gestionar la información de usuarios, libros y préstamos.
- El script `seeder.py` permite reiniciar la base de datos y cargar datos de prueba fácilmente.
- El código está organizado en módulos para separar la lógica, la configuración y las vistas.

## Licencia
Fundación Universitaria Iberoamericana - Ingeniería de Software
