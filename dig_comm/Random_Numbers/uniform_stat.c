#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#include "coeffs.h"

#define unif_path "./uni.dat"


int main(void)
{
uniform(unif_path,1000000);
//print mean and median of RV
printf("Mean- %lf\n",mean("uni.dat"));
printf("varaince %lf\n", variance("uni.dat"));
return 0;
}
