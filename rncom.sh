#!/bin/bash
<<<<<<< HEAD

=======
#code by Ravi Sumanth Muppana
>>>>>>> f531642 (Created codes and figs folder)

#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line
#$ext="Canonical-PoS-"
#cd /sdcard/Download/math 
#pdflatex gvv_math_eg.tex
#termux-open gvv_math_eg.tex
cd $1
<<<<<<< HEAD
if [[ "$1" == "IDE-Codes" ]];
=======
if [[ "$1" == "IDE" ]];
>>>>>>> f531642 (Created codes and figs folder)
then
pio run
elif [[ "$1" == "Assembly" ]];
then
avra Canonical-PoS.asm
elif [[ "$1" == "Matrices/line" ]];
then
<<<<<<< HEAD
python3 rhombus.py
=======
	python3 rhombus.py
elif [[ "$1" == "Matrices/circle" ]];
then
	python3 circle.py
elif [[ "$1" == "Matrices/conic" ]];
then
	python3 conic.py
elif [[ "$1" == "Optimization" ]];
then
	python3 cvx.py
>>>>>>> f531642 (Created codes and figs folder)
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

