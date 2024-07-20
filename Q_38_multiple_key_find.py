# Write a Python program to check multiple keys exists in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

keys_to_check = ['a', 'b', 'c']

all_keys_exist = True

for key in keys_to_check:
    if key not in my_dict:
        all_keys_exist = False
        break

if all_keys_exist:
    print("All keys exist in the dictionary.")
else:
    print("Not all keys exist in the dictionary.")
