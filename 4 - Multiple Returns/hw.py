def search_user_database(query):
    if query is None or query.strip() == "":
        return None, "No search query", False

    if not query.isalpha():  
        return False, "Invalid characters", False

    if query == "john":
        count = 3
        return count, f"Found {count} users", True

    return 0, "No users found", True

    
# TEST 1: Empty string → None (no value provided)
result, message, success = search_user_database("")
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 2: Whitespace only → None (no value provided)
result, message, success = search_user_database(" ")
print(result) # None
print(message) # "No search query"
print(success) # False

# TEST 3: Has numbers → False (operation failed)
result, message, success = search_user_database("user123")
print(result) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 4: Has special chars → False (operation failed)
result = search_user_database("user!@")
print(result) # (False, "Invalid characters", False)

# If you want to unpack from the single tuple:
message, success = result[1], result[2]
print(message) # "Invalid characters"
print(success) # False
print(message) # "Invalid characters"
print(success) # False

# TEST 5: Valid but no results → 0 (valid count of zero)
result, message, success = search_user_database("admin")
print(result) # 0
print(message) # "No users found"
print(success) # True ← Search worked! Just found nothing

# TEST 6: Valid with results → positive int
result, message, success = search_user_database("john")
print(result) # 3 (or any positive number)
print(message) # "Found 3 users"
print(success) # True



def analyze_book_pages(pages):
    if len(pages) == 0:
        return 0, 0, 0.0, False

    count = len(pages)
    total = sum(pages)
    avg = total / count
    has_long = any(p > 500 for p in pages)
    return count, total, avg, has_long

# TEST 1: Mixed collection with one long book
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count) # 4
print(total) # 1360
print(avg) # 340.0
print(has_long) # True (because 620 > 500)

# TEST 2: No long books
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count) # 3
print(total) # 650
print(avg) # 216.67 (approximately)
print(has_long) # False (all books ≤ 500)

# TEST 3: Empty list - EDGE CASE!
count, total, avg, has_long = analyze_book_pages([])
print(count) # 0
print(total) # 0
print(avg) # 0.0
print(has_long) # False

# TEST 4: Exactly 500 pages - TRICKY!
count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(has_long) # False (500 is NOT > 500)

# TEST 5: Exactly 501 pages
count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(has_long) # True (501 IS > 500)