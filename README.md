# dakiclean_v0.1

Version Inicial Pagina Web Daki-Clean
Esta pagina web consta con una interfaz simple, consta tambien con inicio de sesion.

Esta funciona en base al framework Django junto con html css, Tailwind CSS y JavaScript

Trabaja directamente con la base de Datos MYSQL

--------------------Notas--------------------

Para que arranque de forma correcta deves ingresar a la base de datos MYSQL y crear una nueva base de datos. (Esta en setting.py)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dakiclean_db',    <------Con Este Nombre 
        'USER': 'root',
        'PASSWORD': 'contraseña aletoria segun tu password',
    }
}


# Una vez hecho esto ingresaras a tu Visual Studio Code Y abriras la carpeta

Abrir la terminal

# Deberas de Ingresar lo Sigiente:

python manage.py makemigrations

python manage.py migrate 

python manage.py runserver 


------------Y listo------------


