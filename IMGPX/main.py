from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageEnhance

root = Tk()
root.title("Aumentar calidad de imagen PNG")

def open_file():
    global original_image, original_image_label
    
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    
    if file_path:
        original_image = Image.open(file_path)
        
        # Redimensionar la imagen para que quepa en la pantalla
        width, height = original_image.size
        while width > 600 or height > 600:
            width *= 0.9
            height *= 0.9
        original_image = original_image.resize((int(width), int(height)))
        
        original_image_label.configure(image=original_image)
        original_image_label.image = original_image
        
def increase_quality():
    global original_image
    
    quality_value = quality_slider.get()
    
    # Aplicar el filtro de aumento de calidad
    enhancer = ImageEnhance.Sharpness(original_image)
    sharpened_image = enhancer.enhance(quality_value)
    
    # Guardar la imagen con un nombre elegido por el usuario
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        sharpened_image.save(file_path)

# Crear los widgets
original_image_label = Label(root)
original_image_label.pack()

open_button = Button(root, text="Abrir archivo", command=open_file)
open_button.pack()

quality_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Calidad")
quality_slider.set(5)
quality_slider.pack()

increase_button = Button(root, text="Aumentar calidad", command=increase_quality)
increase_button.pack()

root.mainloop()
