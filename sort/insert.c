#include <stdio.h>



void insertIth(int a[], int n, int i)
{
    int key = a[i];
    int j = i - 1;

    while (j >= 0 && a[j] > key)
    {
	a[j + 1] = a[j];
	j = j - 1;
    }
    a[j + 1] = key;
}
void display(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
	printf("%d ", a[i]);
	i++;
    }
    printf("\n");
}
void insSort(int a[], int n)
{
    int i = 1;

    while (i < n)
    {
	insertIth(a,  n, i);
	i++;
    }
}

int main(void)
{
    int arr[] =  {102, 293, 1823, 11, 38, 344, 97482};
    int size = sizeof(arr) / sizeof(int);
    display(arr, size);
    insSort(arr, size);
    display(arr, size);
    return 0;
}
