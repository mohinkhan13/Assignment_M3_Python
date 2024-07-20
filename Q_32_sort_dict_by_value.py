'''
Write a Python script to sort (ascending and descending) a dictionary by
value.
'''

my_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 5, 'e': 4}

sorted_ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

sorted_descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original dictionary:", my_dict)
print("Sorted by value in ascending order:", sorted_ascending)
print("Sorted by value in descending order:", sorted_descending)