from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

### Define draw card function
def draw_card():
    new_card = random.choice(cards)
    return new_card

### Define calculate function

def calculate_score(card):

    ## Automatic Blackjack

    if sum(card) == 21 and len(card) == 2:
        return 0

    ## Ace count as 1 if sum > 21

    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)

    return sum(card)

### Scoring mechanism

def scoring(player, computer):
    if player == computer:
        return "Draw"
    elif computer == 0:
        return "You lose. Computer has Blackjack."
    elif player == 0:
        return "You win with Blackjack!"
    elif player > 21:
        return "You busted!"
    elif computer > 21:
        return "Computer busted! You win!"
    elif player > computer:
        return "You win!"
    elif computer > player:
        return "You lose!"


play_again = True

while play_again:

    print(logo)

## Starting hand

    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    player_cards = [player_card1, player_card2]

    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_cards = [computer_card1, computer_card2]

    should_continue = True
    player_total = calculate_score(player_cards)
    computer_total = calculate_score(computer_cards)

    while should_continue:

        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's first card: {computer_card1}")

        if player_total == 0 or computer_total == 0 or player_total > 21:
            should_continue = False

        else:

            should_draw = input("Type 'y' to get another card. Type 'n' to pass: \n")

            if should_draw == "y":

                player_cards.append(draw_card())
                player_total = calculate_score(player_cards)

            elif should_draw == "n":
                should_continue = False

    while computer_total != 0 and computer_total < 17:
        computer_cards.append(draw_card())
        computer_total = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
    print(scoring(player_total, computer_total))

    new_game = input("Play again? \n")

    if new_game == "y":
        print("\n" * 20)
        play_again = True

    if new_game == "n":
        play_again = False