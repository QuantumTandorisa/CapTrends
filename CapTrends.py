'''
   ______          ______                    __    
  / ____/___ _____/_  __/_______  ____  ____/ /____
 / /   / __ `/ __ \/ / / ___/ _ \/ __ \/ __  / ___/
/ /___/ /_/ / /_/ / / / /  /  __/ / / / /_/ (__  ) 
\____/\__,_/ .___/_/ /_/   \___/_/ /_/\__,_/____/  
          /_/                                      
'''
#######################################################
#             CapTrends.py
#
# This is an application that allows you to get, send 
# and analyze search trends in real time.
# You can set priority topics and receive notifications
# when those topics are among the popular trends. 
# In addition, the application stores trends in a 
# database and displays graphs to visualize trends
# over time.
#
#
# 10/18/23 - Changed to Python3 (finally)
#
# Authors: Facundo Fernandez 
#
#
#######################################################


import sqlite3
import tkinter as tk
from twilio.rest import Client
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import schedule
import time
from config import google_username, google_password, custom_useragent

#  Connect to the database / Conectar a la base de datos
conn = sqlite3.connect('trends.db')
c = conn.cursor()

# Create table if it doesn't exist / Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS trends
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             topic TEXT,
             date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Function to send search trends / Función para enviar tendencias de búsqueda
def send_trends():
    def get_trends(country='ARGENTINA', limit=20):
        pytrends = TrendReq(hl='es-AR', tz=360)
        pytrends.build_payload(kw_list=['Python', 'ciberseguridad', 'pasantia', 'exploit'])  # Agrega tus palabras clave dentro de la lista.

        try:
            results = pytrends.trending_searches(pn=country)
            return results[:limit]
        except Exception as e:
            return str(e)

    top_queries = get_trends()
    prioritized_topics = entry_topics.get().split(',')
    found_topics = set(prioritized_topics).intersection(top_queries)

    if found_topics:
        account_sid = 'TU_ACCOUNT_SID'
        auth_token = 'TU_AUTH_TOKEN'
        twilio_number = '+1234567890'
        recipient_number = entry_number.get()

        client = Client(account_sid, auth_token)

        message = "Temas prioritarios encontrados:\n"
        for topic in found_topics:
            message += f"- {topic}\n"

        try:
            message = client.messages.create(
                body=message,
                from_=twilio_number,
                to=recipient_number
            )

            # Store priority issues in the database / Almacenar temas prioritarios en la base de datos
            inserted_topics = []
            for topic in found_topics:
                if topic not in inserted_topics:
                    c.execute("INSERT INTO trends (topic) VALUES (?)", (topic,))
                    inserted_topics.append(topic)
            conn.commit()

            label_result.config(text=f"Mensaje enviado a {recipient_number}. Message SID: {message.sid}")
        except Exception as e:
            label_result.config(text=f"No se pudo enviar el mensaje. Error: {str(e)}")
    else:
        label_result.config(text="No se encontraron temas prioritarios en las tendencias de búsqueda.")

#  Function to display stored trends / Función para mostrar las tendencias almacenadas
def show_trends():
    try:
        c.execute("SELECT * FROM trends ORDER BY date DESC")
        results = c.fetchall()

        if results:
            message = "Tendencias almacenadas:\n"
            for result in results:
                trend_id, topic, date = result
                message += f"{trend_id}: {topic} - {date}\n"

            label_trends.config(text=message)
        else:
            label_trends.config(text="No se encontraron tendencias almacenadas.")
    except Exception as e:
        label_trends.config(text=f"Error: {str(e)}")

# Function to generate and display the trend graph / Función para generar y mostrar el gráfico de tendencias
def generate_graph():
    def get_trends(country='ARGENTINA', limit=20):
        pytrends = TrendReq(hl='es-AR', tz=360)
        pytrends.build_payload(kw_list=[])  # Agrega tus palabras clave dentro de la lista.

        try:
            results = pytrends.trending_searches(pn=country)
            return results[:limit]
        except Exception as e:
            return str(e)

    try:
        top_queries = get_trends()
        counts = range(1, len(top_queries) + 1)

        fig = plt.figure(figsize=(8, 6))
        plt.barh(counts, top_queries, color='blue')
        plt.xlabel('Consultas Populares')
        plt.ylabel('Posición')
        plt.title('Tendencias de Búsqueda')
        plt.yticks(counts, top_queries)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=7, columnspan=2)
    except Exception as e:
        label_trends.config(text=f"Error: {str(e)}")


# Function to program the periodic sending of trends / Función para programar el envío periódico de tendencias
def schedule_sending():
    interval = int(entry_interval.get())
    schedule.every(interval).minutes.do(send_trends)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Function to close the window and end the application / Función para cerrar la ventana y finalizar la aplicación
def close_application():
    conn.close()
    window.destroy()

# Create the main window / Crear la ventana principal
window = tk.Tk()
window.title("Enviar y Analizar Tendencias de Búsqueda")

# Create label and entry for priority topics / Crear etiqueta y entrada para temas prioritarios
label_topics = tk.Label(window, text="Temas Prioritarios (separados por comas):")
label_topics.grid(row=0, column=0, sticky='w')

entry_topics = tk.Entry(window)
entry_topics.grid(row=0, column=1)

# Create label and entry for phone number / Crear etiqueta y entrada para el número de teléfono
label_number = tk.Label(window, text="Número de Teléfono:")
label_number.grid(row=1, column=0, sticky='w')

entry_number = tk.Entry(window)
entry_number.grid(row=1, column=1)

# Create button to get and submit search trends / Crear botón para obtener y enviar tendencias de búsqueda
btn_get_trends = tk.Button(window, text="Obtener y Enviar Tendencias", command=send_trends)
btn_get_trends.grid(row=2, columnspan=2)

# Create label to show the result of sending trends / Crear etiqueta para mostrar el resultado de enviar tendencias
label_result = tk.Label(window, text="")
label_result.grid(row=3, columnspan=2)

# Create button to show stored trends / Crear botón para mostrar tendencias almacenadas
btn_show_trends = tk.Button(window, text="Mostrar Tendencias Almacenadas", command=show_trends)
btn_show_trends.grid(row=4, columnspan=2)

# Create label to display stored trends / Crear etiqueta para mostrar tendencias almacenadas
label_trends = tk.Label(window, text="")
label_trends.grid(row=5, columnspan=2)

# Create button to generate and display the trend graph / Crear botón para generar y mostrar el gráfico de tendencias
btn_generate_graph = tk.Button(window, text="Generar Gráfico de Tendencias", command=generate_graph)
btn_generate_graph.grid(row=6, columnspan=2)

# Create Label and Entry for Schedule Interval / Crear etiqueta y entrada para el intervalo de programación
label_interval = tk.Label(window, text="Intervalo de Programación (minutos):")
label_interval.grid(row=7, column=0, sticky='w')

entry_interval = tk.Entry(window)
entry_interval.grid(row=7, column=1)

# Create button to schedule the periodic sending of trends / Crear botón para programar el envío periódico de tendencias
btn_schedule_sending = tk.Button(window, text="Programar Envío Periódico", command=schedule_sending)
btn_schedule_sending.grid(row=8, columnspan=2)

# Create button to close the application / Crear botón para cerrar la aplicación
btn_close = tk.Button(window, text="Cerrar", command=close_application)
btn_close.grid(row=9, columnspan=2)

# Run UI / Ejecutar la interfaz de usuario
window.mainloop()
