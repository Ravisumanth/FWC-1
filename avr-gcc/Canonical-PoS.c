//Turns LED on and off
#include <avr/io.h>
#include <util/delay.h>

 
int main (void)
{
  unsigned char x, y, z, a, in;
#define mask 0x01
  DDRD = 0x00;
  DDRB = 0x20;
while(1){
  in = PIND;
  in = in>>2;
  x = in& mask;
  in = in>>1;
  y = in& mask;
  in = in>>1;
  z = in& mask;
  a = (x||y||!z)&&(x||!y||!z)&&(!x||!y||z)&&(!x||!y||!z);

  if (a) {
    PORTB = ((1 <<  PB5));
  }
  else {PORTB = ((0<<PB5));}
}
}
