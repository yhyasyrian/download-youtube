import re
from pytube import YouTube
# https://youtu.be/p_bGaIKej_Q
url = input("Enter Your Url YouTube For Download:")
type = input("Enter Type File For Download video/audio:")
Quality = ['144p','240p','360p','480p','720p','1080p']
QualityVideo = []
PATH = "/data/data/com.termux/files/home/storage/shared/video"
def end():
  print("Finsh Download Video")
if(type.lower() == "video"):
  video = YouTube(url)
  for result in video.streams.filter(progressive=True):
    for i in Quality:
      search = re.search(i,str(result))
      if search != None:
        QualityVideo.append(i)
        break
  p = input("Enter Your The Quality "+  '|'.join(QualityVideo) +":")
  if p == '144p':
    size = 1.9
  elif p == '240p':
    size = 2.7
  elif p == "360p":
    size = 4.4
  elif p == "480p":
    size = 7.7
  elif p == "720p":
    size = 14.5
  elif p == "1080p":
    size = 27.61
  sizeVideo = (video.length / 60) * size
  print("Download Video Size Is : "+ str(sizeVideo))
  video.streams.filter(progressive=True,res=p).order_by('resolution').desc().first().download(output_path=PATH)
  video.register_on_complete_callback(end())
