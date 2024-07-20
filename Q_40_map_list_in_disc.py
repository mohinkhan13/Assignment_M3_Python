# Write a Python program to map two lists into a dictionary

key = input("Enter Key Separate With space : ").split(" ")
values = input("Enter Values Separate With Space : ").split(" ")

my_disc = dict(zip(key,values))

print(my_disc)