import RPi.GPIO as GPIO
import ButtonFrame
from time import sleep


class StopButton():
    __instance = None
    @staticmethod
    def getInstance():
        if StopButton.__instance == None:
            StopButton()
        return StopButton.__instance

    def button_callback(self,channel):
        ButtonFrame.pressStop()
        sleep(1)
    def __init__(self):
        if StopButton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            StopButton.__instance=self
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(18,GPIO.RISING,callback=self.button_callback)
            
