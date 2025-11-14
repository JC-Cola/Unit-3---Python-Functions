# Q1 - Code Writing
def combine_values(*args):
    if not args:
        return 1
    result = 1
    for value in args:
        result *= value
    return result
combine_values(2, 3, 4) # → 24
combine_values(5) # → 5
combine_values() # → 1

# Q2 - Code Writing
def merge_details(label, **info):
    result = {'label': label}
    result.update
    return result
merge_details("ItemA", size="Large", cost=12.50)
# → {"label": "ItemA", "size": "Large", "cost": 12.50}
merge_details("UserX")
# → {"label": "UserX"}

# Q3 - Code Tracing
# 8
# 10
# 0

# Q4 - Code Tracing
# {'name': 'Alpha', 'x': 1, 'y': 2, 'count': 2}
# {'name': 'Beta', 'count': 0}