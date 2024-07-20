# Write a Python program to find the repeated items of a tuple.

tupp = input("Enter values Separate With Space : ").split(" ")

my_list = list(tupp)
repeated_items = []
for item in my_list:
    if my_list.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print(repeated_items)