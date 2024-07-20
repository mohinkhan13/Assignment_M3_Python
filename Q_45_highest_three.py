# Write a Python program to find the highest 3 values in a dictionary

my_dict = {
    'a': 10,
    'b': 20,
    'c': 15,
    'd': 30,
    'e': 25
}

values = my_dict.values()

top_3_values = sorted(values, reverse=True)[:3]

print("Highest 3 values:", top_3_values)
