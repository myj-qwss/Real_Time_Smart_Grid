// Include Libraries //
#include "globals.h"
#include "poll.h"

void rate(){
	clock_gettime(CLOCK_REALTIME, &loop);
	loop_rate = loop.tv_sec - start.tv_sec;
	if(loop_rate >= 2){
		poll();
		printf("%ld\n", loop_rate);
		loop_rate = 0;
		clock_gettime(CLOCK_REALTIME, &start);
	};
};

int main(){
	clock_gettime(CLOCK_REALTIME, &start);
	while(1){
		rate();
	};
	return 0;
};
