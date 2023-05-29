import tkinter as tk
from tkinter import ttk, filedialog
import fitz
from PIL import Image


class PDFConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the window
        self.title("PDF Converter")
        self.geometry("400x200")

        # Create the main frame
        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create the conversion type dropdown
        conversion_type_label = ttk.Label(self.main_frame, text="Select conversion type:")
        conversion_type_label.pack(side=tk.TOP, pady=(0, 5))
        self.conversion_type_var = tk.StringVar()
        self.conversion_type_dropdown = ttk.Combobox(self.main_frame, textvariable=self.conversion_type_var,
                                                     state="readonly", values=["PDF to PNG", "PNG to PDF"])
        self.conversion_type_dropdown.pack(side=tk.TOP, pady=(0, 10))
        self.conversion_type_dropdown.current(0)

        # Create the select file button
        select_file_button = ttk.Button(self.main_frame, text="Select file", command=self.select_file)
        select_file_button.pack(side=tk.TOP)

        # Create the convert button
        convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert_file)
        convert_button.pack(side=tk.TOP, pady=(10, 0))

        # Create the select directory button
        select_dir_button = ttk.Button(self.main_frame, text="Select directory", command=self.select_directory)
        select_dir_button.pack(side=tk.TOP, pady=(10, 0))

        # Set the default file paths
        self.file_path = ""
        self.output_dir = ""

    def select_file(self):
        # Select the file
        file_types = [("PDF Files", "*.pdf"), ("PNG Files", "*.png")]
        self.file_path = filedialog.askopenfilename(title="Select file", filetypes=file_types)

    def select_directory(self):
        # Select the output directory
        self.output_dir = filedialog.askdirectory(title="Select output directory")

    def convert_file(self):
        # Get the selected conversion type
        conversion_type = self.conversion_type_var.get()

        if conversion_type == "PDF to PNG":
            # Convert the PDF to PNG
            pdf_doc = fitz.open(self.file_path)
            for i in range(pdf_doc.page_count):
                page = pdf_doc.load_page(i)
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                output_path = f"{self.output_dir}/page{i + 1}.png"
                img.save(output_path)

            # Show success message
            tk.messagebox.showinfo("Success", "PDF successfully converted to PNGs!")
        elif conversion_type == "PNG to PDF":
            # Select the output file path
            file_types = [("PDF Files", "*.pdf")]
            self.output_path = filedialog.asksaveasfilename(title="Save as", filetypes=file_types)

            # Convert the PNG to PDF
            images = []
            for i in range(1, 101):
                try:
                    img = Image.open(f"{self.file_path[:-4]}_page{i}.png")

                    images.append(img)
                except FileNotFoundError:
                    break
            images[0].save(self.output_file_path, save_all=True, append_images=images[1:])

            # Show success message
            tk.messagebox.showinfo("Success", "PNGs successfully converted to PDF!")

# Run the application
app = PDFConverter()
app.iconbitmap(r'icon.ico')
app.mainloop()
