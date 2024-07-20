# Write a Python program to calculate the area of a trapezoi
def trapezoid_area(base1, base2, height):
    """Calculate the area of a trapezoid given two bases and the height."""
    area = 0.5 * (base1 + base2) * height
    return area

# Example usage
base1 =  int(input("Enter Length of the first base : "))
base2 =  int(input("Enter Length of the Second base : "))
height = int(input("Enter Height of the trapezoid : "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid with bases {base1} and {base2} and height {height} is {area}.")
