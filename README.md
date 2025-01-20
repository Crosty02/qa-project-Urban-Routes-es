Proyecto Urban Routes
Nombre completo y cohort
Crystal Puentes - Grupo 19 QA

Descripción del proyecto
Este proyecto tiene como objetivo realizar pruebas automatizadas sobre un servicio web, validando la creación de kits y usuarios a través de solicitudes HTTP. Se incluyen pruebas positivas y negativas para garantizar el correcto funcionamiento de las funcionalidades del sistema.

Estructura del proyecto
El proyecto está organizado de la siguiente manera:

├── configuration.py # Configuración de rutas y URLs del servicio. ├── data.py # Datos utilizados en las solicitudes y pruebas. ├── sender_stand_request.py # Funciones para enviar solicitudes HTTP. ├── create_kit_name_test.py # Archivo con las pruebas automatizadas. ├── README.md # Descripción del proyecto y pasos para ejecutar. ├── .gitignore # Archivos y directorios a ignorar por Git.

Tecnologías utilizadas
Python
Requests (para realizar solicitudes HTTP)
pytest (para ejecutar las pruebas)
GitHub (para gestionar el código y colaborar)
Instrucciones para ejecutar las pruebas
git clone https://github.com/Crosty02/qa-project-Urban-Grocers-app-es.git Ingresar a pycharm buscar el archivo y crear un nuevo proyecto, ejecutar pruebas.
El proyecto consta de los siguientes archivos:
configuration.py Este archivo contiene las configuraciones principales, como la URL base del servicio y las rutas de las solicitudes.

data.py Contiene los datos predefinidos para las solicitudes, como el cuerpo de las peticiones (user_body, kit_body) y encabezados (headers).

sender_stand_request.py Incluye las funciones para enviar las solicitudes HTTP al servicio, como la creación de usuarios y kits.

create_kit_name_test.py Este archivo contiene las pruebas automatizadas, organizadas según la lista de comprobación.

README.md Este archivo explica el propósito del proyecto y cómo ejecutarlo.

.gitignore Define los archivos y directorios que deben ser ignorados por Git.

Ejecutar las pruebas en pytest create_kit_name_test.py
Validar resultados Cada prueba valida un caso de la lista de comprobación. Los resultados se mostrarán en la consola.
Lista de Comprobación de Pruebas Positivas Nombre mínimo válido (1 carácter) Nombre máximo válido (511 caracteres) Uso de caracteres especiales Uso de espacios Uso de números
Lista de Comprobación de Pruebas Negativas Nombre mínimo válido (1 carácter) Nombre vacío Nombre excede el límite (512 caracteres) Parámetro name no se pasa en solicitud Tipo de dato incorrecto para name
