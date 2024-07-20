
'''
Write a Python program to combine values in python list of dictionaries.
'''
data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

combined_amounts = {}

for entry in data:
    item = entry['item']
    amount = entry['amount']

    if item in combined_amounts:
        combined_amounts[item] += amount
    else:
        combined_amounts[item] = amount

# Convert the combined_amounts dictionary to a list of dictionaries
result = [{'item': item, 'amount': amount} for item, amount in combined_amounts.items()]

print("Combined values:", result)
