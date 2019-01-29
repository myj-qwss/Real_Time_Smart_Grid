#!/usr/bin/env python2.7

#import MySQLdb
from smbus import SMBus
import time

#db = MYSQLdb.connect("localhost", "z3r0", "toor", "smbtable")
#curs = db.cursor()

bus = SMBus(1)

addr = 0x0b

t_end = time.time() + 60 * 15

while time.time() < t_end:
	voltage = bus.read_byte_data(addr, 0x09)
	current = bus.read_byte_data(addr, 0x0a)
	temperature = bus.read_byte_data(addr, 0x08)
	relsoc = bus.read_byte_data(addr, 0x0d)
	adssoc = bus.read_byte_data(addr, 0x0e)

	print "Voltage: "
	print voltage
	print "Current: "
	print current
	print "Temperature: "
	print temperature
	print "Relsoc: "
	print relsoc
	print "Adssoc: "
	print adssoc
#	myquery = "INSERT INTO smtable (time, temperature, voltage, current, relsoc, absoc) VALUES ('" + time() + "','" + temperature + "','" + voltage + "','" + current + "','" + relsoc + "','" + absoc + "')"
	#curs.execute(myquery)
	#db.comit()
	
#	print(myquery)

#report = "SELECT time, temperature, voltage, current, relsoc, absoc FROM smbtable"
#cursor.execute(report)
