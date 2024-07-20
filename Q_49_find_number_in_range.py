# Write a Python function to check whether a number is in a given range

# Define the number and range
number = int(input("Enter Number : "))
start = 5
end = 15

if start <= number <= end:
    print(f"{number} is within the range [{start}, {end}]")
else:
    print(f"{number} is not within the range [{start}, {end}]")
