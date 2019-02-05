#!/usr/bin/env python2.7

from smbus import SMBus
import time

bus = SMBus(1)
addr = 0x0b

t_end = time.time() + 60 * 15

while time.time() < t_end:
	voltage = bus.read_word_data(addr, 0x09)
	current = bus.read_word_data(addr, 0x0a)
	#temperature = bus.read_word_data(addr, 0x08)
	relsoc = bus.read_word_data(addr, 0x0d)
	adssoc = bus.read_byte_data(addr, 0x0e)

	#voltage = voltage / (2^16)
	#current = current / (2^16)
	
	print("Voltage: ")
	print(voltage)
	print("Current: ")
	print(current)
	print("Relsoc: ")
	print(relsoc)
	print("Adssoc: ")
	print(adssoc)

#	#voltage = int(voltage) / 65536
#	current = current / 65536
#	print("New Voltage: ")
#	print(voltage)
#	print("New Current: ")
#	print(current)

	time.sleep(1)

