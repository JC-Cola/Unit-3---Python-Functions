# Q1: Viewer Peak Detection
# 2300

# Q2: Chat Filter
# WOW WOW LFG

# Q3: Top Donor Finder
def find_top_donor(donations):
    top = ""
    top_amount = -1
    for donor, amount in donations.items():
        if amount > top_amount:
            top = donor
            top_amount = amount
    return top