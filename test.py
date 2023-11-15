import os
from yt_dlp import YoutubeDL
def download_url(path,URL):
    option = {
        "outtmpl":f"{path}"+"%(title)s.%(ext)s"
    }#パスは実行する環境に合わせて
    URLs=[]
    ydl = YoutubeDL(option)
    URLs.append(URL)
    result = ydl.download(URLs)
    return f"{path}"+"%(title)s.%(ext)s"

download_url(os.getcwd(),f"https://www.youtube.com/watch?v=WEYCz553Sto&ab_channel=S2P%5BThaiLyrics%5D%3Ainfinity")
