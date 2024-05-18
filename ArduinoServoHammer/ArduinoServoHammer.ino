#include <Servo.h>

String myCmd;                            // command string object
Servo myservo;                           // create servo object to control a servo
int startpos = 10;                       // starting position of hammer in degrees
int endpos = 100;                        // ending position of hammer in degrees
int pos = startpos;                      // variable to store the servo position
int decimal_points_on_floatread = 1;     // amount of decimal points we should send when sending a float on serial line
bool blink_for_move_confirmation = true; // whether to blink for confirmation a command has been sent to the arduino

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
  myservo.write(startpos); // move hammer to start position
  delay(1000);             // 1 sec wait
  myservo.write(endpos);   // move hammer to end position
}

/**
 * setup
*/
void setup() {
  myservo.attach(9);               // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);              // Listens on com-port
  Serial.setTimeout(10);           // listen for 10ms when reading String. If no timeout is set, the readstring will wait indefinitely for a command.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);  // Turns the test LED off initially.
  blink(5);                        // let us know the board is set up by blinking 5 times
  myservo.write(startpos);         // move hammer to starting position
}

/**
 * check for incoming values on the usb
 * if values(=move accuracy rating) available < 0, then smash player
*/
void loop() {
  if (Serial.available() > 0) {           // Check for available values on serial line
    myCmd = Serial.readString();          // grab the command string
    float arduinoValue = myCmd.toFloat(); // read the command as being a float (it's the move accuracy)
    Serial.println(arduinoValue, decimal_points_on_floatread); // send back confirmation over usb
    Serial.flush();
    if (blink_for_move_confirmation) blink(2); // blink twice;
    if(arduinoValue < 0) {                // negative rating on move = get whacked
      hammerfall();
    } 
  }
} // End loop 

    




