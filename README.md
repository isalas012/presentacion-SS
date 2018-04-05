## Proyecto ##
  * Instalar django (pip3 install django)
  * Crear el proyecto (django-admin startproject presentacion)

##Aplicación##
  * Crear aplicación (python manage.py startapp testBlog)
  * Crear archivo urls.py para definir las urls de la aplicación
  * Crear los modelos a utilizar y añadirlos a la base de datos (python manage.py migrate)
  * Agregar vistas y rutas editando los archivo urls.py y views.py

##Ejecutar Servidor##
  * python3 manage.py runserver

##Generar Test##
* Crear archivo test.py
* Importar TestCase (from django.test import TestCase) y los modelos a utilizar (from .models import modelo)
* Crear clase de prueba que extienda TestCase y definir setUp y funciones de prueba.
* Ejecutar prueba (python3 manage.py test)
