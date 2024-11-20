# Equipo c22-03-n-webapp / No Country

Plataforma de Marketplace de Productos Artesanales

Nombre del proyecto: Pro_Art

1. Clonar repositorio de GitHub en local

2. Crear su entorno virtual
python3 -m venv env

3. Activar el entorno
source env/bin/activate

4. Instalar paquetes necesrios
pip install -r requirement.txt
	
5. El archivo requirements.txt (que ya está creado)
En él se anotarán todos los paquetes necesarios para el proyecto con su versión
Puedes ver los paquetes instalados usando:
pip freeze

6. El archivo .gitigore (está creado)
Anotar en él todos los archivos que NO se quieran subir a repo como el env (entorno virtual), db.sqlite3 o uploads

7. La BBDD db.sqlite3 está ignorada (.gitignore)
Para que cada uno pueda hacer pruebas sin afectar al resto

python manage.py makemigrations 
python manage.py migrate

8. Crear superuser (admin de Django)
python manage.py createsuperuser
Username: el que quiera
mail: el que quiera
password: el que quiera

* Aquí se podrá hacer pruebas en la BBDD, sin que afecte a los demás compañeros. 
* Hay que configurar todos los archivos admin.py de cada app (products, sales, users) ESTO ya está configurado.

APP  products:
En el modelo image.
Para las imágenes se ha configurado settings.py en él se ha añadido la siguiente linea:

MEDIA_ROOT = BASE_DIR / ‘uploads/’

Esto es para cuando se vayan a subir imágenes, se guardará automáticamente en la carpeta uploads, ESTO ya está configurado.
OJO la carpeta uploads también está en .ignore

9. Arrancar el servidor
python manage.py runserver
Navegador:
127.0.0.1:8000/admin
Aquí se podrá hacer las pruebas cada uno por individual
