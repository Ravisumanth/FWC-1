#include <Arduino.h>


int X,Y,Z,A;


void setup(){
pinMode(6,INPUT);
pinMode(7,INPUT);
pinMode(8,INPUT);
pinMode(13,OUTPUT);
}
void loop(){
X = digitalRead(6);
Y = digitalRead(7);
Z = digitalRead(8);

A = (X||Y||!Z)&&(X||!Z||!Y)&&(!X+!Y+Z)&&(!X+!Y+!Z);

if (A==0){
digitalWrite(13,LOW);
}
else {
digitalWrite(13,HIGH);
}
} 
