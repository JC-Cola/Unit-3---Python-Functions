# 15. ZeroDivisionError. Fix: Check if it is empty before.
# 16. C
# 17. strip, upper, split, len
# 18.
def validate_password(password):
    if len(password) == 0:
        return (False, "Empty password")
    if len(password) < 8:
        return (False, "Too short")
    return (True, "Valid")

# 19.
def create_inventory(item_name, *quantities, location="Warehouse"):
    return {
        "item_name": item_name,
        "quantities": quantities,
        "location": location
    }
    
# 20. 
def safe_list_access(items, index):
    try:
        return items[index], True
    except IndexError:
        return None, False