# Pasos Puesta en marcha del proyecto

Ingresando a la carpeta raiz del proyecto.

Instalamos los requemientos que el sistema necesita en el entorno virtual, las librerias y sus versiones que se necesitan estan en el documento requirements.txt, con el siguiente comando se instalan automaticamente.
    (djangoDataForce) ~$ pip install -r requirements.txt

Hacer las migraciones
    (djangoDataForce) ~$ python manage.py makemigrations 
    (djangoDataForce) ~$ python manage.py migrate

Crear usuario administrador
    (djangoDataForce) ~$ python manage.py createsuperuser

Correr el servidor de django
    (djangoDataForce) ~$ python manage.py runserver

Poner en el navegador la url que sale en el terminal para entrar el sistema, ejemplo: es http://127.0.0.1:8000

 __Nota__
    Para el siguiente error se puede genera cuando hay conflictos en las versiones de python y pkg, por las versiones recientes que estan tienen. 
        // from pkg_resources import load_entry_point ImportError: No module named pkg_resources

    Para solucionar hay que traer las versiones compatibles con los siguientes comando.
    (djangoDataForce) ~$ pip install --upgrade setuptools
    (djangoDataForce) ~$ pip install --upgrade distribute


Para ingresar al administrador de Django ingresamos la url que sale en el terminal y acontinuacion escribir "/admin", ingresamos el usuario y contraseña de super administrador

Llegado hasta aquí el sistema ya debe estar funcionando

Para salir del entorno virtual se puede ejecutar desde cualquier lugar del terminal: deactivate




# Algunos comandos básicos

    // Crear proyectos en django. Desde el terminal, moverse a la carpeta proyectos_django y ejecutar

    (Nuevo_Proyecto) ~$ django-admin startproject nombre_proyecto

    // Crear aplicaciones en un proyecto de django. Desde el terminal, moverse a la carpeta nombre_proyecto

    (Nuevo_Proyecto) ~$ django-admin startapp nombre_app


# Subir cambios al repositorio

    // Prepara todos los cambios para subirlos
    ~$ git add .

    // Descripción de lo que se sube
    ~$ git commit -m "descripción específica acerca del cambio que se está subiendo"

    // Con este comando pedirá las credenciales de la cuenta
    ~$ git push origin master

    // Actualizar los cambios de un repositorio
    ~$ git pull

Cuando un proyecto tiene varios desarrolladores se deben usar ramas

    // Crear rama a partir de la master (nueva funcionalidad)
    ~$ git checkout -b nombre_rama

    // Subir cambios a nombre_rama
    ~$ git push origin nombre_rama

    // Terminada y probada la funcionalidad, moverse a la rama master para hacer la fusión
    ~$ git checkout master

    // Fusionar nombre_rama con la rama master
    ~$ git merge nombre_rama

En caso que hayan conflictos en la fusión, probar lo siguiente

    // Ver los archivos que tienen conflicto
    git status

    git add archivos ó git add .

    git commit -m "solución de los conflictos en la fusión"

    git merge nombre_rama

    //ver el estado
    git status

    git push

Arreglar los archivos en donde hubo conflictos durante la fusión, luego suba los cambios

    git add .

    git commit -m "fusion completada"

    git push origin master

Si la fusión se completó con éxito, eliminar la rama de manera local

    ~$ git branch -d nombre_rama

    // Eliminar la rama remota
    ~$ git push origin :nombre_rama

    // Limpiar lista de las ramas eliminadas en local
    ~$ git fetch --prune

Establecer una rama como principal

    ~$ git remote set-head origin nombre_rama

