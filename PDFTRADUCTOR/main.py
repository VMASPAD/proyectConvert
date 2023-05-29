import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from googletrans import Translator
from PyPDF2 import PdfFileWriter, PdfFileReader
import pytesseract
from io import BytesIO

translator = Translator(service_urls=['translate.google.com'])

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.select_file_button = tk.Button(self.master, text="Seleccionar archivo", command=self.select_file)
        self.select_file_button.pack()

        self.language_label = tk.Label(self.master, text="Selecciona el idioma al que quieres traducir el PDF:")
        self.language_label.pack()

        self.language_options = ["es", "fr", "de", "it"]
        self.language_var = tk.StringVar(self.master)
        self.language_var.set(self.language_options[0])
        self.language_menu = tk.OptionMenu(self.master, self.language_var, *self.language_options)
        self.language_menu.pack()

        self.translate_button = tk.Button(self.master, text="Traducir", command=self.translate_file)
        self.translate_button.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    def translate_file(self):
        language = self.language_var.get()
        output_file_path = "" + self.file_path

        with open(self.file_path, "rb") as pdf_file:
            input_pdf = PdfFileReader(pdf_file)
            output_pdf = PdfFileWriter()

            for i in range(input_pdf.getNumPages()):
                page = input_pdf.getPage(i)
                images = convert_from_path(self.file_path, dpi=300, grayscale=True)
                text = pytesseract.image_to_string(images[i], lang="eng")
                translation = translator.translate(text, dest=language).text
                
                output_text_stream = BytesIO()
                output_text_stream.write(translation.encode("utf-8"))
                
                output_text_page = output_pdf.addBlankPage(width=page.mediaBox.getWidth(),
                                                           height=page.mediaBox.getHeight())
                output_text_page.mergePage(page)
                output_pdf.addBookmark("Translated Text", i, parent=None)

            with open(output_file_path, "wb") as output_file:
                output_pdf.write(output_file)

            self.complete_label = tk.Label(self.master, text="Traducción completada y guardada en: " + output_file_path)
            self.complete_label.pack()

root = tk.Tk()
root.iconbitmap(r'icon.ico')
app = App(master=root)
app.mainloop()
