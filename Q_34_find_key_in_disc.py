'''
Write a Python script to check if a given key already exists in a
dictionary
'''

dics = {
    "Name" : "Mohin",
    "Age" : 25,
    "Mobile" : 8200193049,
    "Gneder" : 'male'
}

find = input("Enter value to Find  : ")

if find in dics:
    print(f"The key '{find}' exists in the dictionary.")
else:
    print(f"The key '{find}' does not exist in the dictionary.")