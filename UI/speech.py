import speech_recognition as sr

class Speech(sr.Recognizer):
    def __init__(self):

        super().__init__()
        
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index,name))

        self.energy_threshold = 6000
        self.dynamic_energy_threshold = False 
        # self.pause_threshold = 100000

        # print("Energy threshold: {}".format(self.energy_threshold))
        # print("Pause threshold: {}".format(self.pause_threshold))

    """
    Using a Microphone for audio input
    """
    def listenMicrophone(self):
        text = None
        #mic = sr.Microphone(device_index=1)
        r = sr.Recognizer()
        
        #sr.Recognizer.dynamic_energy_threshold = 
        with sr.Microphone() as source:
            r.dynamic_energy_threshold = False 
            r.energy_threshold =10000000
            # r.adjust_for_ambient_noise(source)
            print("Please say something:")
            try:
                audio = self.listen(source, timeout=0.2)
                print("LISTENED")
                text = self.recognize_google(audio)
                print("You said: \n" + text)
            except sr.WaitTimeoutError as e:
                print(e)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        # write audio to a WAV file
        # with open("speech.wav", "wb") as f:
        #     f.write(audio.get_wav_data())
      
        return text

if __name__ == "__main__":
    speech_recognition = Speech()
    
    text = speech_recognition.listenMicrophone()
