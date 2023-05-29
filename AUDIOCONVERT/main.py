import tkinter as tk
from tkinter import filedialog
import os
import subprocess

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Conversión de archivos de audio")

# Función para seleccionar el archivo de entrada
def select_file():
    file_path = filedialog.askopenfilename()
    input_file_path.set(file_path)

# Función para seleccionar la carpeta de salida
def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_path.set(output_folder_path)

# Función para convertir el archivo .mp3 a .ogg
def convert_to_ogg():
    input_path = input_file_path.get()
    output_folder = output_folder_path.get()
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".ogg")
    subprocess.call(["ffmpeg", "-i", input_path, output_path])
    status_label.config(text="¡La conversión a .ogg se ha completado!")

# Función para convertir el archivo .mp3 a .wav
def convert_to_wav():
    input_path = input_file_path.get()
    output_folder = output_folder_path.get()
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".wav")
    subprocess.call(["ffmpeg", "-i", input_path, output_path])
    status_label.config(text="¡La conversión a .wav se ha completado!")

# Función para convertir el archivo .mp3 a .mp3 (sí, es redundante, pero puede ser útil para algunas situaciones)
def convert_to_mp3():
    input_path = input_file_path.get()
    output_folder = output_folder_path.get()
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".mp3")
    subprocess.call(["ffmpeg", "-i", input_path, output_path])
    status_label.config(text="¡La conversión a .mp3 se ha completado!")

# Crear los widgets de la interfaz gráfica
input_file_path = tk.StringVar()
tk.Label(root, text="Archivo de entrada (.mp3):").grid(row=0, column=0)
tk.Entry(root, textvariable=input_file_path).grid(row=0, column=1)
tk.Button(root, text="Seleccionar archivo", command=select_file).grid(row=0, column=2)

output_folder_path = tk.StringVar()
tk.Label(root, text="Carpeta de salida:").grid(row=1, column=0)
tk.Entry(root, textvariable=output_folder_path).grid(row=1, column=1)
tk.Button(root, text="Seleccionar carpeta de salida", command=select_output_folder).grid(row=1, column=2)

tk.Button(root, text="Convertir a .ogg", command=convert_to_ogg).grid(row=2, column=0)
tk.Button(root, text="Convertir a .wav", command=convert_to_wav).grid(row=2, column=1)
tk.Button(root, text="Convertir a .mp3", command=convert_to_mp3).grid(row=2, column=2)
status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3)
root.iconbitmap(r"icon.ico")
# Ejecutar la ventana principal
root.mainloop()
