import speech_recognition as sr

class Speech(sr.Recognizer):
    def __init__(self):

        super().__init__()

        # for index, name in enumerate(sr.Microphone.list_microphone_names()):
            # print("Microphone with name \"{1}\" found for 'Microphone(device_index={0})'".format(index,name))

        self.energy_threshold = 20000
        self.dynamic_energy_threshold = False

        # self.pause_threshold = 100000

        self.microphone = sr.Microphone()
        with self.microphone as source:
            self.adjust_for_ambient_noise(source, duration = 10)

    """
    Using a Microphone for audio input
    """
    def listenMicrophone(self):
        text = None
        with self.microphone as source:
            print("Please say something:")
            try:
                audio = self.listen(source, timeout=1, phrase_time_limit=10)
                print("LISTENED")
                text = self.recognize_google(audio)
                print("You said: " + text)
            except sr.WaitTimeoutError as e:
                print(e)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
                return "_"
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return text

if __name__ == "__main__":
    speech_recognition = Speech()
    # print("Energy threshold: {}".format(speech_recognition.energy_threshold))
    # print("Pause threshold: {}".format(speech_recognition.pause_threshold))
    while True:
        speech_recognition.listenMicrophone()
