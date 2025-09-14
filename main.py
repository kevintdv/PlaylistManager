import json

try:
    with open("users.json") as f:
        users = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    users = {}

name = input("Enter your first name: ")
dob = input("Enter date of birth (DD/MM/YY): ")
key = f"{name}:{dob}"

if key not in users:
    fav_genre = input("Enter your favourite genre: ")
    fav_artist = input("Enter your favourite artist: ")
    users[key] = {
        "genre": fav_genre,
        "artist": fav_artist
    }
    with open("users.json", "w") as f:
        json.dump(users, f, indent=2)
else:
    print(f"Favourite genre: {users[key]['genre']}")
    print(f"Favourite artist: {users[key]['artist']}")
