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
main_text = tkinter.Label(gui, text="Mewloader", bg='#EFEFEF', font=('Arial', 40, "bold"))
main_text.pack(fill='both', pady=20)

# Label Creation
label = tkinter.Label(gui, text="YOUTUBE DOWNLOADER")
label.pack(pady=10)

# TextBox Creation
input_text = Entry(gui, width=50)
input_text.focus_set()
input_text.pack()

def download_audio():
    global input_text
    string = input_text.get()
    lbl.configure(text=string)

    url = input_text.get()
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
        lbl.configure(text="Not valid URL")
        return

    lbl.configure(text="[-] Downloading audio...")
    audio_file = yt.streams.filter(only_audio=True).first().download()
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    lbl.configure(text="[+] Audio download completed successfully!")

def download_video():
    global input_text
    string = input_text.get()
    lbl.configure(text=string)

    url = input_text.get()
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
        lbl.configure(text="Not valid URL")
        return
    
    lbl.configure(text="[-] Downloading video...")
    video_file = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    video_file.download()
    lbl.configure(text="[+] Video download completed successfully!")

def get_link_info():
    global input_text
    string = input_text.get()
    lbl.configure(text=string)

    url = input_text.get()
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    except (pytube.exceptions.RegexMatchError, pytube.exceptions.VideoUnavailable):
        lbl.configure(text="Not valid URL")
        return
    
    lbl.configure(text="Title: " + yt.title)


    
# Button for getting info from the given Youtube URL
get_info = tkinter.Button(gui, text='Get Info!', command=get_link_info)
get_info.pack()

# Button for downloading audio MP3
download_mp3 = tkinter.Button(gui, text='Download MP3', command=download_audio)
download_mp3.pack()

# Button for downloading video MP4
download_mp4 = tkinter.Button(gui, text='Download MP4', command=download_video)
download_mp4.pack()

# Label Creation
lbl = tkinter.Label(gui, text="", font=("Arial", 20))
lbl.pack()

gui.mainloop()
