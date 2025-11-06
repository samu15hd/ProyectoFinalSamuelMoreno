# BlogMe

BlogMe es un proyecto final desarrollado por Samuel Moreno para la comisión 78130 de Coderhouse. Es una plataforma de blogging personal construida con Django, que permite a los usuarios publicar, editar y gestionar páginas, además de intercambiar mensajes entre ellos. El diseño se basa en una estética minimalista y monocromática, enfocada en la claridad, la funcionalidad y la identidad personal.

Samuel Moreno, 17 años, nacido en Venezuela el 3 de noviembre de 2008. Apasionado por la música, la programación y el diseño. Actualmente cursa la comisión 78130 de Coderhouse, donde desarrolla este proyecto como parte de su formación en desarrollo web con Django.

Funcionalidades principales:
- Registro e inicio de sesión de usuarios
- Creación, edición y eliminación de páginas personales
- Visualización de páginas publicadas
- Perfil editable
- Messenger entre usuarios registrados
- Página “Acerca de mí” con presentación personal
- Navegación clara y coherente con estilo monocromático

Tecnologías utilizadas:
- Python 3.13
- Django 5.2
- Bootstrap 5
- SQLite como base de datos por defecto

Instalación:
1. Clonar el repositorio:
   git clone https://github.com/tuusuario/blogme.git
   cd blogme

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar migraciones:
   python manage.py makemigrations
   python manage.py migrate

4. Iniciar el servidor:
   python manage.py runserver

Estructura de templates:
- base.html: layout principal con navbar negra y tipografía Inter
- home.html: página de bienvenida
- mis_paginas.html: páginas creadas por el usuario
- listar_paginas.html: páginas públicas
- crear_pagina.html / editar_pagina.html: formularios de publicación
- conversacion.html: messenger entre usuarios
- about.html: presentación personal
- perfil.html / editar_perfil.html: gestión de perfil

Este proyecto es de uso educativo y personal. Todos los derechos reservados por Samuel Moreno.