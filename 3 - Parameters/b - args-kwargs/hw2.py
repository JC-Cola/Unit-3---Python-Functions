# Question 5: Code Tracing
# 9.00
# 15.00

# Question 6: Code Writing
def make_notification(user, *messages, urgent=False):
    message_str = ", ".join(messages)
    if urgent:
        return f"URGENT: {user} - {message_str}"
    else:
        return f"{user} - {message_str}"
    
print(make_notification("admin", "Server down!", urgent=True))
print(make_notification("user", "Welcome", "Check inbox"))

# Question 7: Code Tracing
# SELECT name,email FROM users LIMIT 10
# SELECT * FROM logs WHERE level='error' LIMIT 5


# Question 8: Code Writing
def log_action(actor, *actions, timestamp=None, **context):
    actions_str = ", ".join(actions)
    context_str = ", ".join([f"{key}={value}" for key, value in context.items()])
    if timestamp:
        return f"[{timestamp}] {actor}: {actions_str} | {context_str}"
    else:
        return f"{actor}: {actions_str} | {context_str}"
    
print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4")) # bot: login, scan | source=APiI, ip=1.2.3.4