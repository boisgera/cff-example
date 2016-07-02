#include <stdio.h>

void greenify(unsigned char* data, unsigned int length) 
{
    unsigned int i;
    for(i=0; i<length; i++) 
    {
      data[3*i] = 255;
    }
}

