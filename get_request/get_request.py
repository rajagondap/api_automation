# Import the required libraries
from gtts import gTTS
import os

# Open the text file and read the content
with open('input.txt', 'r') as file:
    text = file.read().replace('\n', '')

# Create a text-to-speech object
tts = gTTS(text)

# Save the output as an mp3 file
tts.save('output.mp3')

# Play the output file
os.system('start output.mp3')