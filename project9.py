#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio
import pygame
from pygame import mixer
import time
intial = time.time()
# Starting the mixer
mixer.init()
# Loading the song
song1=mixer.music.load("song2.mp3")
# song2=mixer.music.load("song2.mp3")

# Setting the volume
mixer.music.set_volume(1)

# Start playing the song
for i in range(4):
# infinite loopwhile (i<4):
    time.sleep(30)
    mixer.music.play()
    a=input(" ")
    if a == 'done':
        mixer.music.stop()
    curr = time.ctime()
    f=open("Record.txt","a")
    f.write(f"I have take the medicine at {curr}\n ")
    f.close()
	    # print("Press 'p' to pause, 'r' to resume")
	    # print("Press 'e' to exit the program")
	    # query = input(" ")
	
	    # if query == 'p':

		# # Pausing the music
		#     mixer.music.pause()	
	    # elif query == 'r':

		# # Resuming the music
		#     mixer.music.unpause()
	    # elif query == 'e':

		# # Stop the mixer
		#     mixer.music.stop()
		#     break
        
