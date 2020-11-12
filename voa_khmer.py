# -*- coding: utf-8 -*-
"""
@author: danhhong
"""
import re, urllib.request  # pip3 install urllib3
from pygame import mixer   # pip3 install pygame

# search mp3 file
mp3url = "https://khmer.voanews.com/embed/player/0/5639504.html?type=audio"
data = urllib.request.urlopen(mp3url).read()
data = data.decode("utf-8")
m = re.search("https://av.voanews.com/clips/VKH/",data)

start = m.end()
end = m.end() + 54
mp3url = data[start:end]
url = "https://av.voanews.com/clips/VKH/" + mp3url

# download mp3
mp3file = urllib.request.urlopen(url)
with open('voaprogram.mp3','wb') as output:
  output.write(mp3file.read())
print("Download finished")

# play mp3 with pygame library
mixer.init()
mixer.music.load('voaprogram.mp3')
mixer.music.play()
print ("Playing mp3...")
