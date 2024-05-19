# Importing Libraries 
import serial 
import time 

class ArduinoComm:
	def __init__(self):
		self.arduinoSerial = serial.Serial('com6', 9600, timeout=1) #opens comport
		time.sleep(5) # wait until device is setup 
		print("arduino comms set up!")

	def write_read (self, x : str): 
		bytestr = bytes(x, 'utf-8')
		self.arduinoSerial.write(bytestr) 
		data = self.arduinoSerial.readline() 
		return data.decode().strip()

if __name__ == "__main__": # enables us to import the function but not run the main code, as well as running the main code when we want to test. see https://stackoverflow.com/questions/419163/what-does-if-name-main-do
	arduino = ArduinoComm()
	while True: 
		num = input("Enter a number: ") # Taking input from user 
		value = arduino.write_read(num) 
		print(value) # printing the value (decode bytes first, strip off the ctrl+lf println returns)


