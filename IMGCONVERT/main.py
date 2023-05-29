import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Conversión de archivos de imagen")

# Función para seleccionar el archivo de entrada
def select_file():
    file_path = filedialog.askopenfilename()
    input_file_path_var.set(file_path)

# Función para seleccionar la carpeta de salida
def select_output_folder():
    output_folder_path = filedialog.askdirectory()
    output_folder_path_var.set(output_folder_path)

# Función para convertir la imagen a la extensión seleccionada
def convert_image():
    input_path = input_file_path_var.get()
    output_folder = output_folder_path_var.get()
    output_extension = output_extension_var.get()
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + "." + output_extension)
    image = Image.open(input_path)
    image.save(output_path)
    status_label.config(text="¡La conversión a ." + output_extension + " se ha completado!")
    

# Crear los widgets de la interfaz gráfica
input_file_path_var = tk.StringVar()
tk.Label(root, text="Archivo de entrada (.png):").grid(row=0, column=0)
tk.Entry(root, textvariable=input_file_path_var).grid(row=0, column=1)
tk.Button(root, text="Seleccionar archivo", command=select_file).grid(row=0, column=2)

output_folder_path_var = tk.StringVar()
output_folder_path_var.set("")
tk.Label(root, text="Carpeta de salida:").grid(row=1, column=0)
tk.Entry(root, textvariable=output_folder_path_var).grid(row=1, column=1)
tk.Button(root, text="Seleccionar carpeta de salida", command=select_output_folder).grid(row=1, column=2)

output_extensions = ["jpg", "jpeg", "bmp", "gif", "tiff", "ppm", "pgm", "pbm", "webp","ico"]
output_extension_var = tk.StringVar(root)
output_extension_var.set(output_extensions[0])
output_menu = tk.OptionMenu(root, output_extension_var, *output_extensions)
output_menu.grid(row=2, column=1)

tk.Button(root, text="Convertir", command=convert_image).grid(row=3, column=1)
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3)
root.iconbitmap(r'icon.ico')
# Ejecutar la ventana principal
root.mainloop()
