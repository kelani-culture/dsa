def remove_duplicates(arr):
    nl = []
    for num in arr:
        if num in nl:
            continue
        else:
            nl.append(num)
    return nl

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))