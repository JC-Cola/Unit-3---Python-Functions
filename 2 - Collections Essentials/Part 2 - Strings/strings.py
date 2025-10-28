# Starting with messy uesr input:
announcement = "  BERGEN TECH robotics meeting TODAY!  "

# We'll clean it up together...
def format_course_code(code):
    return code.strip().upper()
# Test all cases
print(format_course_code(announcement))
print(format_course_code("  webdev101  ")) 
print(format_course_code("  Python202  "))

def count_hashtags(post):
    return post.count('#')
# Test all cases
print(count_hashtags("Great game today! #BergenTech #GoGamrz #Pride"))
print(count_hashtags("Meeting tomorrow in room 205"))
print(count_hashtags("#Robotics team wins #StateChampionship! #STEM #BergenTech"))