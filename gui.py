import os.path
from pytube import YouTube, exceptions
import customtkinter as ctk
import tkinter as tk


# https://www.youtube.com/watch?v=vZgitU13LLI


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App Frame
        self.title("Mewloader - YouTube Downloader")
        self.geometry("720x480")
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)


        # UI Elements
        self.title = ctk.CTkLabel(self, text='Insert a youtube link')
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        # Link input
        url = tk.StringVar()
        self.link = ctk.CTkEntry(self, width=350, height=20, textvariable=url)
        self.link.grid(row=1, column=0, padx=10, pady=10)

        # Download button 
        self.download = ctk.CTkButton(self, text='Download', command=self.startDownload)
        self.download.grid(row=2, column=0, padx=10, pady=(10, 0))

    
    def button_callback(self):
        print('button pressed')

    def startDownload(self):
        try:
            yt_link = self.link.get()
            yt = YouTube(yt_link, use_oauth=True, allow_oauth_cache=True)
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

            if video:
                video.download()
                print("Downloaded!")
            else:
                print("No suitable video stream found!")
        except Exception as e:
            print("Error downloading: ", str(e))


# def download_audio():
#     global input_text
#     string = input_text.get()
#     lbl.configure(text=string)

#     url = input_text.get()
#     try:
#         yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
#     except (exceptions.RegexMatchError, exceptions.VideoUnavailable):
#         lbl.configure(text="Not valid URL")
#         return

#     lbl.configure(text="[-] Downloading audio...")
#     audio_file = yt.streams.filter(only_audio=True).first().download()
#     base, ext = os.path.splitext(audio_file)
#     new_file = base + '.mp3'
#     os.rename(audio_file, new_file)
#     lbl.configure(text="[+] Audio download completed successfully!")

# def download_video():
#     global input_text
#     string = input_text.get()
#     lbl.configure(text=string)

#     url = input_text.get()
#     try:
#         yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

#     except (exceptions.RegexMatchError, exceptions.VideoUnavailable):
#         lbl.configure(text="Not valid URL")
#         return
    
#     lbl.configure(text="[-] Downloading video...")
#     video_file = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
#     video_file.download()
#     lbl.configure(text="[+] Video download completed successfully!")

# def get_link_info():
#     global input_text
#     string = input_text.get()
#     lbl.configure(text=string)

#     url = input_text.get()
#     try:
#         yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
#     except (exceptions.RegexMatchError, exceptions.VideoUnavailable):
#         lbl.configure(text="Not valid URL")
#         return
    
#     lbl.configure(yt.title)



# Run app
app = App()
app.mainloop()
