import tkinter as tk
from tkinter import filedialog
import subprocess
import os

root = tk.Tk()
root.withdraw()
root.iconbitmap(r'icon.ico')
# Seleccionar archivo MP4 para convertir
file_path = filedialog.askopenfilename(
    title="Selecciona el archivo MP4 a convertir",
    filetypes=(("MP4", "*.mp4"),)
)

if file_path:
    # Obtener el nombre del archivo y la extensión
    filename, extension = os.path.splitext(file_path)

    # Crear la lista de formatos de salida
    output_formats = [".avi", ".mkv", ".flv", ".mov", ".wmv", ".mpg", ".webm", ".gif"]

    # Crear la ventana de selección de formato de salida
    format_selection_window = tk.Toplevel()
    format_selection_window.title("Selecciona el formato de salida")
    format_selection_window.geometry("300x100")

    # Crear el menú desplegable para seleccionar el formato de salida
    format_variable = tk.StringVar()
    format_variable.set(output_formats[0])

    format_label = tk.Label(format_selection_window, text="Formato de salida:")
    format_label.pack()

    format_dropdown = tk.OptionMenu(format_selection_window, format_variable, *output_formats)
    format_dropdown.pack()

    # Botón de confirmación para la selección del formato de salida
    def confirm_format():
        format_selection_window.destroy()

    confirm_button = tk.Button(format_selection_window, text="Confirmar", command=confirm_format)
    confirm_button.pack()

    # Esperar a que se cierre la ventana de selección de formato de salida
    format_selection_window.wait_window()

    # Obtener la ubicación de salida del archivo convertido
    output_path = filedialog.asksaveasfilename(
        title=f"Guardar como {format_variable.get()}",
        initialfile=f"{os.path.basename(filename)}{format_variable.get()}",
        defaultextension=format_variable.get()
    )

    if output_path:
        # Convertir el archivo a formato de salida seleccionado
        subprocess.run(["ffmpeg", "-i", file_path, output_path])

        # Abrir la carpeta de salida
        output_folder = os.path.dirname(output_path)
        os.startfile(output_folder)
