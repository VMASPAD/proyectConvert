import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *

def download_mp3():
    # Obtener la URL de YouTube del usuario
    url = url_entry.get()
    # Crear objeto de YouTube y obtener la mejor calidad de audio
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    # Mostrar ventana de diálogo de selección de archivo
    root.filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Guardar como", filetypes=[("Archivo MP3", "*.mp3")])
    # Descargar el archivo de audio y guardar en la ubicación seleccionada
    audio.download(output_path=os.path.dirname(root.filename), filename=os.path.basename(root.filename) + ".mp4")
    # Convertir archivo de audio a MP3
    mp4_file = os.path.join(os.path.dirname(root.filename), os.path.basename(root.filename) + ".mp4")
    mp3_file = os.path.join(os.path.dirname(root.filename), os.path.basename(root.filename) + ".mp3")
    AudioFileClip(mp4_file).write_audiofile(mp3_file)
    # Eliminar archivo de audio original
    os.remove(mp4_file)
    # Mostrar mensaje de éxito
    tk.messagebox.showinfo("Descarga completada", "El archivo MP3 se ha descargado y guardado correctamente en la ubicación seleccionada.")

# Crear ventana de la aplicación
root = tk.Tk()
root.title("Descargar MP3 de YouTube")
root.iconbitmap(r'icon.ico')
# Crear cuadro de entrada para la URL de YouTube
url_label = tk.Label(root, text="URL de YouTube:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Crear botón para descargar el archivo MP3
download_button = tk.Button(root, text="Descargar MP3", command=download_mp3)
download_button.pack()

# Ejecutar la ventana de la aplicación
root.mainloop()
