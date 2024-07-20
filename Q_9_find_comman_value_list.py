'''
Write a Python function that takes two lists and returns true if they have
at least one common member.
'''

list1 = [10,20,30,40,50,60,70,90]
list2 = [80,90,100,110]
ind = 0
for i in list1:
    for j in list2:
        if i == j:
            print(True)
            break

