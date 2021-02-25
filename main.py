from functions import num_of_players, starting_deal, place_bets, get_cards_val, has_ace, choose_ace_val, bust, \
    double_down, regular_play
from classes import Player, Deck

new_game = True
regular = True

while new_game:

    # GAME SETUP
    dealer = Player('Dealer', 0)
    player_list = []
    players_num = num_of_players()

    i = 1
    for each in range(0, players_num):
        player_list.append(Player(input(f"Enter name of Player{i}: "), i))
        i += 1

    new_round = True

    while new_round:

        for player in player_list:
            player.cards = []
            player.cards2 = []
        dealer.cards = []
        winners_list = []
        deck = Deck()
        deck.shuffle()

        # Dealing cards
        for card in deck.deal(1):
            dealer.cards.append(card)
        for cardabc in deck.all_cards:
            if cardabc.rank == 'Ace':
                dealer.cards.append(cardabc)
                break

        print('')
        print('The dealer has 2 cards')
        print('You can only see one card of the dealer')
        print(f"One of the dealer's cards is {dealer.cards[0]}")
        print('')
        i = 1
        print(player_list)
        starting_deal(player_list, deck)

        print('')

        # Placing bets
        bets = place_bets(player_list)

        for player in player_list:
            print('\n')
            print(f"****************************** {player.name}'s turn ******************************")
            print(f"{player.name} has these cards:")
            for card in player.cards:
                print(card)
            print('')

            # Blackjack check and execution if needed

            if get_cards_val(player.cards) == 21:
                print(f'{player.name} has been dealt a BLACKJACK!')
                chips_by_2 = player.chips.number // 2
                player.chips.number += chips_by_2 * 3
                regular = False

            # Split and execution if needed
            elif player.cards[0].rank == player.cards[1].rank:
                print(f"{player.name} has been dealt 2 cards of same rank and has the option to split them")
                split_choice = 'dfg'
                while split_choice not in ['S', 'C']:
                    split_choice = input(f"{player.name} Do you want to split[S] or continue[C]: ")
                if split_choice == 'S':
                    print('You have chosen to split')
                    print('')

                    player.cards2.append(player.cards.pop())

                    print('Play for the first set: ')
                    print('Current cards are: ')
                    for card in player.cards:
                        print(card)
                        print('')
                    player_choice = player.play()

                    while player_choice == 'D':
                        if bets[player.index] * 2 > player.chips.number:
                            print(f'{player.name} has insufficient funds to double down')
                            player_choice = player.play()
                        else:
                            print(f'{player.name} has chosen to double down')
                            for card in deck.deal(1):
                                player.cards.append(card)
                            print(f"{player.name} now has these cards:")
                            for card in player.cards:
                                print(card)

                            regular = False
                            print('')
                            break

                    while player_choice == 'H':
                        print(f'{player.name} has chosen to hit.')
                        for card in deck.deal(1):
                            player.cards.append(card)
                        print(f"{player.name} now has these cards in their first set:")
                        for card in player.cards:
                            print(card)
                        print('')
                        yes_or_no = 'gsgsdfsd'
                        while yes_or_no not in ['Y', 'N']:
                            yes_or_no = input('Do you wish to continue to hit yes[Y] or no[N]: ')
                        if yes_or_no == 'Y':
                            continue
                        if yes_or_no == 'N':
                            player_choice = 'S'

                    if player_choice == 'S':
                        print(f'{player.name} has chosen to stay.')
                        print(f"{player.name} now has these cards in their first set:")
                        for card in player.cards:
                            print(card)

                    print('Play for the second set: ')
                    print('Current cards are: ')
                    for card in player.cards2:
                        print(card)
                    print('')
                    player_choice = player.play()

                    while player_choice == 'D':
                        if bets[player.index] * 2 > player.chips.value:
                            print(f'{player.name} has insufficient funds to double down')
                            player_choice = player.play()
                        else:
                            print(f'{player.name} has chosen to double down')
                            bets[player.index] = (bets[player.index]) * 2
                            for card in deck.deal(1):
                                player.cards2.append(card)
                            print(f"{player.name} now has these cards:")
                            for card in player.cards2:
                                print(card)

                            regular = False
                            print('')
                            break

                    while player_choice == 'H':
                        print(f'{player.name} has chosen to hit.')
                        for card in deck.deal(1):
                            player.cards2.append(card)
                        print(f"{player.name} now has these cards in their second set:")
                        for card in player.cards2:
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
                        print(f"{player.name} now has these cards in their second set:")
                        for card in player.cards2:
                            print(card)
                            regular = False

                elif split_choice == 'C':
                    player_choice = player.play()

                    done = False
                    choice = 'tatti'
                    while player_choice == 'D' and choice != 'done':
                        choice = double_down(player_choice, bets, player, deck)
                        if choice in ['H', 'S']:
                            player_choice = choice
                            break

                    if player_choice in ['H', 'S']:
                        regular_play(player_choice, player, deck)

            if regular:

                done = False
                choice = 'tatti'
                while player_choice == 'D' and choice != 'done':
                    choice = double_down(player_choice, bets, player, deck)
                    if choice in ['H', 'S']:
                        player_choice = choice
                        break

                if player_choice in ['H', 'S']:
                    regular_play(player_choice, player, deck)

        # Conclude game
        print('')
        print('***************** Conclusion *****************')

        for player in player_list:
            if len(player.cards2) != 0:
                player.cards_sets.append(player.cards2)

            a = 1

            print(player.cards_sets)
            for card_set in player.cards_sets:
                set = []
                for xyz in card_set:
                    set.append(xyz)
                if len(player.cards_sets) == 2:
                    print(f"Result for card set {a}: ")
                    a += 1

                if bust(set) and has_ace(set) == False:
                    print(f"{player.name}'s total value is {get_cards_val(set)}")
                    print(f"{player.name} has busted and has lost their bet.")
                    player.chips.number -= bets[player.index]

                else:
                    print("The dealer has these cards:")
                    for card in dealer.cards:
                        print(card)

                    if has_ace(set) or has_ace(dealer.cards):
                        print('')
                        print(f'{player.name} choose the value of Ace')
                        ace_val = int(choose_ace_val())
                        print(type(ace_val))
                        print(f'val of ace is {ace_val}`')
                        cards_val = 10000000
                        dealer_val = 99999999999999
                        if has_ace(set) and has_ace(dealer.cards):
                            cards_val = get_cards_val(player.cards, ace_val)
                            dealer_val = get_cards_val(dealer.cards, ace_val)
                        elif has_ace(set):
                            cards_val = get_cards_val(set, ace_val)
                            dealer_val = get_cards_val(dealer.cards)
                        elif has_ace(dealer.cards):
                            cards_val = get_cards_val(set)
                            dealer_val = get_cards_val(dealer.cards, ace_val)
                    else:
                        cards_val = get_cards_val(set)
                        dealer_val = get_cards_val(dealer.cards)
                    print(f"Dealer's total value is {dealer_val}")

                    if bust(set):
                        player.chips.number -= bets[player.index]
                        print('')
                        print(f"{player.name}'s total value is {cards_val}")
                        print(f"{player.name} has busted and has lost their bet.")

                    elif bust(dealer.cards):
                        print('The dealer busted and you win your bet.')
                        player.chips.number += bets[player.index]

                    elif cards_val < dealer_val:
                        print('')
                        print(f"{player.name}'s total value is {cards_val}")
                        player.chips.number -= bets[player.index]
                        print(f"The dealer is closer to 21 than {player.name} and so {player.name} loses their bet.")

                    elif cards_val > dealer_val:
                        print('')
                        print(f"{player.name}'s total value is {cards_val}")
                        print(f"{player.name} is closer to 21 than the dealer and wins their bet")
                        player.chips.number += bets[player.index]
                        winners_list.append(player)

        print('\n')
        print('END OF ROUND')
        if len(winners_list) != 0:
            print('The winner(s) of this round is/are: ')
            for winner in winners_list:
                print(winner.name)

        print('')
        game_on_choice = 'fsgdg'
        while game_on_choice not in ['NR', 'NG', 'E']:
            game_on_choice = input('''Index:
    Next round => NR
    New game => NG
    Exit => E
                  
Enter the code of what you want to do: ''')

        if game_on_choice == 'NR':
            new_round = True
        elif game_on_choice == 'NG':
            new_round = False
            new_game = True
        else:
            new_round = False
            new_game = False
