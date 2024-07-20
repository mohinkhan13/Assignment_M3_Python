#Write a Python program to split a list into different variables.

list = input("Enter Vlaues separat with (Space) : ").split(" ")

variables = {}

for i,value in enumerate(list,start=1):
    variables[f"variable_{i}"] = value

for key, value in variables.items():
    print(f"{key} = {value}")