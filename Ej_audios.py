import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import wave  # Importa la biblioteca wave para trabajar con archivos WAV

# Variables globales para mantener el estado del sonido
audio_saved = False
canvas_signal = None  # Almacena el lienzo de la señal
canvas_fft = None  # Almacena el lienzo de la transformada de Fourier

# Función para generar y guardar el sonido de la frecuencia en un archivo WAV
def generate_and_save_sound(frequency):
    global audio_saved
    if frequency <= 0:
        return None  # No generar sonido si la frecuencia es menor o igual a 0

    t = np.linspace(0, 1, 44100)  # Generar una señal de 1 segundo a 44.1 kHz
    audio_signal = np.sin(2 * np.pi * frequency * t)

    # Escala la señal a valores de 16 bits para guardarla en un archivo
    audio_signal = (audio_signal * 32767).astype(np.int16)

    # Define el nombre del archivo de audio a guardar
    audio_file_name = "audio_output.wav"

    # Crea un objeto Wave_write para escribir el archivo WAV
    with wave.open(audio_file_name, 'wb') as audio_file:
        audio_file.setnchannels(1)  # Mono
        audio_file.setsampwidth(2)  # 16 bits por muestra
        audio_file.setframerate(44100)  # 44.1 kHz
        audio_file.writeframes(audio_signal.tobytes())

    audio_saved = True

    # Devuelve el nombre del archivo de audio
    return audio_file_name

# Función para actualizar y mostrar las imágenes en el lienzo de Matplotlib
def update_images(frequency):
    global canvas_signal, canvas_fft
    t = np.linspace(0, 1, 100)
    x = np.sin(2 * np.pi * frequency * t)

    # Calculamos la transformada de Fourier de la señal
    X = np.fft.fft(x)

    # Limpiamos los widgets anteriores
    if canvas_signal is not None:
        canvas_signal.get_tk_widget().destroy()
    if canvas_fft is not None:
        canvas_fft.get_tk_widget().destroy()

    # Creamos una figura de Matplotlib para la señal de audio
    fig_signal = plt.figure(figsize=(6, 3))
    plt.plot(t, x)
    plt.title("Frecuencia: {} Hz".format(frequency))

    # Creamos una figura de Matplotlib para la transformada de Fourier
    fig_fft = plt.figure(figsize=(6, 3))
    plt.plot(np.abs(X))
    plt.title("Transformada de Fourier")

    # Creamos lienzos de Matplotlib para cada figura
    canvas_signal = FigureCanvasTkAgg(fig_signal, master=canvas_frame)
    canvas_fft = FigureCanvasTkAgg(fig_fft, master=canvas_frame)

    # Mostramos los nuevos lienzos en el frame de Tkinter
    canvas_signal_widget = canvas_signal.get_tk_widget()
    canvas_signal_widget.pack(side=LEFT, padx=10)
    canvas_fft_widget = canvas_fft.get_tk_widget()
    canvas_fft_widget.pack(side=LEFT, padx=10)

# Función para iniciar la generación y guardar el audio en un archivo
def start_audio():
    global audio_saved
    if not audio_saved:
        file_name = generate_and_save_sound(slider.get())
        if file_name is not None:
            info_label.config(text="Audio guardado como: {}".format(file_name))

# Función para cerrar la aplicación
def close_app():
    exit(1)

# Creamos la ventana principal
root = Tk()
root.title("Generador de audio")
root.geometry("800x400")  # Establecemos un tamaño inicial

# Creamos el slider
slider = Scale(root, from_=20, to=20000, orient=HORIZONTAL, resolution=1)
slider.set(200)  # Valor inicial para el slider (440 Hz)
slider.pack()

# Etiqueta para mostrar información sobre el archivo de audio guardado
info_label = Label(root, text="")
info_label.pack()

# Creamos un frame para los lienzos de Matplotlib
canvas_frame = Frame(root)
canvas_frame.pack()

# Botón para iniciar la generación y guardar el audio en un archivo
start_button = Button(root, text="Generar y Guardar Audio", command=start_audio)
start_button.pack()

# Botón para cerrar la aplicación
close_button = Button(root, text="Cerrar", command=close_app)
close_button.pack()

# Actualizamos y mostramos las imágenes iniciales en el lienzo de Matplotlib
update_images(slider.get())

# Iniciamos la ventana
root.mainloop()

