# Proyecto Urban Routes
# Desarrollado por: Crystal Puentes - Grupo 19 QA

# Descripción del Proyecto
El objetivo de este proyecto es automatizar las pruebas sobre el proceso completo de solicitar un taxi en 
Urban Routes. Las pruebas cubren acciones como la configuración de la dirección, la selección de tarifa, el 
ingreso de datos personales y de pago, y la solicitud de un taxi, entre otros. Se validan tanto los flujos 
principales como casos opcionales, como la visualización de la información del conductor.

# Estructura del Proyecto
El proyecto está organizado en los siguientes archivos:

├── data.py                    # Datos utilizados en las solicitudes y pruebas.
├── UrbanRoutesLocators.py      # Localizadores de elementos de la página de Urban Routes.
├── TestUrbanRoutes.py          # Pruebas automatizadas para el proceso de solicitud de taxi.
├── UrbanRoutesPage.py          # Funciones y acciones relacionadas con la página de Urban Routes.
├── setup_driver.py             # Configuración del driver de Selenium para Chrome.
├── README.md                  # Descripción del proyecto y pasos para ejecutar.
├── .gitignore                 # Archivos y directorios a ignorar por Git.


# Tecnologías Utilizadas
Python: Lenguaje de programación principal.
Requests: Biblioteca para realizar solicitudes HTTP.
pytest: Framework para ejecutar las pruebas automatizadas.
GitHub: Para gestionar el código fuente y colaborar en el proyecto.

# Instrucciones para Ejecutar las Pruebas
Sigue estos pasos para ejecutar las pruebas:
Clona el repositorio:
git clone https://github.com/Crosty02/qa-project-Urban-Routes-es.git
Abre el proyecto en tu editor preferido (como PyCharm) y crea un nuevo entorno de proyecto.
Instala las dependencias necesarias (si es que no están instaladas aún):
pip install -r requirements.txt
Ejecuta las pruebas utilizando pytest

Para ejecutar las pruebas, navega al archivo main.py y ejecuta:
pytest TestUrbanRoutes.py
Las pruebas se ejecutarán y los resultados se mostrarán en la consola.

# Pruebas Automatizadas

Las pruebas automatizadas cubren los siguientes pasos en el proceso de solicitud de un taxi:

* Configurar la dirección: Validar que la dirección de recogida se configure correctamente.
* Seleccionar la tarifa Comfort: Verificar que la tarifa Comfort se seleccione sin problemas.
* Rellenar el número de teléfono: Comprobar que el número de teléfono se ingrese correctamente y sea válido.
* Agregar una tarjeta de crédito: Validar que se pueda agregar una tarjeta de crédito correctamente
(recuerda que el campo CVV debe perder el enfoque para activar el botón).
Escribir un mensaje para el controlador: Comprobar que el mensaje se envíe correctamente.
* Pedir una manta y pañuelos: Verificar que los artículos sean añadidos correctamente.
* Pedir 2 helados: Confirmar que los helados se pidan correctamente.
* Aparece el modal de búsqueda de taxi: Validar que el modal de búsqueda se muestre correctamente.
* Información del conductor: Validar que la información del conductor aparezca en el modal después 
de la asignación del conductor.

Ejercicio Adicional (Opcional)
El ejercicio incluye una parte opcional que involucra la verificación de la cuenta regresiva y 
la visualización de los detalles del viaje cuando un conductor es asignado.
Esta parte es un desafío adicional para asegurarse de que el flujo de trabajo sea correcto.

