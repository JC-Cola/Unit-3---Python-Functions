# Question 3: Code Writing
def calculate_discount(price, member_status):
    if member_status == "premium":
        return price * 0.7
    elif member_status == "standard":
        return price * 0.85
    else:
        return price

print(calculate_discount(100, "premium"))
print(calculate_discount(100, "standard"))
print(calculate_discount(100, "guest"))

# Question 6: Code Writing
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))
print(count_vowels("Python"))
print(count_vowels("AEIOU"))

# Question 9: Code Writing
def validate_password(password):
    if len(password) < 8:
        return False
    has_digit = any(i.isdigit() for i in password)
    return has_digit