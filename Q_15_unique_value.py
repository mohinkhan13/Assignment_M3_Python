# Write a Python program to get unique values from a list

my_list = input("Enter values (Separate with ',') : ").split(",")

unique_values = list(set(my_list))

print("Unique values:", unique_values)