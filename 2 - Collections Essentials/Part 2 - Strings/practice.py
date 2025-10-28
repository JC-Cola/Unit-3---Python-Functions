# Question 3: Code Tracing
def create_username(first_name, last_name):
    username = (first_name + "_" + last_name).lower()
    return username
    #return f"{first_name.}_{last_name.}".lower()

print(create_username("John", "Smith"))  # Returns "john_smith"

# Question 6: Code Tracing
def check_email(email):
    if "@" in email and ".com" in email.lower():
        return True
    return False

print(check_email("test@gmail.COM"))
print(check_email("invalid.com"))   

# Question 9: Code Tracing 
def create_slug(title):
    slug = title.strip().replace(" ", "-").lower()
    return slug

print(create_slug("My first Blog Post"))
print(create_slug("  Python Tutorial  "))