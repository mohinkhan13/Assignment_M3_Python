'''

Write a Python function to get the largest number, smallest num and sum
of all from a list.

'''

list = [65,24,7,55,10,22,75,3,99]
max = list[0]
min = list[0]
sum = 0
for i in list:
    if i > max:
        max = i

    if i < min:
        min = i
    sum += i

print(f"Max Number In List is : {max}")
print(f"Small Number In List is : {min}")
print(f"Total Of List is : {sum}")