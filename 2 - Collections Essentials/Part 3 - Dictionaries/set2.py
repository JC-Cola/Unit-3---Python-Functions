# Question 3: Code Writing
def calculate_engagement_rate(post):
    if post.get("views") == 0:
        return 0
    total_interactions = post.get("likes") + post.get("comments") + post.get("shares")
    views = post.get("views")
    engagement_rate = (total_interactions / views) * 100
    return round(engagement_rate, 2)

post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
print(calculate_engagement_rate(post))  # Output: 6.5