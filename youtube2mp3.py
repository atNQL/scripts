import youtube_dl
import sys
import shutil
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False,
}

if __name__ == "__main__":


    # for file in os.listdir('.'):
    #     if file.endswith('mp3'):
    #         shutil.move(file, "youtube_download/"+file)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = ['https://www.youtube.com/watch?v=y_6aSG2yfe8']
        ydl.download(filenames)
