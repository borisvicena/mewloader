from tkinter import *
from tkinter import ttk
import tkinter
import pytube.exceptions
from pytube import YouTube
from termcolor import colored

gui = tkinter.Tk(className='\tMewloader - YouTube Link Downloader')
gui.geometry('1280x720')
gui['bg'] = '#A682FF'

# MainText Creation - Mewloader
main_text = tkinter.Label(gui, text="Mewloader", bg='#A682FF', font=('Arial', 25))
main_text.pack(fill='both', pady=20)

# TextBox Creation
input_text = Entry(gui, width=50)
input_text.focus_set()
input_text.pack()
# yt = YouTube()


def print_input():
    global input_text
    string = input_text.get()
    lbl.configure(text=string)


# Button Creation
print_button = tkinter.Button(gui, text='Download link', command=print_input)
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
# def download_youtube_mp4():
#     '''
#     Function: Downloads a mp4 file from a given YouTube URL
#     '''
#     print('[-] Downloading...')
#     video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     video_file.download()
#     print(colored('[+] Download completed successfully!', 'green'))


gui.mainloop()
