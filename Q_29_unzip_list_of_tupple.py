# Write a Python program to unzip a list of tuples into individual lists.

list_tupp = [(10,20,30),("Hello","My","name"),(20,30)]

lists = {}

for i,item in enumerate(list_tupp,start=1):
    new_item = list(item)
    lists[f"list{i}"] = new_item

for key, value in lists.items():
    print(f"{key} {value} {type(value)}")
