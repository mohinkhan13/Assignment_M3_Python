# Write a Python program to print all unique values in a dictionary.

dictionary = {"a":10,"b":20,"c":30,"D":40,"e":20,"f":10}

values = dictionary.values()
unique = set(values)
print(f"Unique Value In Dictionary Is : {unique}")