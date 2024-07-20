# Example dictionaries
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 150, 'b': 50, 'd': 400}

combined_dict = {}

for key in dict1:
    if key in dict2:
        combined_dict[key] = dict1[key] + dict2[key]
    else:
        combined_dict[key] = dict1[key]

for key in dict2:
    if key not in combined_dict:
        combined_dict[key] = dict2[key]

print("Combined dictionary:", combined_dict)
