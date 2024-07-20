# Write a Python program to remove an empty tuple(s) from a list of tuples.

tupp = [(10,20),(),(20,30,50),(60,90),()]

new_tupp = [tup for tup in tupp if tup]

print(new_tupp)