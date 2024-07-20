'''
Write a Python program to check whether an element exists within a
tuple
'''

tupp = (10,20,"Hello",1.5,"Mohin",[80,90])

find = input("Enter Element To Find : ")

if find in tupp:
    print("Itme Fond")
else:
    print("Item Not Found")