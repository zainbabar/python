planets = {
    "Mercury" : ["The smallest planet, nearest the sun", False, 0],
    "Venus"   : ["Venus takes only 243 days to rotate", False, 0],
    "Earth"   : ["The only planet known to have native life", False, 1],
    "Mars"    : ["The Red Planet is the second smallest planet", False, 2],
    "Jupiter" : ["The largest planet, Jupiter is a gas giant", True, 67],
    "Uranus"  : ["An ice giant with a ring system", True, 27],
    "Neptune" : ["An ice giant and the farthest from the sun", True, 14],
    "Pluto"   : ["Pluto no planet, sorry, no sorry!", False, 5]
}

while True:
    query = input("Which planet would you like information on? ")
    if query in planets.keys():
        print(planets[query][0])
        print("Does it have rings?", planets[query][1])
    else:
        print("Databanks empty. Sorry!")
                                                                                                                                                                                                                                                            