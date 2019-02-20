#!/usr/bin/env python2.7

### Battery Capacity Test ###
from smbus import SMBus
import time

bus = SMBus(1)
addr = 0x0b

csv = open("battery_cap_bb2590.csv","w")
titles = "Voltage, Current, Relsoc, Adssoc\n"
csv.write(titles)

t_end = time.time() + 3600 * 20 # in hours
voltage = 0
current = 0
relsoc = 0
abssoc = 0

while time.time() < t_end:
	try:
		voltage = bus.read_word_data(addr, 0x09)
		current = bus.read_word_data(addr, 0x0a)
		#temperature = bus.read_word_data(addr, 0x08)
		relsoc = bus.read_word_data(addr, 0x0d)
		adssoc = bus.read_byte_data(addr, 0x0e)
	except:
		voltage = 0
		current = 0
		relsoc = 0
		abssoc = 0
	
	line = str(voltage) + "," + str(current) + "," + str(relsoc) + "," + str(adssoc) + "\n"
	csv.write(line)
	print(time.time())
	print(t_end)
	print(line)

	time.sleep(1)

