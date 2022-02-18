import speech_recognition as sr

r = sr.Recognizer()

# r.energy_threshold = 0
# r.pause_threshold = 100000

print("Energy threshold: {}".format(r.energy_threshold))
print("Pause threshold: {}".format(r.pause_threshold))

##############################################################################

"""
Using audio files (.wav) for input
"""
# # Test files: tests_english; connor_social; male
# audio_file = sr.AudioFile(r"C:\Users\tzesh\Desktop\speech3.wav")
#
# with audio_file as source:
#     # This cuts out the first second or so for some reason
#     # r.adjust_for_ambient_noise(source)
#     audio = r.record(source)

##############################################################################

"""
Using a Microphone for audio input
"""
with sr.Microphone() as source:
    # r.adjust_for_ambient_noise(source)
    print("Please say something:")
    audio = r.listen(source)

##############################################################################

# write audio to a WAV file
with open("speech2.wav", "wb") as f:
    f.write(audio.get_wav_data())

try:
    text = r.recognize_google(audio)
    print("You said: \n" + text)
except:
    print("Sorry I didn't understand you.")
