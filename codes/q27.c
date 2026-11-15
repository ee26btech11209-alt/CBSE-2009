#include <stdio.h>

// Function to find maximum
int max(int a, int b)
{
    if (a > b)
        return a;
    else
        return b;
}

int main()
{
    int x, y;
    int profit, maxProfit = 0;
    int bestFans = 0, bestMachines = 0;

    //  loops to check all combinations
    for (x = 0; x <= 20; x++)
    {
        for (y = 0; y <= 20; y++)
        {
            // Check budget and space constraints
            if ((360*x + 240*y <= 5760) &&
                (x + y <= 20))
            {
                profit = 22*x + 18*y;

                if (profit > maxProfit)
                {
                    maxProfit = max(maxProfit, profit);

                    bestFans = x;
                    bestMachines = y;
                }
            }
        }
    }

    printf("Number of fans = %d\n", bestFans);
    printf("Number of sewing machines = %d\n", bestMachines);
    printf("Maximum profit = Rs. %d\n", maxProfit);

    return 0;
}
