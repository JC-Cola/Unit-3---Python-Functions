def format_phone_number(phone):
    phone = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if phone.isdigit() and len(phone) == 10:
        return f"({phone[0:3]}) {phone[3:6]}-{phone[6:10]}"
    else:
        return "Invalid phone number"

print(format_phone_number("555-123-4567"))
print(format_phone_number("(555) 123 4567"))
print(format_phone_number("5551234567"))
print(format_phone_number("123"))

def sanitize_filename(filename):
    clean_filename = filename.lower().replace(" ", "_")
    special = "._-"
    for char in clean_filename:
        if not char.isdigit():
            if not char.isalpha():
                if char not in special:
                    clean_filename = clean_filename.replace(char, "")
    if clean_filename[-4:] != ".txt":
        clean_filename += ".txt"
    
    if len(clean_filename) > 46:
        return "50 char max with .txt"
    
    return clean_filename   

print(sanitize_filename("Ancient Scroll.txt"))
print(sanitize_filename("Quest 2024! (Epic)"))
print(sanitize_filename("notes"))
print(sanitize_filename("X"*60))