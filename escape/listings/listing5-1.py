planets = {"Mercury": "The smallest planet, nearest the sun",
"Venus": "Venus takes only 243 days to rotate",
"Earth": "The only planet known to have naitive life",
"Mars": "The Red Planet is the second smallest planet",
"Jupiter": "The largest planet, Jupiter is a gas giant",
"Uranus": "An ice giant with a ring system",
"Neptune": "An ice giant and the farthest from the sun",
}

while True:
    query = input("Which planet would you like information on? ")
    print(planets[query])