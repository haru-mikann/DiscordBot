import discord
from yt_dlp import YoutubeDL
import os

print('getcwd:', os.getcwd())

def download_url(path,URL):
    option = {
        "outtmpl":f"{path}"+"%(title)s.%(ext)s"
    }#パスは実行する環境に合わせて
    URLs=[]
    ydl = YoutubeDL(option)
    URLs.append(URL)
    result = ydl.download(URLs)
    return f"{path}"+"%(title)s.%(ext)s"


TOKEN = "MTE3NDIwNjIxODE3NzM2Mzk4OA.G6K7Mm.b0mia5BRuhGSerB1mSpXP-JeIMJTvYQmsmQcl0"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(":download"):
        file_path = download_url(os.getcwd(),str(message.content).strip(":download"))
        await message.channel.send(message.content)
        # await message.channel.send(file=discord.File(file_path,filename="youtubeDL.mp4"))

client.run(TOKEN)