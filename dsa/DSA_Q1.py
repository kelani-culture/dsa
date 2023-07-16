"""
	Alice has some cards with numbers written on them she arranges the cards in decreasing orders and lays them face down in a sequence on a table she challenges Bob to pick the cardcontaining a given number by turning over as few cards as possible write a function to help Bob locate the cards
"""
"""
	Identifying problem
	write a program to find the position of a given number in a list of numbers arranged in decreasing order. and also
	we need to minimize the number of times we access the list
"""
"""
    Ask the interviewer platform for clarification
"""
# Name your function appropraitely and think carefully about the signature
# Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
# use descriptive variable names, otherwise you may forget what a variable represents
"""
Our first goal should always be to come up with a correct solution to the problem, which may necessarily be tho most efficient solution. The simplest or most obvious solution to a problem which generally involves checking possible answers is called the brute force solution
"""
"""
1. create a variable position wiht the value 0.
2. check whether the number at index position in card equals query
3. if it does, position is the answer and can be returned from the function
4. If not, increment the value of position by 1, and repeat step 2 to 5 till we reach the last position
5. if the number was not found return -1
"""

def locate_cards(card, query):
     position = 0
    
     if len(card) == 0:
         return -1

     while True:
        # check if for query in the list
        if card[position] == query:
            return position

        # increment position
        position += 1

        # return -1 if value is not found
        if position == len(card):
            return -1


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
    'output': 7
})
tests.append({
    'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6,3 , 2, 2, 2, 0, 0],
              'query': 6},
    'output': 2
})
i = 0
for test in tests:
    i += 1
    print(i, test, '=', locate_cards(test['input']['cards'], test['input']['query']))
