def factorial(n):
    """Calculate the factorial of a nonnegative integer n."""
    if n < 0:
        raise ValueError("The input must be a nonnegative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter Number : "))
print(f"Factorial of {num} Is {factorial(num)}")
