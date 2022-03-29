import RPi.GPIO as GPIO

from time import sleep
import navigation as nav

class StopButton():
    __instance = None
    @staticmethod
    def getInstance():
        if StopButton.__instance == None:
            StopButton()
        return StopButton.__instance

    def button_callback(self,channel):
        self.move_bot.stop()
        sleep(1)
        
    def __init__(self):
        #self.move_bot = nav.Navigation()
    
        if StopButton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            StopButton.__instance=self
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(18,GPIO.RISING,callback=self.button_callback)
            
