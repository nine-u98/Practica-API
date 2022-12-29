# Django API Backend

## Setup

Como obtener este proyecto en su directorio:

```sh
$ git clone https://github.com/nine-u98/Practica-API.git
$ cd Practica-API
```

Crear un entorno virtual y activarlo para posterior instalar las librerias:

```sh
$ virtualenv env

# windows
$ source env/Scripts/activate
# Linux
$ source env/bin/activate
```

Luego instalar las librerias:

```sh
(env) $ pip install -r requirements.txt
```

Observe el `(env)` delante de la linea de su terminal. Esto indica que esta sesión de terminal opera en un `entorno virtual` configurado por `virtualenv`.

Una vez que `pip` haya terminado de descargar las dependencias:

Luego ejecutamos las migraciones para crear la base de datos de nuesta aplicacion, todo dentro de nuestro entorno virtual.

```sh
# De manera general
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env) $ python manage.py runserver
```

## Hacer uso del proyecto

Navegue hasta `http://127.0.0.1:8000/`

## Credenciales de acceso login
Email
```sh
prueba@gmail.com
```
Password
```sh
123456789
```