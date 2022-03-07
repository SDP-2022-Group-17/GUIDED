import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

class StopButton():
  def __init__(self):
    super().__init__()
  
  def listenButton():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
    text = None
    try:
      if GPIO.input(inpin) == 0:
        text = 1
        print("please")
    except Exception as e:
      print(e)

    GPIO.cleanup()

  def button_callback(channel):
    print("Button was pushed!")

if __name__ == "__main__":
  speech_recognition = Speech()
  text = speech_recognition.listenMicrophone()