import random
import os
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        for i in range (len(cards)):
            if cards[i] == 11:
                cards[i] = 1
    return sum(cards)
def compare(user_score,comp_score):
    if user_score == comp_score:
        return "draw"
    elif user_score == 0:
        return "Congrats, You win with BlackJack !"
    elif comp_score == 0:
        return "Oops! YOU lose, Opponent got BLackJack!"
    elif user_score > 21:
        return "You Lose, You went over 21!"
    elif comp_score > 21:
        return "You WIn, Opposition went over 21!"
    elif user_score > comp_score:
        return "COngrats! YOu got more score!"
    else:
        return "You lose! "
def play_game():
    user_card = []
    comp_card = []
    is_game_over = False
    for x in range (2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while is_game_over == False:     
        user_score = calculate_score(user_card)
        comp_score = calculate_score(comp_card)
        print(f" Your cards: {user_card}, current score = {user_score}")
        print(f" Computers first card:  {comp_card[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? Yes or No\n ").lower()
            if another_card == "yes":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal_card())
        comp_score = calculate_score(comp_card)

    print(f" Your final hand is {user_card}, final score: {user_score}")
    print(f" Computers card: {comp_card}, final score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play: y or n") == "y":
    os.system('cls')
    play_game()