import serial
import sys
import signal
import string

arduinoData = serial.Serial('com7', 9600)

def SendToArduino(inputt) :
    cmd = inputt
    print(inputt)
    str(cmd)
    cmd = cmd + '\r'
    arduinoData.write(cmd.encode())


