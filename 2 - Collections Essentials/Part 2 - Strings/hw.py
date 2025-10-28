# 1. Code Tracing
# john.smith gmail.com

# 2. Code Tracing
# tqbf

# 3. Code Writing
def extract_domain(email):
    at = 0
    for char in email:
        if char == "@":
            at += 1

    if at > 1 or at < 1:
        return "Invalid email"
    return email.lower().split("@")[1]
    

print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))

# 4. Code Tracing
# 123456

# 5. Code Tracing
# MY_DOCUMENT

# 6. Code Tracing
# banana

# 7. Code Writing
def filter_numbers(text):
    for char in text:
        if char.isdigit():
            text = text.replace(char, "")
    return text

print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))

# 8. Code Tracing
# https://example.com/users/profile

# 9. Code Writing
def count_characters_types(text):
    letters = 0
    digits = 0
    spaces = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1

    return (f"letters: {letters}, digits: {digits}, spaces: {spaces}")

print(count_characters_types("Hello World 123"))
print(count_characters_types("Test2024!"))