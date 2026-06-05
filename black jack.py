import random

single_deck = [
    "Ace", "King", "Queen", "Jack",
    "10", "9", "8", "7", "6", "5", "4", "3", "2"
] * 4

points = {
    "Ace": 11, "King": 10, "Queen": 10, "Jack": 10,
    "10": 10, "9": 9, "8": 8, "7": 7,
    "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

print("With how many decks would you like to play? 1-4")
num_decks = int(input())

if 1 <= num_decks <= 4:
    cards = single_deck * num_decks
else:
    print("Error: too many decks")
    exit()

while True:
    you1 = random.choice(cards)
    you2 = random.choice(cards)
    you3 = random.choice(cards)
    you4 = random.choice(cards)

    dealer1 = random.choice(cards)
    dealer2 = random.choice(cards)
    dealer3 = random.choice(cards)
    dealer4 = random.choice(cards)

    playerpoints = points[you1] + points[you2]
    playerpoints2 = points[you1] + points[you2] + points[you3]
    playerpoints3 = points[you1] + points[you2] + points[you3] + points[you4]

    dealerpoints = points[dealer1] + points[dealer2]
    dealerpoints2 = points[dealer1] + points[dealer2] + points[dealer3]
    dealerpoints3 = points[dealer1] + points[dealer2] + points[dealer3] + points[dealer4]

    def game():
        if playerpoints == 21 and dealerpoints == 21:
            print(f"Dealer: {dealer1}, {dealer2}")
            print("")
            print(f"You: {you1}, {you2}")
            print("Tie")
            return()
        elif playerpoints == 21 and dealerpoints < 21:
            print(f"Dealer: {dealer1}, {dealer2}")
            print("")
            print(f"You: {you1}, {you2}")
            print("You won!")
            return()
        elif playerpoints < 21 and dealerpoints == 21:
            print(f"Dealer: {dealer1}, {dealer2}")
            print("")
            print(f"You: {you1}, {you2}")
            print("You have lost")
            return()
        elif playerpoints < 21 and dealerpoints < 21:
            print(f"Dealer: {dealer1}, #")
            print("")
            print(f"You: {you1}, {you2}")
            print("Hit or Stay:")
            choice1 = input()

            if choice1.lower() == "hit" and playerpoints2 == 21:
                print("")
                print(f"Dealer: {dealer1}, {dealer2}")
                print("")
                print(f"You: {you1}, {you2}, {you3}")
                if dealerpoints < 21:
                    print("You have won!")
                else:
                    print("Tie")
                return()
            elif choice1.lower() == "hit" and playerpoints2 > 21:
                print("")
                print(f"Dealer: {dealer1}, {dealer2}")
                print("")
                print(f"You: {you1}, {you2}, {you3}")
                print("You have lost")
                return()
            elif choice1.lower() == "stay":
                if playerpoints > dealerpoints:
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}")
                    print("You have won")
                elif playerpoints < dealerpoints:
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}")
                    print("You have lost")
                elif playerpoints == dealerpoints:
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}")
                    print("Tie")
                return()
            elif choice1.lower() == "hit" and playerpoints2 < 21:
                print("")
                print(f"Dealer: {dealer1}, #")
                print("")
                print(f"You: {you1}, {you2}, {you3}")
                print("Hit or Stay:")
                choice2 = input()

                if choice2.lower() == "hit" and playerpoints3 == 21:
                    print("")
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}, {you3}, {you4}")
                    if dealerpoints < 21:
                        print("You have won!")
                    else:
                        print("Tie")
                    return()
                elif choice2.lower() == "hit" and playerpoints3 > 21:
                    print("")
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}, {you3}, {you4}")
                    print("You have lost")
                    return()
                elif choice2.lower() == "hit" and playerpoints3 < 21:
                    print("")
                    print(f"Dealer: {dealer1}, {dealer2}")
                    print("")
                    print(f"You: {you1}, {you2}, {you3}, {you4}")
                    if playerpoints3 > dealerpoints:
                        print("You have won!")
                    elif playerpoints3 < dealerpoints:
                        print("You have lost")
                    else:
                        print("Tie")
                    return()
                elif choice2.lower() == "stay":
                    if playerpoints2 > dealerpoints:
                        print(f"Dealer: {dealer1}, {dealer2}")
                        print("")
                        print(f"You: {you1}, {you2}, {you3}")
                        print("You have won")
                    elif playerpoints2 < dealerpoints:
                        print(f"Dealer: {dealer1}, {dealer2}")
                        print("")
                        print(f"You: {you1}, {you2}, {you3}")
                        print("You have lost")
                    elif playerpoints2 == dealerpoints:
                        print(f"Dealer: {dealer1}, {dealer2}")
                        print("")
                        print(f"You: {you1}, {you2}, {you3}")
                        print("Tie")
                    return()

    print("Press Enter to start a round of Black Jack:")
    start = input()
    if start == "":
        game()
    else:
        break

    print("")
    print("Press Enter to play again or any key to quit:")
    again = input()
    if again != "":
        break