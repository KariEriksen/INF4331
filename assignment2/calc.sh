#!/bin/bash

#Bash code for adding/multiplying number sequence, and finding maximal/minimum value in sequnce
#CL input $ ./calc.sh S 1 2 3 4 
#CL output 10


#Summation

if [ $1 == "S" ]; then
for num in "${@:2}"; do
(( sum += num ))
done 
echo $sum


#Multiplication

elif  [ $1 == "P" ]; then
prod=1
for num in "${@:2}"; do
(( prod = prod*num ))
done
echo $prod


#Finding maximal value

elif [ $1 == "M" ]; then
max=$2

for num in "${@:3}"; do
if [ $num \> $max ]; then
max=$num

else
max=$max
fi

done
echo $max

#Finding minimal value

elif [ $1 == "m" ]; then
min=$2

for num in "${@:3}"; do
if [ $num \< $min ]; then
min=$num

else
min=$min
fi

done
echo $min

else
echo "Specify type of operation, ex. S, P, M or m, as second command line argument"
fi
