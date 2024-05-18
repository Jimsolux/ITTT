# Importing Libraries 
import serial 
import time 

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1) 

def write_read(x : str): 
	bytestr = bytes(x, 'utf-8')
	arduino.write(bytestr) 
	data = arduino.readline() 
	return data 

if __name__ == "__main__": # enables us to import the function but not run the main code, as well as running the main code when we want to test. see https://stackoverflow.com/questions/419163/what-does-if-name-main-do
	time.sleep(5) # wait until device is setup
	while True: 
		num = input("Enter a number: ") # Taking input from user 
		value = write_read(num) 
		print(value.decode().strip()) # printing the value (decode bytes first, strip off the ctrl+lf println returns)


