// created on Apr 8
//By: Sophie

//using servo wit a potentiometer with arduino

# include <Servo.h>

Servo servoNumber1;

const int ANALOG_PIN = 0;
int angleOfServo;
   
void setup() 
{
  //servo pin
  servoNumber1.attach(9); 
}

void loop() 
{
  //reads Analog 0 pin
  angleOfServo = analogRead(ANALOG_PIN);
  
  //changes range to 1-180
  angleOfServo = angleOfServo /6;

  servoNumber1.write(angleOfServo);
  delay (15);
}