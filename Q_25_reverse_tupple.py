# Write a Python program to reverse a tuple

my_tuppel = (10,20,40,"Hello",1.5,[50,80],{"Key":123})

my_list = list(my_tuppel)

my_list.reverse()

my_tuppel = tuple(my_list)

print(my_tuppel)