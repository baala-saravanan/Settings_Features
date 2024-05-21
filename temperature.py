#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import vlc
import time
from pydub import AudioSegment
import sys
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA
play_machine_voice = GTTSA()

THERMAL_PATH = '/sys/devices/virtual/thermal/'


def get_thermal_zone_paths():
    return [os.path.join(THERMAL_PATH, d) for d in os.listdir(THERMAL_PATH) if 'thermal_zone' in d]

def read_sys_value(pth):
    with open(pth, 'r') as file:
        return file.read().strip()

def get_thermal_zone_temps(zone_paths):
    return [int(read_sys_value(os.path.join(p, 'temp'))) for p in zone_paths]

def main():
    zone_paths = get_thermal_zone_paths()
    zone_temps = get_thermal_zone_temps(zone_paths)
    
    temperature = zone_temps[0] / 1000
    if temperature > 110:
        temperature = 110
        play_machine_voice.play_machine_audio("off_the_device.mp3")
        
    print(f"HearSight Device Temperature {temperature:.1f} Degree Celsius")
    
    temp_tens = int(temperature // 10) * 10
    temp_ones = int(temperature % 10)
    
    temp = "HearSight Device Temperature.mp3"
    play_machine_voice.play_machine_audio(temp)
    tempF = int(temperature)
    temp_tens_audio = f"number_{tempF}.mp3" 
    play_machine_voice.play_machine_audio(temp_tens_audio)
    
#    temp_ones_audio = f"number_{temp_ones}.mp3" 
#    play_machine_voice.play_machine_audio(temp_ones_audio))    
    
    tempS = f"{temperature:.1f}"
    decimal = str(tempS)[-1]
    if decimal != "0":
        play_machine_voice.play_machine_audio("period.mp3")
        decimal_audio = f"number_{decimal}.mp3"
        play_machine_voice.play_machine_audio(decimal_audio)
    else:
        pass
    
    celsius =  "degree_celsius.mp3"
    play_machine_voice.play_machine_audio(celsius)

if __name__ == "__main__":
    main()
