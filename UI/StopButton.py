import RPi.GPIO as GPIO



class StopButton():
  def __init__(self):
    super().__init__()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  def button_callback(channel):
      # talk to ROS??
      print("Stop button pressed.")

  def button_event():
      GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
