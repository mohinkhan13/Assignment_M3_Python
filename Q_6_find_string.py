'''

Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings

'''

str1 = input("Enter String : ")
list = str1.split()
print(list)
newList = []
for w in  list:
    if len(w) > 2:
        if w[0] == w[-1]:
            newList.append(w)

print(f"\nThere Are {len(newList)} Words With similar first and last character")
print(newList)
