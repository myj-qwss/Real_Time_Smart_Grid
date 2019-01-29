######################################################
## Setup.h                                          ##
## Author: z3r0 - Anna DeVries                      ##
## 23 Jan 2019                                      ##
## chmod +x setup.sh                                ##
## ./setup.sh                                       ##
## Description: installs all necessary dependencies ##
## Sets all config files; enables ssh               ##
######################################################

#!/bin/bash


## exit on failure
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'


## Update
#sudo apt-get install update
#sudo apt-get upgrade
sudo apt-get install python3
sudo apt-get install pythong3-pip


## Install dependencies
sudo apt-get install git-core
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
cd
if [ ! -d "$wiringPi/" ]; then
	git clone git://git.drogon.net/wiringPi
	cd ~/wiringPi
	git pull origin
	./build					## Troubleshooting: gpio -v
						## Toubleshooting: gpio readall
fi

## If using python
# sudo raspi-config
# Select Interfacing Options
# Select SPI, select yes, enter
# Repeat for I2C and Serial
if grep -Fxq "alias python='/usr/bin/python3'" ~/.bashrc
then
        echo "Python3 Already Configured"
else
        echo "alias python='/usr/bin/python3'" >> ~/.bashrc ## >> appends to end
fi

if grep -Fxq "alias pip=pip3" ~/.bashrc
then
        echo "Pip3 Already Configured"
else
        echo "alias pip=pip3" >> ~/.bashrc ## >> appends to end
fi

source ~/.bashrc


## Update /etc/modules
if grep -Fxq "i2c-bcm2708" /etc/modules
then
	echo "i2c-bcm2708 Already Exists"
else
	echo i2c-bcm2708 >> /etc/modules
fi

if grep -Fxq "i2c-dev" /etc/modules
then
	echo "i2c-dev Already Exists"
else
	echo i2c-dev >> /etc/modules ## >> appends to end
fi


## Update /boot/config.txt
# Remove old parameters
sudo sed -i '/dtparam=i2c1=/d' /boot/config.txt
sudo sed -i '/dtparam=i2c_arm=/d' /boot/config.txt
sudo sed -i '/dtparam=i2c_vc=/d' /boot/config.txt


# Add new parameters\
sudo bash -c 'echo "dtparam=i2c1=on" >> /boot/config.txt'
sudo bash -c 'echo "dtparam=i2c_arm=on" >> /boot/config.txt'
sudo bash -c 'echo "dtparam=i2c_vc=on" >> /boot/config.txt'


sudo reboot

## Troubleshooting
# after rebooting...
# ls /dev/*spi* should return /dev/spidev0.0 /dev/spidev0.1
# ls /dev/*i2c* should return /dev/i2c-1
# sudo i2cdetect -y 1
# sudo i2cget
