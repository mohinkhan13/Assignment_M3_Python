# Write a Python program to returns sum of all divisors of a number
def sum_of_divisors(n):

    if n <= 0:
        return 0

    total_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total_sum += i

    return total_sum

number = int(input("Enter Number : "))
result = sum_of_divisors(number)
print(f"The sum of all divisors of {number} is {result}.")
