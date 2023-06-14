# MichiStore

MichiStore es un proyecto de Django que consiste en un ecommerce para la venta de productos para gatos.

## Requisitos previos

- Python 3.x
- Django 4.2.1

## Administrador

El proyecto incluye un administrador al que se puede acceder con un superusuario. Las credenciales de inicio de sesión son:

- Nombre de usuario: nawsp
- Contraseña: 1234

## Estructura del proyecto

El proyecto se encuentra en la carpeta "michiStore" y consta de una aplicación llamada "AppTienda" donde se encuentran los templates.

### Archivos en la carpeta "michiStore"

- **manage.py**: Archivo principal para ejecutar tareas administrativas de Django.

### Archivos en la carpeta "michiStore/michiStore"

- **urls.py**: Archivo de configuración de URL para el proyecto michiStore

### Archivos en la carpeta "michiStore/AppTienda"

- **views.py**: Contiene las vistas (funciones) que controlan el comportamiento de las páginas web.

- **urls.py**: Archivo de configuración de URL para la aplicación AppTienda.

- **models.py**: Define los modelos de la aplicación, incluyendo las clases Cliente, Producto y Pedido.

- **admin.py**: Archivo de configuración del administrador de Django.

### Archivos en la carpeta "michiStore/AppTienda/templates/michiStore"

- **base.html**: Plantilla base que define la estructura común de todas las páginas.

- **index.html**: Plantilla para la página de inicio.

- **nosotros.html**: Plantilla para la página "Nosotros".

## Configuración

El archivo de configuración principal del proyecto se encuentra en "michiStore/michiStore/settings.py". Aquí se encuentran las siguientes configuraciones destacadas:

- **SECRET_KEY**: Clave secreta utilizada por Django para la seguridad del proyecto.

- **DEBUG**: Indica si el modo de depuración está habilitado o deshabilitado.

- **ALLOWED_HOSTS**: Lista de hosts permitidos para el proyecto.

- **INSTALLED_APPS**: Lista de aplicaciones instaladas en el proyecto, incluyendo 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles' y 'AppTienda'.

- **TEMPLATES**: Configuración de las plantillas, incluyendo la ubicación de los directorios de plantillas.

- **DATABASES**: Configuración de la base de datos, en este caso se está utilizando SQLite.

- **STATIC_URL**: URL base para los archivos estáticos.

## Ejecución del proyecto

Para ejecutar el proyecto, asegúrate de tener Django instalado y sigue estos pasos:

1. Abre una terminal en la carpeta raíz del proyecto (donde se encuentra el archivo manage.py).

2. Ejecuta el siguiente comando para aplicar las migraciones de la base de datos:

### `python manage.py migrate`

3. Luego, ejecuta el siguiente comando para iniciar el servidor de desarrollo:

### `python manage.py runserver`

4. Abre un navegador web y visita la siguiente URL para acceder al sitio:

### `http://localhost:8000/`

¡Listo! Ahora puedes explorar el ecommerce de MichiStore y realizar pruebas en el entorno de desarrollo.

## Contribuciones

Este proyecto está en proceso de desarrollo y se aceptan contribuciones o sugerencias para mejorar. Si deseas contribuir, no dudes en abrir un problema en el repositorio de GitHub del proyecto o en comunicarte por estos medios:

### Contacto

Información de contacto:

`Burrut Yasmin Lara`

[Linkedin](https://www.linkedin.com/in/burrutyasmin/)

[Github](https://github.com/Nawsper)

nawsper@gmail.com
