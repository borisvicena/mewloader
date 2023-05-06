import os.path
from tkinter import *
from tkinter import ttk
import tkinter
import pytube.exceptions
from pytube import YouTube
from termcolor import colored


gui = tkinter.Tk(className='\tMewloader - YouTube Link Downloader')
gui.geometry('500x720')
gui['bg'] = '#EFEFEF'

# MainText Creation - Mewloader
main_text = tkinter.Label(gui, text="Mewloader", bg='#EFEFEF', font=('Arial', 40))
main_text.pack(fill='both', pady=20)

# Label Creation
label = tkinter.Label(gui, text="YOUTUBE DOWNLOADER")
label.pack(pady=10)

# TextBox Creation
input_text = Entry(gui, width=50)
input_text.focus_set()
input_text.pack()

def download_youtube_mp3():
    global input_text
    string = input_text.get()
    lbl.configure(text=string)

    url = input_text.get()
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
        lbl.configure(text="Not valid URL")
        return

    lbl.configure(text="[-] Downloading...")
    audio_file = yt.streams.filter(only_audio=True).first().download()
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    lbl.configure(text="[+] Download completed successfully!")

# def download_video():
#     global input_text
#     string = input_text.get()
#     lbl.configure(text=string)

#     url = input_text.get()
#     try:
#         yt = YouTube(url)
#     except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
#         lbl.configure(text="Not valid URL")
#         return
    
#     lbl.configure(text="[-] Downloading...")
#     video_file = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
#     video_file.download()
#     lbl.configure(text="[+] Download completed successfully!")
    

# Button Creation
print_button = tkinter.Button(gui, text='Download', command=download_youtube_mp3)
print_button.pack()

# Label Creation
lbl = tkinter.Label(gui, text="")
lbl.pack()


# video_info = {
#     "title": yt.title,
#     "views": yt.views,
#     "length": yt.length,
#     "rating": yt.rating
# }
#

gui.mainloop()
