#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "tinytest.h"
#include "tinytest_macros.h"
#include "util.h"

static void test_round_to_next_multiple_of(void *arg)
{
  (void) arg;
  const int number = 13;
  const int divisor = 4;
  const int correct = 16;
  int answer = NULL;

  answer = round_to_next_multiple_of(number,divisor);
  
  tt_assert(answer);
  tt_int_op(answer, ==, correct);
}

struct testcase_t multiple_of_tests[]={
  {"round to next multiple of test", test_round_to_next_multiple_of, 0, NULL, NULL}, End_OF_TESTCASES
};

struct testgroup_t test_groups[]={
  {"multiple/",multiple_of_test},
  END_OF_GROUPS
};

int main(int argc, const char **argv){
  return tinytest_main(argc,argv,test_groups);
}
  
  
