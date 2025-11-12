# Q1: Kill Streak Tracker
# [20, 8, 7]

# Q2: Clan Tag Extractor
# Nexus

# Q3: MVP Calculator
players = {
    "pheonix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18},
}
def match_mvp(players):
    best = ""
    kd = 0.0
    for name, stats in players.items():
        ratio = stats["kills"] / stats["deaths"]
        if ratio > kd:
            kd = ratio
            best = name
    return best