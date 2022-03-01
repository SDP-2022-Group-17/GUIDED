import speech_recognition as sr

class Speech(sr.Recognizer):
    def __init__(self):

        super().__init__()

        # self.energy_threshold = 100
        # self.pause_threshold = 100000

        # print("Energy threshold: {}".format(self.energy_threshold))
        # print("Pause threshold: {}".format(self.pause_threshold))

    """
    Using a Microphone for audio input
    """
    def listenMicrophone(self):
        text = None
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source)
            print("Please say something:")
            try:
                audio = self.listen(source, timeout=0.8)
                text = self.recognize_google(audio)
                print("You said: \n" + text)
            except sr.WaitTimeoutError as e:
                print(e)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

        # # write audio to a WAV file
        # with open("speech.wav", "wb") as f:
        #     f.write(audio.get_wav_data())
        #
        # text = None
        # try:
        #
        # except sr.UnknownValueError:
        #     print("Google Speech Recognition could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return text

    """
    Using audio files (.wav) for input
    """
    def listenAudioFile(filepath):
        # Test files: tests_english; connor_social; male
        audio_file = sr.AudioFile(filepath)

        with audio_file as source:
            # This cuts out the first second or so for some reason
            # r.adjust_for_ambient_noise(source)
            audio = r.record(source)

        try:
            text = r.recognize_google(audio)
            print("You said: \n" + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    speech_recognition = Speech()
    text = speech_recognition.listenMicrophone()
