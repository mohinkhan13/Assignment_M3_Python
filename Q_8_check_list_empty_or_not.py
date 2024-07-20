# Write a Python program to check a list is empty or not.

list1 = [10.0,"Hello",22,654,"list"]
list2 = []
list3 = ["Heloo"]
list4 = []
list = {
    "list1": list1,
    "list2": list2,
    "list3": list3,
    "list4": list4
}


for name,i in list.items():
    if not i:
        print(f"{name} Is Empty")
    else:
        print(f"{name} Is Not Empty")
