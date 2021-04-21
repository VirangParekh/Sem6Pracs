#include <stdio.h>
#include <time.h>

void main()
{
    clock_t t;
    t = clock();
    float circum, diameter;
    int i, a, b, c;
    printf("Enter the diameter\n");
    scanf("%f", &diameter);

    //Constant Propogation
    circum = (22 / 7) * diameter;
    printf("The Constant value gets evaluated during compile time and gives Circumference = %f\n", circum);

    //Code Motion
    i = 0;
    int limit = 5;
    a = limit - 2;
    while (i < a)
    {
        i++;
    }

    //Dead Code Elimination
    i = 0;

    //Common Sub-Expression
    if (i == 0)
    {
        a = (i + 1) * 1;
        b = (i + 2) * 1;
    }
    printf("The nos after eliminating Common Sub-Expression: %d %d %d \n", a, b, a);

    //After Strength Reduction
    c = a + a;
    printf("After Strength Reduction c = %d\n", c);
    t = clock() - t;
    double time_taken = ((double)t) / CLOCKS_PER_SEC;
    printf("Time taken: %f", time_taken);
}
