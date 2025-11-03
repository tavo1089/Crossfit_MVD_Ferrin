# Crossfit_MVD_Ferrin
Sistema de gestion del gimnasio 

# Crossfit_MVD_Ferrin

Proyecto Django para la gestión de un box de CrossFit en Montevideo.

## Descripción
Aplicación web que permite administrar socios, coaches y clases del gimnasio **MVD CrossFit**.  
Incluye formularios para registrar datos, búsqueda de socios y una interfaz minimalista con Bootstrap 5.

## Funcionalidades
- Herencia de plantillas (base.html)
- Modelos: Socio, Clase, Coach
- Formularios para crear registros
- Búsqueda de socios por apellido o email
- Panel de administración con superusuario

## Tecnologías
- Python 3  
- Django 5  
- Bootstrap 5  

## Cómo ejecutar el proyecto
1. Clonar el repositorio o descargar el proyecto.  
2. Instalar dependencias:

   # Proyecto Final Django - Crossfit MVD

   Este es mi primer proyecto web usando Python y Django. Es una página para un gimnasio tipo Crossfit, con usuarios, perfiles, blog, mensajería y administración.

   ## ¿Qué incluye?
   - Registro, login y logout de usuarios
   - Perfil editable con foto y biografía
   - Blog/páginas con CKEditor, imágenes y buscador
   - Mensajería entre usuarios
   - Panel de administración
   - Navbar con accesos a todas las secciones

   ## Instalación rápida
   1. Clona el repo
   2. Instala las dependencias:
      ```
      pip install -r requirements.txt
      ```
   3. Crea las migraciones y la base de datos:
      ```
      python manage.py makemigrations
      python manage.py migrate
      ```
   4. Crea un superusuario para el admin:
      ```
      python manage.py createsuperuser
      ```
   5. Corre el servidor:
      ```
      python manage.py runserver
      ```


   ## Video de mi proyecto
   A continuación dejo el video explicativo de mi proyecto:

   `[Enlace al video explicativo]`

   ## Notas
   - No subas el archivo `db.sqlite3` ni la carpeta `media/` al repo (ya está en el .gitignore)
   - Las imágenes de usuario se guardan en `media/`, las del código en `static/`
   - El proyecto usa herencia de templates y CBVs
   - Si tienes dudas, revisa el código o pregúntame

   ¡Gracias por revisar mi proyecto!
