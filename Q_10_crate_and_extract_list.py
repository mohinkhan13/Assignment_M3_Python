'''
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''
list = [x**2 for x in range(1,31)]
print(list)

f_five = list[:5]
l_five = list[-5:]

print(f_five)
print(l_five)