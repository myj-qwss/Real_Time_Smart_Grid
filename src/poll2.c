#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define SYSFS_GPIO_DIR "/sys/class/gpio"
#define POLL_TIMEOUT (-1) /* 3 seconds */
#define EXPORT_BUFFER 4
#define MAX_BUFFER 64
#define MAX_READ 32

int exportGPIO(int gpioPin){
    char buffer[EXPORT_BUFFER];
    ssize_t bytes_written;
    int fd;

    fd = open(SYSFS_GPIO_DIR "/export", O_WRONLY);
    if(fd == -1){ // If opening failed
        fprintf(stderr, "Failed to open export for writing!\n");
        return -1;
    }

    bytes_written = snprintf(buffer, EXPORT_BUFFER, "%d", gpioPin);
    write(fd, buffer, bytes_written);
    close(fd);

    return 0;
}

int unexportGPIO(int gpioPin){
    char buffer[EXPORT_BUFFER];
    ssize_t bytes_written;
    int fd;

    fd = open(SYSFS_GPIO_DIR "/unexport", O_WRONLY);
    if(fd == -1){ // If opening failed
        fprintf(stderr, "Failed to open unexport for writing!\n");
        return -1;
    }

    bytes_written = snprintf(buffer, EXPORT_BUFFER, "%d", gpioPin);
    write(fd, buffer, bytes_written);
    close(fd);

    return 0;
}

int gpioSetEdge(int gpioPin, char *edge){
    int fd, len;
    char buf[MAX_BUFFER];

    // Copies correct path into buf and returns
    // returns length of string written (Even if it overflowed)
    // So len is the length of buf
    len = snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/edge", gpioPin);

    fd = open(buf, O_WRONLY);
    if(fd < 0){
        perror("gpioSetEdge failed");
        return fd;
    }

    write(fd, edge, strlen(edge) +1);
    close(fd);
    return 0;
}


// Open for writing 
// Returns file descriptor
int openGPIO(int gpioPin){
    int fd, len;
    char buf[MAX_BUFFER];

    // Copies correct path into buf and returns
    // returns length of string written (Even if it overflowed)
    // So len is the length of buf
    len = snprintf(buf, sizeof(buf), SYSFS_GPIO_DIR "/gpio%d/value", gpioPin); 

    fd = open(buf, O_RDONLY | O_NONBLOCK);
    /*
    if(fd < 0){
        perror("openGPIO failed");
        return fd;
    }
    */

    return fd;
}

int closeGPIO(int fd){
    return close(fd);
}

int readGPIO(int gpioPin){
    char value[3];
    int fd;

    fd = openGPIO(gpioPin);
    if(fd < 0){
        perror("openGPIO error");
        return fd;
    }

    if(read(fd, value, 3) < 0){
        perror("readGPIO error");
        return -1;
    }

    closeGPIO(fd);

    return atoi(value);

}



int main(int argc, char **argv, char **envp){
    int gpioPin;
    int output;

    gpioPin = 2;

    exportGPIO(gpioPin);
    output = readGPIO(gpioPin);
    printf("%d", output);
    unexportGPIO(gpioPin);
    return 0;
}
