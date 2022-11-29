#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;

int servoPositions[3];

void setup() {
  Serial.begin(9600);
  servo1.attach(13);
  servo2.attach(12);
  servo3.attach(11);

}

void loop() {
  while(Serial.available()){
    String input = Serial.readStringUntil('\n');
    servoPositions[0] = input.substring(0,3).toInt();
    servoPositions[1] = input.substring(3,6).toInt();
    servoPositions[2] = input.substring(6,9).toInt();
  }

  servo1.write(servoPositions[0]);
  servo2.write(servoPositions[1]);
  servo3.write(servoPositions[2]);

  delay(500);
}
