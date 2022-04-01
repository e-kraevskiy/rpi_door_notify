#! /bin/bash

echo "4" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio4/direction

let state=$(</sys/class/gpio/gpio4/value)

while (true)
do
    if [ $(</sys/class/gpio/gpio4/value) == 1 ]
    then
    	echo "Door is open!"
    else
    	echo "closed!"
    fi
    sleep 1
done



