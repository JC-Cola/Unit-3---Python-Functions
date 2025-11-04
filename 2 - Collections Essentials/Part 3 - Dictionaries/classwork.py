# Quesiton 1: Code Tracing
# key_a: value1, key_b: 150, key_d: 50
# key_c: False

# Question 2: Code Tracing
# 120
# 60

# Question 3: Code Writing
def get_user_bio(user):
    bio = user.get("bio", "")
    if bio:
        return bio
    else:
        return "No bio available"

print(get_user_bio({"username": "coder", "bio": "Python enthusiast"})) # "Python enthusiast"}
print(get_user_bio({"username": "newbie"})) # "No bio available"

# Question 4: Code Tracing
# 60
# 100

# Question 5: Code Tracing
# 1

# Question 6: Code Writing
def get_total_engagement(post):
    likes = post.get("likes", 0)
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    total_engagement = likes + comments + shares
    return total_engagement

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10})) # 130
print(get_total_engagement({"likes": 50, "comments": 5})) # 55
print(get_total_engagement({"views": 1000})) # 0

# Question 7: Code Tracing
# 3
# 3

# Question 8: Code Tracing
# {'key1': 'value1', 'key2': 200, 'key3': 50}
# {'key1': 'value1', 'key2': 100, 'key4': True}

# Question 9: Code Writing
def find_most_followers(users):
    most = ""
    if not users:
        return None
    for user in users:
        if user.get("followers", 0) > users[0].get("followers", 0):
            most = user.get("username")
            users[0] = user
    return most
            

print(find_most_followers([{"username": "alex", "followers": 1000}, {"username": "sam", "followers": 5000}, {"username": "jordan", "followers": 3000}])) # "sam"