import random

print("Welcome to treasure island game!!!")
print("*********** a city has a treasure ***************")

cities = ['zahedan', 'chabahar', 'nikshahr', 'fanooj', 'zabol', 'khash', 'iranshahr', 'fanooj', 'kotij']

current_city = random.randrange(0,len(cities))
golen_city = random.randrange(0,len(cities))

live = 4

while 1:

    if current_city == golen_city:
        print("You won congrat!!!")
        break

    if live <= 0:
        print("you sucked and Game is Over")
        break

    left = ""
    right = ""
    if current_city == 0:
        left = "zabol"
        right = "khash"

    if current_city == 1:
        left = "nikshahr"
        right = "zabol"


    if current_city == 2:
        left = "fanooj"
        right = "chabahar"

    if current_city == 3:
        left = "kotij"
        right = "nikshahr"

    if current_city == 4:
        left = "zahedan"
        right = "chabahar"

    if current_city == 5:
        left = "iranshahr"
        right = "zahedan"


    if current_city == 6:
        left = "khash"
        right = "fanooj"

    if current_city == 7:
        left = "kotij"
        right = "iranshahr"

    if current_city == 8:
        left = "fanooj"
        right = "zahedan"

    choice = input(f"Now in:{cities[current_city]} left:{left}, right:{right}. choose l or r, q for quit: ")

    if choice == 'q':
        break
    elif choice == 'l':
        current_city = cities.index(left)
    elif choice == 'r':
        current_city = cities.index(right)

    live -= 1