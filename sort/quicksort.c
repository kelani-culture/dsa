#include <stdio.h>

void sort(int arry[], int low, int hi)
{
    if (low > hi)
        return;

    int s = low;
    int e = hi;
    int m = s + (e - s) / 2;
    int pivot = arry[s];

    while (s <= e)
    {
        while(num[s] < pivot)
        {
            s++;
        }
        while (num[e] > pivot)
        {
            e--;
        }
        if (s <= e)
        {
            int temp = nums[s];
            nums[s] = nums[e];
            nums[e] = temp;
            s++;
            e--;
        }
    }
    sort(nums, low, e);
    sort(nums, s, hi);

}
