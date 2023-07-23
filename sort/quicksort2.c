#include <stdio.h>


void quickSort(int *arr, size_t size);
void help_sort(int *arr, int start, int end);
void swap(int arr[], int start, int end);

int partition(int arr[], int start, int end)
{
    int pivot = arr[end];
    int partitionIndex = start;

    for (int i = start; i < end; i++)
    {
        if (arr[i] <= pivot)
        {
            swap(arr, arr[i], arr[partitionIndex]);
            partitionIndex++;
        }
    }
    swap(arr, arr[partitionIndex], arr[end]);
    return partitionIndex;
}

void swap(int arr[], int start, int end)
{
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
}

void quickSort(int *arr, size_t size)
{
    if (arr == NULL || size < 2)
        return;

    int start = 0;
    int end = size - 1;
    help_sort(arr, start, end);
}

void help_sort(int *arr, int start, int end)
{
    if (start >= end)
        return;
    int pIndex = partition(arr, start, end);
    help_sort(arr, start, pIndex - 1);
    help_sort(arr, pIndex + 1, end);
}


int main(void)
{
    int arr[] = {7, 6, 5, 4, 3, 2, 1, 0};
    int size = sizeof(arr) / sizeof(int);
    quickSort(arr, size);

    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);

    printf("\n");
    return 0;
}
