#ifndef POLLH
#define POLLH

#include <linux/i2c-dev.h>
/*
  Includes the following SMBus functions:
    i2c_smbus_access
	     _write_quick
	     _read_byte
	     _write_byte
	     _read_byte_data
	     _write_byte_data
	     _write_word_data
	     _read_word_data
	     _process_call
	     _read_block_data
	     _write_block_data
	     _read_i2c_block_data
	     _write_i2c_block_data
	     _block_process_call
*/


void poll();

#endif


