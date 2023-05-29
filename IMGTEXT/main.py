import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import pytesseract


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("IMG to TXT")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Botón para seleccionar una imagen
        self.select_button = tk.Button(self, text="Seleccionar imagen", command=self.select_image)
        self.select_button.pack()

        # Visualizador de imagen
        self.image_label = tk.Label(self)
        self.image_label.pack()

        # Visualizador de texto
        self.text_label = tk.Label(self, wraplength=600)
        self.text_label.pack()

        # Botón para guardar el texto extraído en un archivo de texto
        self.save_button = tk.Button(self, text="Guardar texto", command=self.save_text, state=tk.DISABLED)
        self.save_button.pack()

    def select_image(self):
        # Abrir el diálogo de selección de archivo
        file_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png;*.bmp")])
        
        if file_path:
            # Mostrar la imagen seleccionada en el visualizador de imagen
            img = Image.open(file_path) # No cambia el tamaño de la imagen
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)
            self.image_label.image = self.photo

            # Extraer el texto de la imagen
            text = pytesseract.image_to_string(img)

            # Mostrar el texto extraído en el visualizador de texto
            self.text_label.config(text=text)

            # Habilitar el botón de guardar texto
            self.save_button.config(state=tk.NORMAL)

            # Guardar el texto extraído en la variable self.text
            self.text = text

    def save_text(self):
        # Abrir el diálogo de selección de archivo
        file_path = filedialog.asksaveasfilename(filetypes=[("Archivo de texto", "*.txt")], defaultextension=".txt")

        if file_path:
            # Guardar el texto extraído en el archivo seleccionado
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text)

root = tk.Tk()
root.iconbitmap(r"icon.ico")
app = App(master=root)
app.mainloop()
