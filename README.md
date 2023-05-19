
# Aplicacion Web Garden Store 🏠

# Detalle 📄
Esta es una aplicacion web fullstack llamado garden storecpara vender productos de jardinería. Esta creada con las tecnologias de Django con python y una base de datos relacional Mysql en el lado del backend, y en el lado del frontend esta creado con Angular

# Tecnologias ⚙️
- Python 3.10.9
- Django 4.1.4
- Rest Framework 3.14.0
- Base de Datos Relacional MySQL
- Angular 15
- HTML
- SASS
- TypeScript

# Instalación de Dependencias 📁

# Django ❇️
Para instalar las dependencias del proyecto de django, se adjunta un archivo llamado requirements.txt con todas las librerias necesarias. Pero primero, se debe crear un entorno virtual con Python usando el comando:

    python -m venv env 

Después de ejecutar el comando, se creará una carpeta con el entorno virtual. Para activar el entorno virtual, ejecute el archivo activate.bat ubicado en env\Scripts\activate.bat. Con el entorno virtual activado, instale las dependencias del proyecto usando el comando:

    pip install -r requirements.txt

Posteriormente se instalarán las dependencias para ejecutar el proyecto.

# Variables de Entorno 📌

Para poder crear las variables de entorno se necesita crear una archivo .env en la carpeta core/, adentro de este archivo se deben poner las siguientes variables de entorno:

```bash
NAME_DATABASE=<db-name>
USER_DATABASE=<username>
PASSWORD_DATABASE=<password>
HOST_DATABASE=localhost
PORT_DATABASE=3306
SECRET_KEY=<generate-secret-key>
DEBUG=<True|False>
```

# Migraciones 📝
Para migrar los modelos a la base de datos, primero se debe crear unas carpetas llamadas migrations/ en cada app del proyecto y un archivo __init__.py dentro de estas carpetas, configurar el archivo settings.py con los detalles de conexión de la base de datos (En las variables de entorno). Una vez que hayas hecho la configuración, ejecuta el comando:

    python manage.py makemigrations

Esto creará los archivos de migración. Luego, ejecute el comando:

    python manage.py migrate 

Esto ejecutará todas las migraciones y creará las tablas en la base de datos.

# Ejecución Django ☑️
Para ejecutar el proyecto, active el entorno virtual con las dependencias instaladas y luego ejecute el comando:

    python manage.py runserver (numero de puerto opcional)
    
El número de puerto es opcional. Si no proporciona un número de puerto, el servidor se ejecutará en el puerto 8000 en localhost.

# Angular 🅰️
Para correr el servidor de angular primero que todo tenemos que instalar las dependencias, que se realiza con el siguiente comando:

    npm install

Donde se instalaran todas las dependencias del proyecto

# Ejecución Angular ✅
Despues de haber instalado las dependencias al proyecto, ahora podras ejecutarlo con el siguiente comando:

    ng serve

Donde se habilitara un servidor local en el puerdo 4200
