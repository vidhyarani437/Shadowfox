
justice_league = [
    "Superman", "Batman", "Wonder Woman",
    "Flash", "Aquaman", "Green Lantern"
]

# 1. Count the members
print("Number of members:", len(justice_league))

# 2. Add two new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding members:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After changing leader:", justice_league)

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
position = justice_league.index("Aquaman")
justice_league.insert(position + 1, "Green Lantern")
print("After separating them:", justice_league)

# 5. Replace the list with a new team
justice_league = [
    "Cyborg", "Shazam", "Hawkgirl",
    "Martian Manhunter", "Green Arrow"
]
print("New team:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("Alphabetical order:", justice_league)
print("New leader:", justice_league[0])
