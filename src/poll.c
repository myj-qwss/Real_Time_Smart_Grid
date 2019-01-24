//#include "poll.h"
//#include "globals.h"


//void poll(){
//	printf("Poll Data Now!\n");
//};

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>

#include <sys/stat.h>
#include <sys/types.h>

#include <poll.h>

 /****************************************************************
 * Constants
 ****************************************************************/
 
#define SYSFS_GPIO_DIR "/sys/class/gpio"
#define POLL_TIMEOUT (-1) /* 3 seconds */
#define MAX_BUF 64


/****************************************************************
 * gpio_set_edge
 ****************************************************************/

int gpio_set_edge(unsigned int gpio, char *edge)
{
  int fd, len;
  char buf[MAX_BUF];

  len = snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/edge", gpio);
 
  fd = open(buf, O_WRONLY);
  if (fd < 0) {
    perror("gpio/set-edge");
    return fd;
  
 
  write(fd, edge, strlen(edge) + 1); 
  close(fd);
  return 0;
}

/****************************************************************
 * gpio_fd_open
 ****************************************************************/

int gpio_fd_open(unsigned int gpio)
{
  int fd, len;
  char buf[MAX_BUF];

  len = snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpio);
 
  fd = open(buf, O_RDONLY | O_NONBLOCK );
  if (fd < 0) {
    perror("gpio/fd_open");
  }
  return fd;
}

/****************************************************************
 * gpio_fd_close
 ****************************************************************/

int gpio_fd_close(int fd)
{
  return close(fd);
}


/****************************************************************
 * Export GPIO
 ****************************************************************/
int GPIOExport (int pin){
#define EXPORT_MAX 3
	char buffer[EXPORT_MAX];
	ssize_t bytes_written;
	int fd;
	fd = open("/sys/class/gpio/export", O_WRONLY);
	if (-1 == fd) {
		fprintf(stderr, "Failed to open export for writing!\n");
		return(-1);
	}
	
	bytes_written = snprintf(buffer, EXPORT_MAX, "%d", pin);
	write(fd, buffer, bytes_written);
	close(fd);
	return(0);

}

/****************************************************************
 * Main
 ****************************************************************/
int main(int argc, char **argv, char **envp)
{
  struct pollfd fdset[1];
  int nfds = 2;
  int gpio_fd, timeout, rc;
  char *buf[MAX_BUF];
  unsigned int gpio;
  int len;

  int count=0;



  if (argc < 2) {
    printf("Usage: gpio-int <gpio-pin>\n\n");
    printf("Waits for a change in the GPIO pin voltage level or input on stdin\n");
    exit(-1);
  }

  gpio = atoi(argv[1]);
  GPIOExport(gpio);

  gpio_set_edge(gpio, "falling"); // Set the edge (when to event)
  gpio_fd = gpio_fd_open(gpio);

  timeout = POLL_TIMEOUT;
 
  while (1) {
    memset((void*)fdset, 0, sizeof(fdset));

    fdset[0].fd = gpio_fd;
    fdset[0].events = POLLPRI;

    rc = poll(fdset, nfds, timeout);      

    if (rc < 0) {
      printf("\nSomething fails!\n");
      return -1;
    }
      
    if (rc == 0) {
      printf(".");
    }
            
    if (fdset[0].revents & POLLPRI) {
      len = read(fdset[0].fd, buf, MAX_BUF);
      printf("\nGPIO %d interrupted\n", gpio);
    }
    fflush(stdout);
  }

  gpio_fd_close(gpio_fd);
  return 0;
}
