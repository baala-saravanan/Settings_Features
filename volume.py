import subprocess
import sys
import gpio as GPIO
import pyttsx3
from pydub import AudioSegment
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA

play_audio = GTTSA()
engine = pyttsx3.init()

# Define GPIO pins
PIN_INCREASE = 450
PIN_DECREASE = 421
PIN_EXIT = 448

# Set up GPIO
GPIO.setup(PIN_INCREASE, GPIO.IN)
GPIO.setup(PIN_DECREASE, GPIO.IN)
GPIO.setup(PIN_EXIT, GPIO.IN)

play_audio.play_machine_audio("press your feature button now.mp3")

# Function to increase volume
def increase_volume():
    subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
    volume_percentage = get_volume_percentage()
    say_volume_percentage(volume_percentage)

# Function to decrease volume
def decrease_volume():
    subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "5%-"])
    volume_percentage = get_volume_percentage()
    say_volume_percentage(volume_percentage)

# Function to get current volume percentage
def get_volume_percentage():
    result = subprocess.run(["amixer", "get", "Master"], capture_output=True, text=True)
    output = result.stdout
    # Parse the output to get the volume percentage
    start_index = output.find("[") + 1
    end_index = output.find("%]")
    volume_percentage = output[start_index:end_index]
    return volume_percentage

# Function to make the program say the volume percentage
def say_volume_percentage(volume_percentage):
#    engine.setProperty('voice', 'english_rp+f3')
#    engine.setProperty('rate', 200)
    engine.setProperty('voice', 'en-gb')
    engine.setProperty('rate', 140)
    if volume_percentage == '100':
        engine.say("Maximum volume" + volume_percentage + " percent")
    else:
        engine.say(volume_percentage + " percent")
    engine.runAndWait()

# Main loop
while True:
    if GPIO.input(PIN_INCREASE):
        increase_volume()
    elif GPIO.input(PIN_DECREASE):
        decrease_volume()
    elif GPIO.input(PIN_EXIT):
        play_audio.play_machine_audio("feature_exited.mp3")
        sys.exit()
