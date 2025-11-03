# Question 2: Code Writing
def find_top_players(players, min_score):
    """ Return a list of usernames for players with score >= min_score """
    top_players = []
    for player in players:
        if player["score"] >= min_score:
            top_players.append(player["username"])
    return top_players

players = [
    {"username": "DragonSlayer", "score": 8500},
    {"username": "NinjaWarrior", "score": 6200},
    {"username": "MageKing", "score": 9100},
    {"username": "ShadowAssassin", "score": 5800}
]

result = find_top_players(players, 7000)
print(result)  # Should print: ['DragonSlayer', 'MageKing']


# Question 3: Code Writing
playlists = {
    "Workout Mix": ["Eye of the Tiger", "Stronger", "Lose Yourself"],
    "Study Vibes": ["Lofi Beat 1", "Chill Piano", "Rain Sounds"],
    "Party Hits": ["Uptown Funk", "Levitating", "Blinding Lights"]
}

all_songs = [] 

for playlist_name, songs in playlists.items():
    for song in songs:
        all_songs.append(song)
        

        
print(f"Total songs: {len(all_songs)}")
print(f"First song: {all_songs[0]}")
print(f"Last song: {all_songs[-1]}")


# Question 4: Code Writing
def calculate_cart_total(cart):
    """ Calculate the total cost of all  items in the cart and returns: total cost (float) """
    total = 0.0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 24.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "USB Cable", "price": 9.99, "quantity": 3}
]

total_cost = calculate_cart_total(cart)
print(f"Total: ${total_cost:.2f}")  # Should print the total cost of the cart