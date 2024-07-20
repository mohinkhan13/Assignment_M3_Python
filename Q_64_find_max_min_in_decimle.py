def find_max_min(numbers):
    if not numbers:
        return None, None

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number


decimal_numbers = [3.5, 2.1, 5.7, 1.8, 4.4]

max_number, min_number = find_max_min(decimal_numbers)

print(f"The maximum number is {max_number}.")
print(f"The minimum number is {min_number}.")
