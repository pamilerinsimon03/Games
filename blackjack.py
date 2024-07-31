import random
import blackjack_art
logo = blackjack_art.logo

def deal_cards(cards):
    for i in range(0, 2):
        choice = random.randint(1, 2)
        if choice == 1:
            cards.append(random.randint(2, 10))
        elif choice == 2:
            special_cards = ["Jack", "Queen", "King", "Ace"]
            cards.append(special_cards[random.randint(0, 3)])
    return cards

def deal_card(cards):
    choice = random.randint(1, 2)
    if choice == 1:
        cards.append(random.randint(2, 10))
    elif choice == 2:
        special_cards = ["Jack", "Queen", "King", "Ace"]
        cards.append(special_cards[random.randint(0, 3)])
    return cards

def result(cards):
    total = 0
    for i in cards:
        if i == "Jack" or i == "Queen" or i == "King":
            i = 10
            total += i
        elif i == "Ace":
            if cards.index("Ace") == 0:
                ace = 11
                i = ace
                total += i
            elif (total + 11) > 21:
                i = 1
                total += i
            else:
                i = 11
        else:
            total += i
    return total

consent = True

while True:
    start_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    if start_game == 'n':
        print("Okay, maybe next time!")
        break
    else:
        print(logo)
        user_cards = []
        computer_cards = []

        dealt_user_cards = deal_cards(user_cards)
        print(f"Your cards are: {dealt_user_cards}")

        dealt_computer_cards = deal_cards(computer_cards)
        print(f"Computer's first card is: {dealt_computer_cards[0]}")

        second_consent = input("Type 'y' to get another card, type 'n' to pass: ")
        if second_consent == 'y':
            dealt_user_cards = deal_card(dealt_user_cards)
            print(f"Your hand: {dealt_user_cards}")

            total_user = result(dealt_user_cards)
            total_computer = result(dealt_computer_cards)
            while True:
                if total_user < 17:
                    print("Your hand is less than 17, you have to collect another card")
                    dealt_user_cards = deal_card(dealt_user_cards)
                    total_user = result(dealt_user_cards)
                else:
                    break
            while True:
                if total_computer < 17:
                    dealt_computer_card = deal_card(dealt_computer_cards)
                    total_computer = result(dealt_computer_card)
                else:
                    break

        else:
            total_user = result(dealt_user_cards)
            total_computer = result(dealt_computer_cards)
            if total_user < 17:
                print("Your hand is less than 17, you have to collect another card")
                dealt_user_cards_card = deal_card(dealt_user_cards)
                total_user = result(dealt_user_cards)
            if total_computer < 17:
                dealt_computer_card = deal_card(dealt_computer_cards)
                total_computer = result(dealt_computer_card)

        if total_user > 21:
            print(f"Your final hand: {dealt_user_cards}")
            print(f"Computer's final hand: {dealt_computer_cards}")
            print("You lose")
        elif total_computer > 21 or total_user > total_computer:
            print(f"Your final hand: {dealt_user_cards}")
            print(f"Computer's final hand: {dealt_computer_cards}")
            print("You win")
        elif total_user == total_computer:
            print(f"Your final hand: {dealt_user_cards}")
            print(f"Computer's final hand: {dealt_computer_cards}")
            print("It's a draw")
        else:
            print(f"Your final hand: {dealt_user_cards}")
            print(f"Computer's final hand: {dealt_computer_cards}")
            print("You lose")
