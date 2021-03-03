from classes import Deck, Player
import os
from PIL import Image
from pathlib import Path


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


# def get_pics_normal(players):
#     for person in players:
#         pics_paths = []
#         cards_list = person.cards
#         for card in cards_list:
#             print(card)
#             for pic in os.scandir('New folder/Cards_pics'):
#                 path_list = pic.path.split('\\')
#                 path = ''
#                 o = 0
#                 for each in path_list:
#                     path = path + each + '/'
#                     o += 1
#                 path = path[:-1]
#                 if card.name in path:
#                     pics_paths.append(path)
#
#     return pics_paths


def get_pics_for_a_set(cards_list):
    pics_paths = []
    for card in cards_list:
        print(card)
        for pic in os.scandir('Cards_pics'):
            path_list = pic.path.split('\\')
            path = ''
            o = 0
            for each in path_list:
                path = path + each + '/'
                o += 1
            path = path[:-1]
            if card.name in path:
                pics_paths.append(path)

    return pics_paths


def paste_pics_normal(player, dealer_cards_num=0, set2=False):
    back_im = Image.open('big_back.png')
    back_im_copy = back_im.copy()

    if player.name == 'Dealer':
        rest_of_cards = 0
        l = 0
        while l < dealer_cards_num:
            print('Entered while')
            i = 200
            pics_paths = get_pics_for_a_set(player.cards)
            for path in pics_paths:
                p = Image.open(path)
                back_im_copy.paste(p, (i, 100))
                x, y = p.size
                i += (x + 1)
                rest_of_cards += 1
                l += 1

        i = 200
        for each in range(0,rest_of_cards):
            p = Image.open('Cards_pics/card_back.png')
            p.thumbnail((150,150))
            p.save('Cards_pics/card_back.png')
            back_im_copy.paste(p, (i, 100))
            a, b = p.size
            i += (a + 1)
    else:
        num = player.index
        num_im = Image.open(f'Num pics/{player.index}.jpg')
        num_im.thumbnail((80, 80))
        num_im.save(f'Num pics/{num}.jpg')
        back_im_copy.paste(num_im, (154, 300))

        if not set2:
            pics_paths = get_pics_for_a_set(player.cards)
            i = 20
            for path in pics_paths:
                p = Image.open(path)
                back_im_copy.paste(p, (i, 475))
                x, y = p.size
                i += (x + 1)
        else:
            pics_paths = get_pics_for_a_set(player.cards2)
            i = 20
            for path in pics_paths:
                p = Image.open(path)
                back_im_copy.paste(p, (i, 475))
                x, y = p.size
                i += (x + 1)

    # ==========================================================================================
    #                 i = 20
    #                 for path in pics_paths:
    #                     s = Image.open('first_set.png')
    #                     p = Image.open(path)
    #                     back_im_copy.paste(s, (i,475))
    #                     back_im_copy.paste(p, (i, 500))
    #                     x, y = p.size
    #                     i += (x + 1)
    #             elif set == 2:
    #                 i = 20
    #                 for path in pics_paths:
    #                     p = Image.open(path)
    #                     back_im_copy.paste(p, (i,475))
    #                     x,y = p.size
    #                     i += (x+1)
    back_im_copy.show()
