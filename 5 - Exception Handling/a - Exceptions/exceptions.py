def safe_divide(a,b):
    try:
        return a / b
    # except:
    #     print("Can not divide by zero!")
    #     return None
    except ZeroDivisionError:
        print("Can not divide by zero!")
        return None
    except TypeError:
        print("That's not a valid number!")
        return None
    except:
        print("An error occured...")
print(safe_divide(10,2)) # 5.0
print(safe_divide(10,0)) # Can not divide by zero! Returns None
print(safe_divide(10,"hello")) # Can not divide by zero! Returns None

def safe_operations(a,b,lst,key,d):
    try:
        print(f"Division Result: {a/b}")
        print("Access list element", {lst[2]})
        print("Access dictionary value", {d[key]})
        print("Add numbers: ", a + b)
    except ZeroDivisionError:
        print("Can not divide by zero!")
    except IndexError:
        print("List index out of range!")
    except KeyError:
        print(f"Key {key} not found in dictionary!")
    except TypeError:
        print("Invalid types for operation!")
    except Exception as e:
        print("Some other error occured")
        
print(safe_operations(10,2,[1,2],"Tom",{"John":15}))
print(safe_operations(10,0,[1,2],"Tom",{"John":15}))
print(safe_operations(10,0,[1,2],"Tom",{"Tom":15}))

def calculate_price_per_item(total, items):
    try:
        price_per_item = total/items
        return round(price_per_item, 2)
    except ZeroDivisionError:
        return "No items to calculate"

print(calculate_price_per_item(100, 4)) 
print(calculate_price_per_item(50, 0))
print(calculate_price_per_item(25.50, 3))

def parse_age(str):
    try:
        age = int(str)
        return age
    except ValueError:
        return None
print(parse_age("25"))
print(parse_age("twenty-five"))