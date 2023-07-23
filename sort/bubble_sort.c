#include <stdio.h>


void swap(int a[], int x, int y)
{
    int temp = a[x];
    a[x] = a[y];
    a[y] = temp;
}


void bubble_sort(
