# YouTube Downloader App
import os.path

import pytube.exceptions
from pytube import YouTube
from termcolor import colored
import display_banner


display_banner.display_mewloader_banner()


while True:
    try:
        get_link = input("[*] Enter a valid youtube link: ")
        yt = YouTube(get_link)
        break
    except pytube.exceptions.RegexMatchError:
        print("[!] Please enter a valid youtube link")
        continue

video_info = {
    "title": yt.title,
    "views": yt.views,
    "length": yt.length,
    "rating": yt.rating
}


def get_video_info(title, views, length, rating):
    print('---------------------------------')
    print(colored("[+] Title: ", 'blue'), title)
    print(colored("[+] Number of views: ", 'blue'), views)
    print(colored("[+] Length of the video: ", 'blue'), length, 'seconds')
    print(colored("[+] Rating: ", 'blue'), rating)
    print('---------------------------------')


get_video_info(video_info['title'], video_info['views'], video_info['length'], video_info['rating'])


def download_youtube_mp3():
    '''
    Function: Downloads a mp3 file from a given YouTube URL
    '''
    print('[-] Downloading...')
    audio_file = yt.streams.filter(only_audio=True).first().download()
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    print(colored('[+] Download completed successfully!', 'green'))


def download_youtube_mp4():
    '''
    Function: Downloads a mp4 file from a given YouTube URL
    '''
    print('[-] Downloading...')
    video_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_file.download()
    print(colored('[+] Download completed successfully!', 'green'))


while True:
    user_choice = int(input("[*] Choose 0 for mp3 or 1 for mp4: "))
    try:
        match user_choice:
            case 0:
                download_youtube_mp3()
            case 1:
                download_youtube_mp4()
        break
    except ValueError or user_choice != 0 or 1:
        print("[!] Enter a number")
        continue


# Credentials
# Boris Vícena


# !!! Program an application that sends sms
# !!! Program an application that sends email from a random email address
