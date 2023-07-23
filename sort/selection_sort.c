#include <stdio.h>


void swap(int arr[], int x, int y);
void selSort(int a[], int n);

void swap(int arr[], int x, int y)
{
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
}


int locOfSmallest(int a[], int s, int e)
{
    int i = s;
    int j = i;

    while (i <= e)
    {
	if (a[i] < a[j])
	    j = i;

	i = i + 1;
    }
    return j;
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
void selSort(int a[], int n)
{
    int i = 0;

    while (i < n - 1)
    {
	int j = locOfSmallest(a, i, n - 1);
	swap(a, i, j);
	i++;
    }
}


int main(void)
{
    int arr[] = {102, 12, 1936, 192, 3, 4, 89, 8};
    int size = sizeof(arr)/sizeof(int);

    display(arr, size);
    selSort(arr, size);
    display(arr, size);
    return 0;
}
