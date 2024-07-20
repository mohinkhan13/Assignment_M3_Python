'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
'''

import itertools

my_dict = {'1': ['a', 'b'], '2': ['c', 'd'], '3' :['e','f']}

lists_of_letters = my_dict.values()

combinations = itertools.product(*lists_of_letters)

for combination in combinations:
    print(''.join(combination))
