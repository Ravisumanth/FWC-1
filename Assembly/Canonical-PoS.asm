;program to check Canonical-PoS form of Boolean equation using Arduino
.include "/root/ravi/codes/m328Pdef.inc"
.def A = r23
.def X = r19
.def Y = r20
.def Z = r21
.def mask = r22
.def result = r24
.def temp = r25
.def temp1 = r28
;declare the output and input pins in Arduino
ldi r16, 0x00
out DDRD, r16
;the next line is for declaring the mask
ldi mask, 0x01
ldi r16, 0x20
out DDRB, r16

start:
;start the logical operations
IN r17, PIND
;store first bit in X
lsr r17
LSR r17
MOV X, r17
AND X, mask
; similarly store the bit in first position in Y
lsr r17
mov Y, r17
and Y, mask
;this is for Z
lsr r17
mov Z, r17
and Z, mask
mov temp, X
or temp,Y
mov temp1, Z
eor temp1,mask
or temp,temp1
mov result, temp

mov temp, X
mov temp1,Y
eor temp1, mask
or temp, temp1
mov temp1,Z
eor temp1, mask
or temp, temp1
and result, temp

mov temp1, X
eor temp1, mask
mov temp, temp1
mov temp1, Y
eor temp1, mask
or temp, temp1
or temp, Z
and result, temp

mov temp1,X
eor temp1, mask
mov temp, temp1
mov  temp1, Y
eor temp1, mask
or temp, temp1
mov temp1,Z
eor temp1, mask
or temp, temp1
and result, temp
;when more number of shifts are to be done, use loops
lsl result
lsl result
lsl result
lsl result
lsl result
out PORTB, result

rjmp start
