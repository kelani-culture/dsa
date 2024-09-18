
def pair_sum(myList, targ):
    nl = []
    for i in range(len(myList)):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == targ:
                nl.append("{}+{}".format(myList[i], myList[j]))
    return nl
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))