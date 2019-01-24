######################################################
## Makefile                                         ##
## Author: z3r0 Anna DeVries                        ##
## 23 January 2019                                  ##
## Description: compiles all code                   ##
##                                                  ##
## make                                             ##
######################################################

IDIR =./include
CC=gcc
CFLAGS=-I$(IDIR)

ODIR=obj
LDIR =../lib

LIBS=-lm

_DEPS = 
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = battery_polling.o poll.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: ./src/%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

battery_polling: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 
