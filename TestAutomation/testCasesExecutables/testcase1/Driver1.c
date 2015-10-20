#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


//#include "/TestAutomation/tor-0.2.6.10/src/common/util.c"


//copy pasted from util.c
unsigned
round_to_next_multiple_of(unsigned number, unsigned divisor)
{
  number += divisor - 1;
  number -= number % divisor;
  return number;
}



int main(int argc, char **argv){
  int ia = atoi(argv[1]);
  int ib = atoi(argv[2]);
  unsigned a = ia;
  unsigned b = ib;
    
    unsigned num2round;
    num2round = round_to_next_multiple_of(a, b);
 
    //writing to file, fopen creates it as well
    chdir("./temp");
    FILE *file;
    file = fopen("./TestCase1.txt", "w");
    fprintf(file, "%d", num2round);
    fclose(file);

    
}
