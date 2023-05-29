import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *

class YoutubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Descargador de Youtube")

        self.video_quality = tk.StringVar()
        self.audio_quality = tk.StringVar()
        self.video_quality.set('720p')
        self.audio_quality.set('128kbps')

        self.video_label = tk.Label(master, text="Calidad de video")
        self.video_label.pack()
        self.video_menu = tk.OptionMenu(master, self.video_quality, '1080p', '720p', '480p', '360p', '240p', '144p')
        self.video_menu.pack()

        self.audio_label = tk.Label(master, text="Calidad de audio")
        self.audio_label.pack()
        self.audio_menu = tk.OptionMenu(master, self.audio_quality, '128kbps', '160kbps', '192kbps', '256kbps', '320kbps')
        self.audio_menu.pack()

        self.video_button = tk.Button(master, text="Descargar Video", command=self.download_video)
        self.video_button.pack()

        self.audio_button = tk.Button(master, text="Descargar Audio", command=self.download_audio)
        self.audio_button.pack()

        self.merge_button = tk.Button(master, text="Fucionar Archivos", command=self.merge_files)
        self.merge_button.pack()

    def download_video(self):
        yt = YouTube(self.get_link())
        if self.video_quality.get() == '1080p':
            video_stream = yt.streams.filter(res=self.video_quality.get(), file_extension='webm').order_by('resolution').desc().first()
        else:
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4', res=self.video_quality.get()).order_by('resolution').desc().first()
        if video_stream is None:
            tk.messagebox.showerror('Error', 'No video stream found with selected quality.')
        else:
            video_stream.download(output_path=self.get_directory())


    def download_audio(self):
        yt = YouTube(self.get_link())
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
        audio_stream.download(output_path=self.get_directory())

    def merge_files(self):
        video_path = filedialog.askopenfilename(initialdir='/', title='Select Video File', filetypes= [('WEBM Files', '*.webm')])
        audio_path = filedialog.askopenfilename(initialdir='/', title='Select Audio File', filetypes= [('MP4 Files', '*.mp4')])
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        output_path = filedialog.asksaveasfilename(initialdir='/', title='Save File', filetypes=[('MP4 Files', '*.mp4')], defaultextension='.mp4')
        video_with_audio = video.set_audio(audio)
        video_with_audio.write_videofile(output_path)

    def get_link(self):
        link = tk.simpledialog.askstring('Link', 'Enter Youtube Link')
        return link

    def get_directory(self):
        directory = filedialog.askdirectory(initialdir='/', title='Select Directory')
        return directory

root = tk.Tk()
root.iconbitmap(r'./icon.ico')
my_downloader = YoutubeDownloader(root)
root.mainloop()
