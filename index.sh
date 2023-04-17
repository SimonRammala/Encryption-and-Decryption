#!/bin/bash

#figlit used to make a heading for the programm 
figlet -c -f slant Stream Cipher Encryption and Decryption

#used to store all the alphabets in an array
alphabets=("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")


echo "Array used to disply letter " ${alphabets[@]}

#used to ask the user questions
read -p "Enter number of shifts you would like =>" shifts

read -p "Enter your message => " message

echo "Array used to store user input" ${storage[@]}




#look at this loop this is used to help you encrypt a text
for i in seq${#message}
do
	space = $message[$i]

	if [$space == " "]
	  then
		add+=" "
	else
		add += ($space) + $shift - 97 % 26 + 97 | bc

	if
done

echo $space

