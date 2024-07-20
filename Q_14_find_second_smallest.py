'''
 Write a Python program to find the second smallest number in a list.
'''

numbers = input("Enter Number List seprate With (,) : ").split(",")

smallest = numbers[0]
second_smallest = numbers[1]

if second_smallest < smallest:
    smallest, second_smallest = second_smallest, smallest
# [40,20,10,50,5]
for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num


print("Second smallest number:", second_smallest)