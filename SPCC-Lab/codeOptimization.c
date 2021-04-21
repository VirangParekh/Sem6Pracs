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
    printf("%f\n", circum);

    //Code Motion
    i = 0;
    int limit = 5;
    while (i < limit - 2)
    {
        i++;
    }

    //Dead Code
    i = 0;
    if (i == 1)
        printf("This is a dead code. Would never get executed\n");

    //Common Sub-Expression
    if (i == 0)
    {
        a = (i + 1) * 1;
        b = (i + 2) * 1;
        c = (i + 1) * 1;
    }
    printf("The nos before eliminating Common Sub-Expression: %d %d %d\n", a, b, c);

    //Before Strength Reduction
    c = a * 2;
    printf("Before Strength Reduction c = %d\n", c);
    t = clock() - t;
    double time_taken = ((double)t) / CLOCKS_PER_SEC;
    printf("Time taken: %f", time_taken);
}
