'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list
'''

str = input("Enter Value (Saperate By (,) ) : ")

list = str.split(",")
newlist = []
dubli = []
for i in list:
    if i in newlist:
        dubli.append(i)
    else:
        newlist.append(i)

print(list)
print(newlist)