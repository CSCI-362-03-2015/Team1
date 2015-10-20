#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


//#include "/TestAutomation/tor-0.2.6.10/src/common/util.c"


//copy pasted from util.c
//some code may have been changed to remove dependencies
char *
tor_strndup_(const char *s, size_t n)
{
  char *dup;
  //tor_assert(s);
  //tor_assert(n < SIZE_T_CEILING);
  //dup = tor_malloc_((n+1) DMALLOC_FN_ARGS);
  dup = malloc(n+1);
  /* Performance note: Ordinarily we prefer strlcpy to strncpy.  But
   * this function gets called a whole lot, and platform strncpy is
   * much faster than strlcpy when strlen(s) is much longer than n.
   */
  strncpy(dup, s, n);
  dup[n]='\0';
  return dup;
}



int main(int argc, char **argv){
  char *s = (argv[1]);
  signed n = atoi(argv[2]);

    char* answer;
    if ((n <=-1)){
      answer="error";}
    else{
      answer = tor_strndup_(s, n);}
    //writing to file, fopen creates it as well
    chdir("./temp");
    FILE *file;
    file = fopen("./TestCase2.txt", "w");
    fprintf(file, "%s", answer);
    fclose(file);

    
}
