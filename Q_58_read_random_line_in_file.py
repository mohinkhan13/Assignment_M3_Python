# Write a Python program to read a random line from a file.
import random
def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                return "The file is empty."
            return random.choice(lines).strip()
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading the file."

file_path = 'example.txt'  # Replace with your file path
print(read_random_line(file_path))
