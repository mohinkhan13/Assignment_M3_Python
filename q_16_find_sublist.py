#Write a Python program to check whether a list contains a sub list
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4]

main_len = len(main_list)
sub_len = len(sub_list)

sublist_found = False

for i in range(main_len - sub_len + 1):
    if main_list[i:i + sub_len] == sub_list:
        sublist_found = True
        break

if sublist_found:
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")
