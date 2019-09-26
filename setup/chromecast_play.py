#!/usr/bin/python3
# Usage: chromecast_play.py <ip> <language> <what to say>
import sys
import pychromecast
import os
import os.path
from gtts import gTTS
import time
import hashlib

# file to create and play 
audio_output = "audio_output.mp3"
#web port to expose
port = "8081"
# get ip of the chromecast device
ip = sys.argv[1]
# get the language
lang = sys.argv[2]
# get what to say
say = sys.argv[3]

# retrieve local ip
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip=s.getsockname()[0]
s.close()

# connect to the chromecast device
castdevice = pychromecast.Chromecast(ip)
castdevice.wait()

# create the audio file
tts = gTTS(say, lang=lang)
tts.save("/var/www/html/"+audio_output)

# ask the device to play the file
mc = castdevice.media_controller
mc.play_media("http://"+local_ip+":"+port+"/"+audio_output, "audio/mp3")
mc.block_until_active()
mc.pause()
time.sleep(1)
mc.play()
while not mc.status.player_is_idle:
   time.sleep(0.5)
mc.stop()
castdevice.quit_app()

# delete the file
os.remove("/var/www/html/"+audio_output)