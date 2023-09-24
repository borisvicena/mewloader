import os.path
import pytube.exceptions
from pytube import YouTube
import customtkinter
from termcolor import colored


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

gui = customtkinter.CTk()
gui.title("Mewloader - YouTube Link Downloader")
gui.geometry('500x720')


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


# MainText Creation - Mewloader
main_text = customtkinter.CTkLabel(master=gui, text="Mewloader", font=('Arial', 40, "bold"))
main_text.pack(fill='both', pady=20)

# Label Creation
label = customtkinter.CTkLabel(master=gui, text="YOUTUBE DOWNLOADER")
label.pack(pady=10)

# TextBox Creation
input_text = customtkinter.CTkEntry(master=gui, width=250)
input_text.focus_set()
input_text.pack(pady=10)

# Button for getting info from the given Youtube URL
get_info = customtkinter.CTkButton(master=gui, text='Get Info!', command=get_link_info)
get_info.pack(pady=10)

# Button for downloading audio MP3
download_mp3 = customtkinter.CTkButton(gui, text='Download MP3')
download_mp3.pack(pady=10)

# Button for downloading video MP4
download_mp4 = customtkinter.CTkButton(gui, text='Download MP4')
download_mp4.pack(pady=10)

# Label Creation
lbl = customtkinter.CTkLabel(gui, text="", font=("Arial", 20))
lbl.pack()

gui.mainloop()
