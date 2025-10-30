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
