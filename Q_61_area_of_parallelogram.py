# Write a Python program to calculate the area of a parallelogram

def parallelogram_area(base, height):
    area = base * height
    return area

base = int(input("Enter Length of the base : "))
height = int(input("Enter  Height of the parallelogram : "))

area = parallelogram_area(base, height)
print(f"The area of the parallelogram with base {base} and height {height} is {area}.")
