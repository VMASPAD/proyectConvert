import tkinter as tk
from tkinter import filedialog
from pdf2docx import parse
import docx2pdf

# Función para convertir un archivo PDF a DOCX
def convert_pdf_to_docx():
    # Selecciona el archivo PDF que se desea convertir
    file_path = filedialog.askopenfilename(title='Seleccionar archivo PDF', filetypes=[('PDF', '*.pdf')])
    
    # Crea la ruta de salida para el archivo DOCX
    docx_file_path = filedialog.asksaveasfilename(defaultextension='.docx', filetypes=[('DOCX', '*.docx')])

    # Si el usuario cancela la selección de ruta, salimos de la función
    if not docx_file_path:
        return
    
    # Convierte el archivo PDF a DOCX
    parse(file_path, docx_file_path)
    
    # Muestra un mensaje de éxito
    tk.messagebox.showinfo('Convertir PDF a DOCX', 'La conversión se completó con éxito.')

# Función para convertir un archivo DOCX a PDF
def convert_docx_to_pdf():
    # Selecciona el archivo DOCX que se desea convertir
    file_path = filedialog.askopenfilename(title='Seleccionar archivo DOCX', filetypes=[('DOCX', '*.docx')])
    
    # Crea la ruta de salida para el archivo PDF
    pdf_file_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('PDF', '*.pdf')])

    # Si el usuario cancela la selección de ruta, salimos de la función
    if not pdf_file_path:
        return
    
    # Convierte el archivo DOCX a PDF
    docx2pdf.convert(file_path, pdf_file_path)
    
    # Muestra un mensaje de éxito
    tk.messagebox.showinfo('Convertir DOCX a PDF', 'La conversión se completó con éxito.')

# Crea una ventana principal
root = tk.Tk()
root.title('Convertidor Beta')
root.iconbitmap('icon.ico')
# Crea una etiqueta para el título
title_label = tk.Label(root, text='Convertir archivos', font=('Arial', 16))
title_label.pack(pady=20)

# Crea un botón para convertir un archivo PDF a DOCX
pdf_to_docx_button = tk.Button(root, text='PDF a DOCX', font=('Arial', 12), command=convert_pdf_to_docx)
pdf_to_docx_button.pack(pady=10)

# Crea un botón para convertir un archivo DOCX a PDF
docx_to_pdf_button = tk.Button(root, text='DOCX a PDF', font=('Arial', 12), command=convert_docx_to_pdf)
docx_to_pdf_button.pack(pady=10)

# Inicia el bucle principal de la ventana
root.mainloop()
