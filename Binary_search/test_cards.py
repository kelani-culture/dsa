from locate_cards import locate_card

# all test for binary search

tests = []
# query the middle element
tests.append({
        
    'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1},
    'output': 6
})
# query the first element
tests.append({
    'input': {'cards': [4, 2, 1, -1], 'query': 4},
    'output': 0
})
# query a single list
tests.append({

    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})
# card does not contain query
tests.append({
    'input': {'cards': [9, 7, 5, 2, -9], 'query': 4},
    'output': -1
})
# card is empty
tests.append({
    'input': {'cards': [], 'query': 7},
    'output': -1
})

#numbers can repeat in cards
tests.append({
    'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0],
              'query': 3},
    'output': 8
})
tests.append({
    'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 5, 3 , 2, 2, 2, 0, 0],
              'query': 6},
    'output': 2
})

for test in tests:
    index =  locate_card(test['input']['cards'], test['input']['query'])

    if test['output'] == index:
       print("Passed")
    else:
        print("Failed") 
