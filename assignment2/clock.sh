#!/bin/bash

#Prints digital clock in terminal
#Command line argument, time zone
#Ex. ./clock.sh no 

#TZ=America/New_York date

if [ $1 == "no" ]; then
while true; do
 clear
 time=$(TZ="Europe/Oslo" date +"%T")
 echo $time
 echo "Type Ctrl C to quit!"
 sleep 1
done

elif [ $1 == "sk" ]; then
while true; do
 clear
 time=$(TZ="Asia/South_Korea" date +"%T")
 #time=$(TZ + 
 echo $time
 echo "Type Ctrl C to quit!"
 sleep 1
done

elif [ $1 == "us" ]; then
while true; do
 clear
 time=$(TZ="America/New_York" date +"%T")
 echo $time
 echo "Type Ctrl C to quit!"
 sleep 1
done

else
while true; do
 #clear
 time=$(date +"%T")
 echo $time
 echo "Type Ctrl C to quit!"
 sleep 1
done
fi



