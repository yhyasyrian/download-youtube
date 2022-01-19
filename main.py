import re
from pytube import CaptionQuery, Playlist, Stream, YouTube 
import os, sys, shutil
# Start Function For progressive
def display_progress_bar(bytes_received: int, filesize: int, ch: str = "█", scale: float = 0.55) -> None:
  columns = shutil.get_terminal_size().columns
  max_width = int(columns * scale)
  filled = int(round(max_width * bytes_received / float(filesize)))
  remaining = max_width - filled
  progress_bar = ch * filled + " " * remaining
  percent = round(100.0 * bytes_received / float(filesize), 1)
  text = f" ↳ |{progress_bar}| {percent}%\r"
  sys.stdout.write(text)
  sys.stdout.flush()
def on_progress(stream: Stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)

# https://youtu.be/p_bGaIKej_Q
url = input("Enter Your Url YouTube For Download:")
type = input("Enter Type File For Download video/audio:")
Quality = ['144p','240p','360p','480p','720p','1080p']
QualityVideo = []
PATH = "/data/data/com.termux/files/home/storage/shared/video"
def end():
  print("\nFinsh Download Video")
if(type.lower() == "video"):
  video = YouTube(url)
  for result in video.streams.filter(progressive=True):
    for i in Quality:
      search = re.search(i,str(result))
      if search != None:
        QualityVideo.append(i)
        break
  p = input("Enter Your The Quality "+  '|'.join(QualityVideo) +":")
  size = video.streams.filter(progressive=True,res=p).order_by('resolution').desc().first().filesize / 1000000
  print("Download Video Size Is : "+ str(round(size,1)) +"MG")
  video.register_on_progress_callback(on_progress)
  video.streams.filter(progressive=True,res=p).order_by('resolution').desc().first().download(output_path=PATH)
  video.register_on_complete_callback(end())
#end 