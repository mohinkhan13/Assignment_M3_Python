# Write a Python program to remove duplicates from a list.

list = ["new",10,"python","new",10,"hello",22,"My","Name",2,"CSS",2,"CSS","CSS"]
repeat = []
original = []

for i in list:
    if i in original:
        if i not in repeat:
            repeat.append(i)
    else:
        original.append(i)
print(f"\nOriginal List :  ->  {list}")
print(f"Repeted Word :   ->  {repeat}")
print(f"Without Repeat List :   ->  {original}")