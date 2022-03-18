# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

labels = {"start": "Where do you want to go?",
          "end": "Going to: Room A.",
          "travel": "You have arrived at your destination."}

for i in ["start", "travel", "end"]:
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    print(labels[i])
    myobj = gTTS(text=labels[i], slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(i+".mp3")

    # Playing the converted file
    os.system("start " + i + ".mp3")
