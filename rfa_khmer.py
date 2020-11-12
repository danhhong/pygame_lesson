# -*- coding: utf-8 -*-
"""
@author: danhhong
"""
import re, urllib.request  # pip3 install urllib3
from pygame import mixer   # pip3 install pygame

# search mp3 file
mp3url = "http://www.rfa.org/khmer/audio/"
data = urllib.request.urlopen(mp3url).read()
data = data.decode("utf-8")
m = re.search("https://streamer1.rfaweb.org/stream/KHM/",data)

start = m.end()
end = m.end() + 22
mp3url = data[start:end]
url = "http://streamer1.rfaweb.org/stream/KHM/" + mp3url

# download mp3
mp3file = urllib.request.urlopen(url)
with open('rfaprogram.mp3','wb') as output:
  output.write(mp3file.read())
print("Download finished")

# play mp3 with pygame library
mixer.init()
mixer.music.load('rfaprogram.mp3')
mixer.music.play()
print ("Playing mp3...")
