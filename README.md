### Prueba Técnica - API GET /users

Este pequeño proyecto es desarrollado como Prueba Técnica para el desarrollo de una API utilizando la API https://randomuser.me/documentation. La API desarrollada en este respositorio está diseñada para obtener un listado de 10 usuarios aleatorios, cuidando la confidencialidad de los datos sensibles. Además permite que se puedan filtrar/organizar por género y que se puedan traer un número especifico de usuarios dependiendo de la necesidad del cliente. Esta API fue desarrollada usando djangorestframework. 


# Instalación

1) Clona este repositorio.
https://github.com/Lorenainfinita/intechmom_prueba.git

2) Instala las dependencias y librerias disponibles en el requirements.txt

Puedes usar el siguiente comando: 

	pip install -r requirements.txt

3) Ejecuta las migraciones 

Puedes usar el siguiente comando:

	python manage.py migrate

4) Inicia el Servidor de Desarrollo

Puedes usar el siguiente comando: 

	python manage.py runserver

-------------

# ¿Cómo usar esta API?

La aplicación Django expone una API que organiza y filtra los datos de RandomUser a la que puedes acceder una vez ejecutes el servidor. 

Puedes usar el parametro limit el cual define el número máximo de resultados a mostrar.  Si no usas un limite, obtendras días usuarios por defecto.
Ejemplo: http://localhost:8000/users?limit=5.

También puedes usar el parametro categorize el cual organiza los resultados de la consulta según su género

Ejemplo: http://localhost:8000/users?categorize=gender.
