#include <stdio.h>
#include "coeffs.h"
#include <math.h>
#include <stdlib.h>


#define GAUSSIAN_PATH "./gau.dat"


int main(void)
{
gaussian(GAUSSIAN_PATH,1e6);
//mean and variance of gau.dat values
printf("Mean- %lf\n",mean(GAUSSIAN_PATH));
printf("varaince %lf\n", variance(GAUSSIAN_PATH));
return 0;
}
