Aplicación de Envío y Análisis de Tendencias de Búsqueda

Esta es una aplicación que te permite obtener, enviar y analizar las tendencias de búsqueda en tiempo real. Puedes configurar temas prioritarios y recibir notificaciones cuando esos temas se encuentren entre las tendencias populares. Además, la aplicación almacena las tendencias en una base de datos y muestra gráficos para visualizar las tendencias a lo largo del tiempo.

Características

   Obtención de tendencias de búsqueda en tiempo real.
   Envío de notificaciones por SMS utilizando Twilio.
   Almacenamiento de tendencias en una base de datos SQLite.
   Visualización de tendencias almacenadas.
   Generación de gráficos para visualizar las tendencias.
   Programación del envío periódico de tendencias.

Requisitos previos

Antes de utilizar esta aplicación, debes asegurarte de tener los siguientes requisitos previos:

   Python 3 instalado en tu sistema.
   Las siguientes bibliotecas de Python instaladas:
        sqlite3
        tkinter
        twilio
        pytrends
        matplotlib
        schedule

Instalación

   Clona este repositorio en tu máquina local o descarga el código fuente.
   Asegúrate de tener los requisitos previos mencionados anteriormente.
   Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra el código fuente.
   Ejecuta el siguiente comando para instalar las dependencias:

   shell
   
      pip install -r requirements.txt

Configuración

Antes de ejecutar la aplicación, debes realizar algunas configuraciones:

   Abre el archivo main.py en un editor de texto.
   Configura tus credenciales de Google Trends API en la siguiente línea:

   python
    
    pytrends = TrendReq(google_username='TU_NOMBRE_DE_USUARIO', google_password='TU_CONTRASEÑA', custom_useragent='TU_USER_AGENT')
    

Configura tus credenciales de Twilio en las siguientes líneas:

   python
    
    account_sid = 'TU_ACCOUNT_SID'
    auth_token = 'TU_AUTH_TOKEN'
    twilio_number = '+1234567890'
    

Uso

   Ejecuta el archivo main.py utilizando Python.
   Se abrirá una ventana de interfaz de usuario.
   Completa los campos de temas prioritarios y número de teléfono.
   Haz clic en el botón "Obtener y Enviar Tendencias" para obtener las tendencias actuales y enviar notificaciones si se encuentran temas prioritarios.
   Utiliza los otros botones de la interfaz de usuario para mostrar las tendencias almacenadas, generar gráficos y programar el envío periódico de tendencias.

Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error, tienes alguna idea de mejora o deseas agregar nuevas características, puedes abrir un "issue" o enviar una solicitud de extracción.
