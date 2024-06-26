import time
import re
from selenium import webdriver
import codecs
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import serial # Arduino Reference
#import pyserial

import sys
import signal
import keyboard

#Selenium estabishment - driver is used, browser is unused.
browser = webdriver.Chrome()

cService = webdriver.ChromeService(executable_path="C:/Users/jimco/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = cService)
fakeValue = 0
oldFinalAnswer = 0

def SendValueToArduino(value) :
    time.sleep(1) # waits 1 second to establish comport connect.
    #print(str(value) + " is my float input value. (arduinosendfunction)")
    cmd = value
    cmd = str(cmd)
    cmd = cmd + '\r'
    print(cmd)
    arduinoData.write(cmd.encode())

    #arduinoData.close()

def ChangeValueToState(value) :
    hitIndex = 0
    if value >= 0:
        hitIndex = 0    # No hit
    elif value < 0 and value > -2:
        hitIndex = 1    # Hit 1
    elif value <= -2 and value > -4:
        hitIndex = 2    # Hit 2
    elif value <= -4 and value > -8:
        hitIndex = 3    # hit 3
    elif value <= -8 and value > -12:
        hitIndex = 4    # hit 4
    elif value <= -12:
        hitIndex = 5    # hit 5

    SendValueToArduino(hitIndex)



def time_counter(seconds):
    starttime = time.time()
    while True:
        now = time.time()
        if now > starttime + seconds:
            break
        yield now - starttime

    for t in time_counter(20):
        kb()
        time.sleep(.001)


oldAmountOfMoves = 0 #Establish that 0 moves have been made initially, before it checks.
def SeeIfMoveWasMade():
    global oldAmountOfMoves
    html = driver.page_source
    preString = 'data-whole-move-number='
    preStringLength = len(preString)

    amountOfIndexes = Find_All(html, preString) #finds instances
    if oldAmountOfMoves < amountOfIndexes:
        time.sleep(1)
        ReceiveAndPrintValue()
        oldAmountOfMoves = amountOfIndexes

def Find_All(a_str, sub):
    subs = [m.start() for m in re.finditer(sub, a_str)]
    total = len(subs)
    return total


def ReceiveAndPrintValue() :
    htmlString = driver.page_source #Source string, entire webpage
    preString = '<span class="evaluation-bar-score evaluation-bar-dark ">' #Pre String to be sought
    preStringNeg = '<span class="evaluation-bar-score evaluation-bar-light ">' #Pre String if value turns negative
    stringIndexNeg = htmlString.find(preStringNeg) + len(preStringNeg) #index of the negative prestring
    stringIndex = htmlString.find(preString) + len(preString) #The Index is the prestringIndex + the length of the preString.
    int(stringIndex) # stringIndex is now an int
    int(stringIndexNeg) #stringIndexNeg is now an int
    answerStringPos = ""
    answerStringNeg = ""
    if stringIndex != 0 and stringIndex != len(preString) :        # Positive score, calculates pos answer and neg posanswer = 0
        for i in range(stringIndex, stringIndex + 6):
            if htmlString[i] == "+":
                continue
                #answerStringPos += htmlString[i]
            elif htmlString[i] == "-":
                continue
                #answerStringPos += htmlString[i]
            elif htmlString[i] == ".":
                answerStringPos += htmlString[i]
            elif htmlString[i].isnumeric():
                answerStringPos += htmlString[i]
            elif htmlString[i] == "<":
                #print(answerStringPos + " Is Pos")
                #print("Triggered 1")
                answerStringNeg = "0"
                PrintFinalValue(answerStringPos, answerStringNeg)
                break
            elif htmlString[i].isalpha():
                #print(answerStringPos + " Is Pos")
                #print("Triggered 2")
                answerStringNeg = "0"
                PrintFinalValue(answerStringPos, answerStringNeg)
                break
            # print(htmlString[i])
        answerStringNeg = "0" #resets neg (might be not needed.
        # End Positive Reading of value
    if stringIndexNeg != "0" and stringIndexNeg != len(preStringNeg) :     # Negative score, calculates the answer and pos answer = 0
        for i in range(stringIndexNeg, stringIndexNeg + 6):
            if htmlString[i] == "+":
                continue
                #answerStringNeg += htmlString[i]
            elif htmlString[i] == "-":
                continue
                #answerStringNeg += htmlString[i]
            elif htmlString[i] == ".":
                answerStringNeg += htmlString[i]
            elif htmlString[i].isnumeric():
                answerStringNeg += htmlString[i]
            elif htmlString[i] == "<":
                #print(answerStringNeg+ " Is Neg val")
                #print("Triggered 3")
                answerStringPos = "0"
                PrintFinalValue(answerStringPos, answerStringNeg)
                break
            elif htmlString[i].isalpha():
                #print(answerStringNeg+ " Is Neg val")
                #print("Triggered 4")
                #print(stringIndexNeg)
                answerStringPos = "0"
                PrintFinalValue( answerStringPos, answerStringNeg)
                break
        answerStringPos = "0" #resets pos
        #End Negative Reading of value


def ArduinoTestInput() :
    global fakeValue
    print("Testing Arduino with fake input")
    SendValueToArduino(fakeValue)
    fakeValue += 1

def SleepAndReset():
    global oldFinalAnswer
    global oldAmountOfMoves
    oldAmountOfMoves= 0
    print("Sleeping... For 1 minute!")
    oldFinalAnswer = 0
    time.sleep(30)

def PrintFinalValue(posScore, negScore):
    FinalAnswer = 0.0
    global oldFinalAnswer
    try :
        posScore = float(posScore) # parses pos score to a float
        negScore = float(negScore) # parses neg score to a float
        negScore *= -1  #actually makes neg a negative value
        FinalAnswer = posScore + negScore
        if FinalAnswer != 0.0:
            if FinalAnswer < oldFinalAnswer :   # only sends negative values under -2
                print("Final Answer Below")
                str(FinalAnswer)
                #ChangeValueToState(FinalAnswer)
                SendValueToArduino(FinalAnswer)
        oldFinalAnswer = FinalAnswer # stores old final answer
    except Exception as error:
        print("Empty Final Answer recorded")

def checkInput():
    if keyboard.is_pressed("q"):
        ArduinoTestInput()
        time.sleep(.5)
    if keyboard.is_pressed("p"): #Starts Reading out the values and sending it away.
            ReceiveAndPrintValue()
            time.sleep(.5)
            for t in time_counter(1200):
                SeeIfMoveWasMade()
                print("Seen if movewasmade, sleep 2 secs.")
                if keyboard.is_pressed("p"):
                    SleepAndReset()
                time.sleep(2)

def RunProgramme() :
    #Start Web
    driver.get('https://www.chess.com/')
    driver.maximize_window()

    # check input for 20 min
    for t in time_counter(1200):
        checkInput()
        #print(t)
        time.sleep(.001)


# Actual run commands -----------------------------------------

# CONTACT WITH COMPORT - CONNECTION ESTABLISHED WITH ARDUINO
#arduinoData = serial.Serial('com6', 9600)

#arduinoData.open()
    arduinoData = serial.Serial('com6', 9600) #opens comport

# ---------
RunProgramme()

print("Ending programme")
# --------------------
# End run
