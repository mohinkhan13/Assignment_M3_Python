#• Write a Python program to create a tuple with different data types.

tuppel = ("Hello", 10 , 20 ,"Mohin", 10.2, [10,20],("hi","Python"),{"Name":"Mohin"})

print(tuppel)

for i in tuppel:
    print(f"{i} is type of {type(i)}")