#include <Servo.h>

String myCmd;

Servo myservo;  // create servo object to control a servo

int startpos = 0;
int endpos = 100;
int pos = startpos;    // variable to store the servo position
bool hammerFalling = false;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  Serial.begin(9600); // Listens on com-port
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW); // Turns the test LED off initially.
}

void loop() {
  //Check values of Comport serial
 if (Serial.available() > 0) { //Input test Inbuilt led
    String myCmd = Serial.readStringUntil('\r');
    myCmd.trim();
    Serial.println(myCmd);

    if(myCmd != ""){
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      digitalWrite(LED_BUILTIN, LOW);
      delay(100);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(100);
      digitalWrite(LED_BUILTIN, LOW);
      delay(100);
      hammerFalling = true;
      if (hammerFalling == true) {
        for (pos = endpos; pos >= startpos; pos -= 2) { //mf
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(10);                       // waits 15 ms for the servo to reach the position
        }
          delay(1000);  // 10 sec wait
        for (pos = startpos; pos <= endpos; pos += 1) { // goes from 0 degrees to 180 degrees
          // in steps of 1 degree
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(10);  
        }
        hammerFalling = false;
        delay(1000);
      }
    } // End inputtest


      float arduinoValue = myCmd.toFloat();
      Serial.flush();
      //temporaryCompare(arduinoValue);
  }
 

} // End loop 

    
  float difference = 0;
  float lastInputValue = 0;

  void temporaryCompare(int currentInputValue) {
    if(lastInputValue != currentInputValue){
    difference = lastInputValue - currentInputValue;
    }
    if(difference <= -1){
    hammerFalling = true;

    }
    lastInputValue = currentInputValue;
}




