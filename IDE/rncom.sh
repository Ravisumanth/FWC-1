#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line
pio run
var=$(ls | grep *.tex)
echo $var
#cd /sdcard/Download/IDE-Codes/IDE
texfot pdflatex $var
var=$(ls | grep *.pdf)
termux-open Canonical-PoS-IDE.pdf


#Test Python Installation
#Uncomment only the following line
#python3 /data/data/com.termux/files/home/storage/shared/training/math/codes/tri_sss.py

