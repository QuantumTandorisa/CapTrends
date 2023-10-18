CapTrends es una aplicación que te permite obtener, enviar y analizar tendencias de búsqueda en tiempo real. Puedes configurar temas prioritarios y recibir notificaciones cuando esos temas estén entre las tendencias populares. Además, la aplicación almacena en una base de datos y muestra gráficos para visualizar a lo largo del tiempo.

## Características

- Obtén y envía tendencias de búsqueda en tiempo real.
- Configura temas prioritarios y recibe notificaciones cuando se vuelvan populares.
- Almacena las tendencias en una base de datos para su posterior análisis.
- Muestra gráficos para visualizar las tendencias a lo largo del tiempo.

## Requisitos

- Python 3.9 o superior.
- Paquetes de Python: `sqlite3`, `tkinter`, `twilio`, `pytrends`, `matplotlib`, `schedule`.

## Uso

1. Clona este repositorio en tu máquina local.
2. Ejecuta la aplicación con Python 3.9 o superior: `python3 CapTrends.py`.
3. Configura los temas prioritarios y el número de teléfono en la interfaz de usuario.
4. Utiliza los botones disponibles para obtener, enviar, mostrar y analizar tendencias de búsqueda.

## Configuración de API

Asegúrate de configurar las siguientes API en el archivo `config.py` antes de usar la aplicación:

- `google_username`: Tu nombre de usuario de Google.
- `google_password`: Tu contraseña de Google.
- `custom_useragent`: Tu agente de usuario personalizado.
