# Importing Libraries 
import serial 
import time 

arduino = serial.Serial(port='COM6', baudrate=9600, timeout=1) 

def write_read(x : str): 
	bytestr = bytes(x, 'utf-8')
	arduino.write(bytestr) 
	data = arduino.readline() 
	return data 

time.sleep(5) # wait until device is setup
while True: 
	num = input("Enter a number: ") # Taking input from user 
	value = write_read(num) 
	print(value.decode().strip()) # printing the value (decode bytes first, strip off the ctrl+lf println returns)


