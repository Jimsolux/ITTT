#include <Servo.h>

String myCmd;
Servo myservo;  // create servo object to control a servo
int startpos = 1;
int endpos = 100;
int pos = startpos;    // variable to store the servo position
int format = 1;

/**
 * blink amt_of_blinks times
*/
void blink(int amt_of_blinks)
{
  for (int i = 0; i < amt_of_blinks; i++) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
  }
}

/**
 * function to retract and smash the hammer
*/
void hammerfall()
{
  for (pos = endpos; pos >= startpos; pos -= 2) { //mf
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(10);                       // waits 15 ms for the servo to reach the position
  }
  delay(1000);  // 1 sec wait

  for (pos = startpos; pos <= endpos; pos += 1) { // goes from 0 degrees to 180 degrees
  // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(10);  
   }
  delay(1000);
}

/**
 * setup
*/
void setup() {
  myservo.attach(9);               // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);              // Listens on com-port
  Serial.setTimeout(10); 
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);  // Turns the test LED off initially.
  blink(5);                        // let us know it's set up
  myservo.write(endpos);
  hammerfall();
}

/**
 * check for incoming values on the usb
 * if values available < 0, then smash player
*/
void loop() {
  if (Serial.available() > 0) { //Check values of Comport serial
    myCmd = Serial.readString();
    float arduinoValue = myCmd.toFloat();
    Serial.println(arduinoValue, format); // send back confirmation over usb
    Serial.flush();

    if(arduinoValue < 0) { // negative rating on move
      blink(2); // blink twice
      hammerfall();
    } 
  }
} // End loop 

    



