#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

#define unif1_path "./uni1.dat"
#define unif2_path "./uni2.dat"

int main(void) //main function begins
{
//Uniform random numbers
uniform(unif1_path, 1000000);
uniform(unif2_path, 1000000);
printf("Mean-%lf\n", mean(unif1_path));
printf("Mean-%lf\n", mean(unif1_path));
return 0;
}
