# Write a Python program to create a dictionary from a string

input_string = "key1:value1,key2:value2,key3:value3"

pairs = input_string.split(',')
dictionary = dict(pair.split(':') for pair in pairs)

print("Dictionary:", dictionary)
