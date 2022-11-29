#include <Servo.h>

Servo servo1; //Servos
Servo servo2;
Servo servo3;


const int button1 = 3;
const int button2 = 2;

int button1Presses=0,button2Pressed=0;

const int pot1 = A0;
const int pot2 = A1; 
const int pot3 = A2;

int pot1Val, pot2Val, pot3Val, Angulo1, Angulo2, Angulo3; 
int servo1PosSaves[]= {1,1,1,1,1}, servo2PosSaves[]= {1,1,1,1,1}, servo3PosSaves[]= {1,1,1,1,1};

void memoria(){
 for(int i = 0; i < 5; i++){
        servo1.write(servo1PosSaves[i]);
        servo2.write(servo2PosSaves[i]);
        servo3.write(servo3PosSaves[i]);
        Serial.println(" potentimeter Angles: ");
        Serial.println(servo1PosSaves[i]);
        Serial.println(servo2PosSaves[i]);
        Serial.println(servo3PosSaves[i]);
        delay(1050);
      }
}
void setup() {
  servo1.attach(13); // Set up everything and will run once; attach servos and define the pin modes
  servo2.attach(12);
  servo3.attach(11);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  Serial.begin(9600);
}

void loop() {
  pot1Val = analogRead(pot1);
  Angulo1 = map(pot1Val, 0, 1023, 0, 179); // ... and this will map the values from the potentiometers to values the servos can use and store it for later use
  pot2Val = analogRead(pot2); 
  Angulo2 = map(pot2Val, 0, 1023, 0, 179);
  pot3Val = analogRead(pot3);
  Angulo3 = map(pot3Val, 0, 1023, 0, 179);
  
  servo1.write(Angulo1); // These will make the servos move to the mapped angles
  servo2.write(Angulo2);
  servo3.write(Angulo3);
  
  if(digitalRead(button1) == HIGH){ // This will check how many times button1 is pressed and save the positions to an array depending on how many times it is pressed; switch/case works like a if statement
    
    servo1PosSaves[button1Presses] = Angulo1;
    servo2PosSaves[button1Presses] = Angulo2;
    servo3PosSaves[button1Presses] = Angulo3;
    Serial.print("Pos ");
    Serial.print(button1Presses);
    Serial.println(" salva");
    button1Presses++;
  } 
  if(button1Presses==5)
    button1Presses=0;
   
  if(digitalRead(button2) == HIGH){
    memoria();
  }
  delay(300);
