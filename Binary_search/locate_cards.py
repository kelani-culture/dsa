"""
    Using binary search tree with recursion
"""
"""
	Alice has some cards with numbers written on them she arranges the cards in decreasing orders and lays
    them face down in a sequence on a table she challenges Bob to pick the card containing a given number
    by turning over as few cards as possible write a function to help Bob locate the cards
"""
"""
    using binary search can help us locate the card quickly by cutting the card in half
    we can help speed up our search insead of going through the card index by index
"""
"""
    How binary search can be applied
    1. Find the middle element of the list
    2. If it matches queried number, return the middle position as the answer
    3. If it is less than the queried number, then search the first half of the list
    4. If it iis greater than the queried number then search the second half of the list
    5. If no more elements remain return -1
"""

def locate_card(cards, target):
    if cards:
        return search_cards(cards, target, 0, len(cards))
    return -1


def search_cards(cards, target, start, end):
    if start > end:
        return -1

    mid = start + (end - start) // 2
    located = locations(cards, mid, target)
    # checks if the card is located in the middle
    if located == 0:
        return mid

    if located == 1:
        return search_cards(cards, target, start + 1, end)

    return search_cards(cards, target, start, end - 1)

# find the locations of a cards
# if multiple occurence occur locate first occurence
def locations(cards, mid, target):

    # 0 - means found
    # -1 - left
    # 1 - go right

    if target == cards[mid]:
        if mid - 1 >= 0 and cards[mid - 1] == target:
            return -1
        else:
            return 0

    elif cards[mid] < target:
        return -1
    else:
        return 1


tests = [8, 8, 6, 6, 6, 6, 6, 5, 3 , 2, 2, 2, 0, 0]
locate = 6 

if __name__ == "__main__":
    print(locate_card(tests, locate))
