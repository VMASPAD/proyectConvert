import zipfile
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Zipper")
        self.create_widgets()
    
    def create_widgets(self):
        self.select_folder_button = tk.Button(self, text="Select Folder", command=self.select_folder)
        self.select_folder_button.pack(pady=10)
        self.zip_button = tk.Button(self, text="Zip", command=self.zip_folder, state=tk.DISABLED)
        self.zip_button.pack(pady=10)
        self.progress_bar = tk.ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.zip_button.config(state=tk.NORMAL)
    
    def zip_folder(self):
        if not hasattr(self, "folder_path"):
            return
        
        output_path = filedialog.asksaveasfilename(defaultextension=".zip")
        if not output_path:
            return
        
        with zipfile.ZipFile(output_path, mode="w") as zipf:
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.folder_path)
                    zipf.write(file_path, arcname=rel_path)
                    self.progress_bar.step(100 / len(files))
                    self.progress_bar.update()
        
        self.progress_bar.stop()
        self.zip_button.config(state=tk.DISABLED)
        tk.messagebox.showinfo("Success", "Folder zipped successfully.")
            

root = tk.Tk()
root.iconbitmap(r'icon.ico')
app = App(master=root)
app.pack()
app.mainloop()
