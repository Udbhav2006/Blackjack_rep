from classes import Deck, Player
import os
from PIL import Image

def num_of_players():
    choice = 'wrong'

    while choice.isdigit() == False or int(choice) not in range(1, 4):
        choice = input("Enter number of players[max 3]: ")

    choice = int(choice)
    return choice


def starting_deal(player_list, deck):
    for each_player in player_list:
        first_dealt_cards = deck.deal(2)
        for card in first_dealt_cards:
            each_player.cards.append(card)
        print(f"{each_player.name} has been dealt 2 cards.")


def place_bets(player_list):
    bets = ['#']
    for player in player_list:
        bet = player.place_bet()
        bets.append(bet)
        print('')
    return bets


def has_ace(cards_list):
    for card in cards_list:
        if card.rank == 'Ace':
            return True
    return False


def get_cards_val(func_cards_list, func_ace_val=0):
    cards_val = 0
    if has_ace(func_cards_list):
        for card in func_cards_list:

            if card.rank == 'Ace':
                card.value = func_ace_val

            cards_val += card.value

        return cards_val

    if not has_ace(func_cards_list):

        print(func_cards_list)

        for each_card in func_cards_list:
            cards_val += each_card.value
        return cards_val


def choose_ace_val():
    choice = 'dsjgf'
    while choice.isdigit() == False or int(choice) not in [1, 11]:
        choice = input('What do you want the ace value to be[1/11]: ')

    return int(choice)


def bust(cards_list):
    result = 0
    for card in cards_list:
        result += card.value
    if result > 21:
        return True
    return False


def double_down(player_choice, bets, player, deck):
    if bets[player.index] * 2 > player.chips.number:
        print(f'{player.name} has insufficient funds to double down')
        player_choice = player.play()
        if player_choice in ['H', 'S']:
            return player_choice
    else:
        print(f'{player.name} has chosen to double down')
        for card in deck.deal(1):
            player.cards.append(card)
        print(f"{player.name} now has these cards:")
        for card in player.cards:
            print(card)
        return 'done'


def regular_play(player_choice, player, deck):
    while player_choice == 'H':
        print(f'{player.name} has chosen to hit.')
        for card in deck.deal(1):
            player.cards.append(card)
        print(f"{player.name} now has these cards:")
        for card in player.cards:
            print(card)
        print('')
        yes_or_no = 'gsgsdfsd'
        while yes_or_no not in ['Y', 'N']:
            yes_or_no = input('Do you wish to continue to hit yes[Y] or no[N]: ')
        if yes_or_no == 'Y':
            continue
        if yes_or_no == 'N':
            print(f"{player.name} is done hitting.")
            break

    if player_choice == 'S':
        print(f'{player.name} has chosen to stay.')
        print(f"{player.name} now has these cards:")
        for card in player.cards:
            print(card)

def get_pics(cards_list):
    pics_paths = []
    for card in cards_list:
        for pic in os.scandir('D:/Udbhav/Blackjack_rep/Cards_pics'):
            if card.name in pic.path:
                pics_paths.append(pic.path)

def paste_pics(pics_paths, background_path):
    back_im = Image.open('background.jpg')
    back_im_copy = back_im.copy()
    for path in pics_paths:
        back_im_copy.paste()
