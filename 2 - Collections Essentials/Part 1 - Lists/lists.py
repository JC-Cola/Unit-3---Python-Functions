'''
Python
Create: [1, 2, 3]
Add: .append(4)
Remove end: .pop()
Insert: insert(index, val)
Length: len(list)
Slice: [start:end]
Index: [0] 
Length: len(list)
Maximum: max(list)
Minimum: min(list)
Total: sum(list)
'''

#Creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]
#Acessing elements
first_day = daily_likes[0]  #500    
last_day = daily_likes[-1]  #400
third_day = daily_likes[2]  #750
#Slicing
first_three = daily_likes[0:3]  #[500, 600, 750]
last_two = daily_likes[-2:]     #[750, 400]

#Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty."

#Takes list of usernames, returns list with @ prefix
def format_usernames (handles):
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted

print(format_usernames(["nasa", "tswift", "netflix"]))

"Return posts with over 1000 likes"
def filter_trending_posts(likes_list):
    trending = []
    for likes in likes_list:
        if likes > 1000:
            trending.append(likes)
    return trending
print(filter_trending_posts([500, 1200, 800, 1500, 600]))