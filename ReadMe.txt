Hello, World!
Welcome to Real Time Smart Grid
My name is z3r0

This is an electrical engineer's attempt at coding. Good luck.

Setup Instructions:
	chmod +x setup.sh
	./setup.sh

Instructions:
	make clean
	make
	./battery_polling
	
Help:
	You get a "Unable blah blah /var/lib/dpkg/. is another process using it?
	Do:
		sudo lsof /var/lib/dpkg/lock
			> take number under PID
		sudo kill <number>
		sudo rm /var/lib/dpkg/lock
		sudo dpkg --configure -a
	If that doesn't work -- youre on your own.


