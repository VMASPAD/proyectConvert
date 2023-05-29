import fitz
from tkinter import filedialog
import tkinter as tk


def select_file():
    # Abrir un diálogo de selección de archivo
    file_path = filedialog.askopenfilename()
    return file_path


def select_save_path():
    # Abrir un diálogo de selección de archivo para guardar
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf")
    return file_path


def convert_to_pdf():
    # Seleccionar el archivo a convertir
    file_path = select_file()

    # Convertir el archivo a PDF
    with fitz.open(file_path) as ebook:
        pdf_bytes = ebook.convert_to_pdf()

    # Seleccionar la ruta de guardado del archivo PDF
    save_path = select_save_path()

    # Guardar el archivo PDF
    with open(save_path, "wb") as pdf_file:
        pdf_file.write(pdf_bytes)


# Crear una ventana Tkinter
root = tk.Tk()
root.geometry("400x200")

# Agregar un icono a la ventana
root.iconbitmap(r"icon.ico")
root.title('Convertidor de E-Book = PDF')
# Crear un botón para iniciar la conversión
button = tk.Button(root, text="Convertir a PDF", command=convert_to_pdf)
button.pack()

# Ejecutar la ventana
root.mainloop()
