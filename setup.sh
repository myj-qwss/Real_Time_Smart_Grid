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


## Install dependencies
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools


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
sudo sed -i '/dtparam=12c_arm=/d' /boot/config.txt

# Add new parameters\
sudo bash -c 'echo "dtparam=i2c1=on" >> /boot/config.txt'
sudo bash -c 'echo "dtparam=i2c_arm=on" >> /boot/config.txt'
