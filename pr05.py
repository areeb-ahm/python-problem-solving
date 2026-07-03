# You track expenses for your father's jewelry business (tie-in to JewelMind). Given list of dicts:
# pythonexpenses = [
#     {"item": "gold ring", "category": "raw material", "amount": 15000},
#     {"item": "electricity", "category": "utility", "amount": 3000},
#     {"item": "silver chain", "category": "raw material", "amount": 8000},
#     {"item": "rent", "category": "utility", "amount": 12000},
# ]
# Write function total_by_category(expenses). Returns dict: category -> total amount. Use dict comprehension or loop, your choice, but must be clean.

def total_by_category(expenses):
    new_dict = {}

    for item in expenses:
        if item.get("category") in new_dict:
            new_dict[item.get("category")] += item.get("amount")
        else:
            new_dict[item.get("category")] = item.get("amount")
    
    return new_dict

expenses = [
    {"item": "gold ring", "category": "raw material", "amount": 15000},
    {"item": "electricity", "category": "utility", "amount": 3000},
    {"item": "silver chain", "category": "raw material", "amount": 8000},
    {"item": "rent", "category": "utility", "amount": 12000},
]

print(total_by_category(expenses))