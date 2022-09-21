#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line
#$ext="Canonical-PoS-"
#cd /sdcard/Download/math 
#pdflatex gvv_math_eg.tex
#termux-open gvv_math_eg.tex
cd $1
if [[ "$1" == "IDE-Codes" ]];
then
pio run
elif [[ "$1" == "Assembly" ]];
then
avra Canonical-PoS.asm
elif [[ "$1" == "Matrices/line" ]];
then
python3 rhombus.py
fi



#echo $ext$1 
#cd /sdcard/Download/IDE-Codes/IDE
var=$(ls | grep *.tex)
texfot pdflatex $var
var=$(ls | grep *.pdf)
termux-open $var

#Test Python Installation
#Uncomment only the following line
#python3 /data/data/com.termux/files/home/storage/shared/training/math/codes/tri_sss.py

