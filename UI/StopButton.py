import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

		
class StopButton():
    def __init__(self):
		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
		GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
	
    def listenButton(self):
        text = None
        with BUTTON as source:
            try:
				if GPIO.input(10) == GPIO.HIGH:
					command = 1
            except Exception as e:
				print("Error")

        return command

if __name__ == "__main__":
    buttonpress = StopButton()
    text = buttonpress.listenButton()