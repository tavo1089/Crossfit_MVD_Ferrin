# MVD CrossFit - Sistema de Gestión

> Aplicación web completa para la administración de un box de CrossFit en Montevideo, desarrollada con Django 5 y Bootstrap 5.

**🌐 Sitio en vivo**: [https://tavo10.pythonanywhere.com/](https://tavo10.pythonanywhere.com/)

## Descripción

Sistema integral de gestión para gimnasios de CrossFit que permite administrar socios, coaches, clases y facilita la comunicación entre miembros. Incluye un sistema completo de autenticación, perfiles personalizables, mensajería interna y panel administrativo.

## Funcionalidades Principales

### **Gestión de Usuarios**
- Registro y autenticación de usuarios
- Perfiles personalizables con foto y biografía
- Sistema de roles (socios, coaches, administradores)

### **Gestión del Gimnasio**
- Administración de socios y coaches
- Gestión de clases y horarios
- Búsqueda avanzada de socios
- Sistema de reservas

### **Comunicación**
- Mensajería interna entre usuarios
- Sistema de notificaciones
- Blog/páginas informativas con CKEditor

### **Interfaz y UX**
- Diseño responsive con Bootstrap 5
- Validación de formularios en tiempo real
- Iconos para mostrar/ocultar contraseñas
- Alertas profesionales y mensajes de error
- Navegación intuitiva con hamburger menu

## Tecnologías Utilizadas

- **Backend**: Python 3.11+ | Django 5.2.7
- **Frontend**: HTML5 | CSS3 | Bootstrap 5 | JavaScript
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Editor**: CKEditor para contenido rich text
- **Autenticación**: Sistema Django integrado
- **Deployment**: PythonAnywhere

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/tavo1089/Crossfit_MVD_Ferrin.git
cd Crossfit_MVD_Ferrin
```

### 2. Crear entorno virtual
```bash
python -m venv entorno_virtual
# Windows
entorno_virtual\Scripts\activate
# Linux/Mac
source entorno_virtual/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://127.0.0.1:8000/`

## Demo del Proyecto

[![Video Demostrativo MVD CrossFit](https://img.youtube.com/vi/0FrxET5zf7c/maxresdefault.jpg)](https://youtu.be/0FrxET5zf7c)

**🎬 Video explicativo completo**: [Ver en YouTube](https://youtu.be/0FrxET5zf7c)

*Haz clic en la imagen o el enlace para ver el video demostrativo que muestra todas las funcionalidades del sistema*

## Características Destacadas

- **Seguridad**: Validación robusta de contraseñas y autenticación segura
- **Responsive**: Diseño adaptable a todos los dispositivos
- **Performance**: Carga rápida y optimizada
- **UX/UI**: Interfaz moderna y fácil de usar
- **Búsqueda**: Sistema de búsqueda avanzado
- **Comunicación**: Mensajería interna completa

## Estructura del Proyecto

```
MVD_Crossfit/
├── cuentas/          # Autenticación y usuarios
├── gimnasio/         # Gestión del gimnasio
├── mensajes/         # Sistema de mensajería
├── perfiles/         # Perfiles de usuario
├── paginas/          # Páginas y blog
├── static/           # Archivos estáticos
├── media/            # Archivos multimedia
└── templates/        # Plantillas HTML
```

## Deployment

El proyecto está desplegado en **PythonAnywhere**:
- URL de producción: [https://tavo10.pythonanywhere.com/](https://tavo10.pythonanywhere.com/)
- Configuración automática con Git
- Base de datos MySQL en producción

## Autor

**Gustavo Ferrín**
- GitHub: [@tavo1089](https://github.com/tavo1089)
- Proyecto: Trabajo Final - Curso Python/Django

## Licencia

Este proyecto fue desarrollado como proyecto final de curso y está disponible para fines educativos.

---

**¡Gracias por revisar mi proyecto!** Si te gusta, no olvides darle una estrella al repositorio.
