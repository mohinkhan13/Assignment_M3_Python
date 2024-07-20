'''
Write a Python program to calculate surface volume and area of a
cylinder
'''

PI = 3.141592653589793

def cylinder_volume(radius, height):
    return PI * radius**2 * height

def cylinder_surface_area(radius, height):
    return 2 * PI * radius * (radius + height)

radius = int(input("Enter Radius of the base of the cylinder : "))
height = int(input("Enter Height of the cylinder : "))

volume = cylinder_volume(radius, height)
surface_area = cylinder_surface_area(radius, height)

print(f"The volume of the cylinder with radius {radius} and height {height} is {volume:.2f}.")
print(f"The surface area of the cylinder with radius {radius} and height {height} is {surface_area:.2f}.")
