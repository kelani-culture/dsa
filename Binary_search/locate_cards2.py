"""
    Using binary search tree with loop
"""
def locate_card2(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            end = mid - 1
        elif arr[mid] > target:
            start = mid + 1
    return -1


def main():
    arr = [13, 12, 11, 10, 9, 8, 7, 6, 4, 3]
    if locate_card2(arr, 8) > -1:
        print("Passed")
    else:
        print("Fail")


main()
