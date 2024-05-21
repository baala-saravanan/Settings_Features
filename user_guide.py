import os
import vlc
import time
from pydub import AudioSegment
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from config import *
from play_audio import GTTSA

play_file = GTTSA()

def get_audio_duration(self, filename):
    audio = AudioSegment.from_file(filename)
    duration_in_seconds = len(audio) / 1000  # Convert milliseconds to seconds
    return duration_in_seconds

def play_audio():
#    with open(LANG_FILE,'r') as file:
#        language = file.read()       
#    print(language)
    
#    if language == 'English':
    play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/English.mp3")
        
#    elif language == 'Hindi':
#        play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/Hindi.mp3")
#        
#    elif language == 'Kannada':
#        play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/Kannada.mp3")
#        
#    elif language == 'Malayalam':
#        play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/Malayalam.mp3")
#        
#    elif language == 'Tamil':
#        play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/Tamil.mp3")
#        
#    else:
#        play_file.play_audio_file("/home/rock/Desktop/Hearsight/English/user_guide/Telugu.mp3")
            
play_audio()       
