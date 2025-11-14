# Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }
    
player1 = create_gamer(username="BTStudent", level=25, xp=10000, rank="Gold", online=True)
print(player1)



def send_message(sender, recipient, message, urgent):
    return f"{sender} \u2192 {recipient}: {message} (Urgent: {urgent})"

msg = send_message(sender="Alex", recipient="Jordan", message="Check Discord", urgent=True)
print(msg)



def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | 💗 {likes} 🔁 {retweets}"

post_content("techguru", "Python is amazing!")
print(post_content)


# *args - Accept Any Number of Values

def sum_scores(*scores):
    """Sum ANY Number of scores"""
    total = 0
    for score in scores:
        total += score
    return total

result = sum_scores(10,20,30)