import random

# ace = False

def menu():
    print('BLACKJACK\n')
    single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    complete_deck = single_deck * 6

    # single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    # single_deck = [9, 'A', 10, 10, 10, 'A', 10, 8, 10, 'J', 'Q', 'K', 'A', 1]

    print('Shuffling...\n')
    new_deck = shuffleDeck(complete_deck)
    # new_deck = (single_deck)
    value_new_deck = deckValue(new_deck)
    deck_min_length = len(single_deck)/2

    player_cards_value, dealer_cards_value = 0, 0
    player_cards = []
    dealer_cards = []

    money = 100
    deb = 0
    life = 5
    hands = 0
    hands_copy = 0
    bet = 0

    bet_choice = True
    last_hand = False

    while bet_choice:
        if money and deb:
            if hands and (money >= deb):
                choice_stake = True
                while choice_stake :
                    print('Your money:', money, '$')
                    print('Your debts:', deb, '$')
                    print('Hands before the shark beats you:', hands)
                    print('Your life:', setLife(life), '\n')
                    print('Would you pay your debts?\n[1] Yes\n[2] No')
                    choice_stake = input()

                    if choice_stake == '1':
                        print('Your money:', money, '$')
                        print('Your debts:', deb, '$')
                        print('Hands before the shark beats you:', hands)
                        money, deb = payStake(money, deb)
                        print('\nYou have paid your debts')
                        choice_stake = False
                        bet_choice = True
                    elif choice_stake == '2':
                        choice_stake = False
                        bet_choice = True
                    else:
                        print('\nCan you choose somenthing right?\n')
                        choice_stake = True
            elif hands <= 0:
                life -= 1
                hands = hands_copy
                print('The shark has given a punch in your face ( - \u2665)')

        if life:
            if money != 0:
                if last_hand:
                    print('Shuffling...\n')
                    new_deck = shuffleDeck(complete_deck)
                    value_new_deck = deckValue(new_deck)
                    last_hand = False

                if len(value_new_deck) - 3 <= deck_min_length:
                    print('LAST HAND\n')
                    last_hand = True

                print('Your money:', money, '$')
                if deb:
                    print('Your debts:', deb, '$')
                    print('Hands before the shark beats you:', hands)

                print('Your life:', setLife(life), '\n')
                print('Bet:\n[1] 5$\t\t[2] 10$\n[3] 20\t\t[4] 50$\n[5] All\t\t[0] Exit\n')
                bet_choice = input()
                choice = True
                ace_player, ace_dealer = [False], [False]

                if bet_choice == '1':
                    if checkBet(money, 5):
                        bet = 5
                    else:
                        print('You don\'t have enough money')
                        choice = False
                elif bet_choice == '2':
                    if checkBet(money, 10):
                        bet = 10
                    else:
                        print('You don\'t have enough money')
                        choice = False
                elif bet_choice == '3':
                    if checkBet(money, 20):
                        bet = 20
                    else:
                        print('You don\'t have enough money')
                        choice = False
                elif bet_choice == '4':
                    if checkBet(money, 50):
                        bet = 50
                    else:
                        print('You don\'t have enough money')
                        choice = False
                elif bet_choice == '5':
                    if checkBet(money, money):
                        bet = money
                    else:
                        print('You don\'t have enough money')
                        choice = False
                elif bet_choice == '0':
                    if not deb:
                        print('Bye')
                        choice = False
                        bet_choice = False
                    else:
                        print('If you don\'t pay your debts you can\'t leave')
                        choice = False
                        bet_choice = True
                else:
                    print('Can you choose somenthing right?\n')
                    bet_choice = True
                    choice = False
                
                if choice:
                    print('Dealing...')
                    # print('Deck:', new_deck)
                    # print(ace_player, ace_dealer)
                    player_cards_value, dealer_cards_value, ace_player, ace_dealer = firstHand(new_deck, value_new_deck, player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                    hands -= subHands(deb) 
                    # print(ace_player, ace_dealer)
                    setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                    player_blackjack = checkBlackjack(player_cards_value)
                    dealer_blackjack = False
                    insurance_loop = True
                    insurance_choice = False
                    insurance = 0

                    if player_blackjack:
                        print('Blackjack!\n')
                        if dealer_cards_value != 10 and dealer_cards_value != 11:
                            player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                            print('You win', bet + (bet/2), '$\n')
                            money = addMoney(money, bet + (bet/2))
                            choice = False
                        elif dealer_cards_value == 11:
                            while insurance_loop:
                                print('The dealer has an ace. Pay now your Blackjack 1 to 1? (', bet, '$)\n[1] Yes\n[2] No\n')
                                insurance_choice = input ()

                                if insurance_choice == '1':
                                    player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                    print('You win', bet, '$\n')
                                    money = addMoney(money, bet)
                                    choice = False
                                    insurance_loop = False
                                elif insurance_choice == '2':
                                    insurance_loop = False
                                else:
                                    print('Can you choose somenthing right?\n')

                    if dealer_cards_value == 11 and not player_blackjack:
                        while insurance_loop:
                            print('The dealer has an ace. Would you like an insurance? (', bet/2, '$)\n[1] Yes\n[2] No\n')
                            insurance_choice = input ()

                            if insurance_choice == '1':
                                print('Insurance: yes')
                                insurance = addMoney(insurance, bet/2)
                                insurance_loop = False
                            elif insurance_choice == '2':
                                print('Insurance: no')
                                insurance_loop = False
                            else:
                                print('Can you choose somenthing right?\n')

                double = True

                while choice:
                    # print(ace_player, ace_dealer)
                    print('[1] Give me a card\n[2] Stay\n[3] Double +', bet, '$\n')
                    choice = input()

                    if choice == '1':
                        double = False
                        if not (player_cards_value == 21):
                            print('Dealing...')
                            card = hitOneCard(new_deck, value_new_deck, 0)
                            value = checkAceValue(player_cards_value, card[0], ace_player)
                            player_cards_value += value[0]
                            ace_player = value[1]
                            player_cards.append(card[1])
                            setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                            if player_cards_value > 21:
                                if not insurance:
                                    print('Too many. You lose your bet', bet, '$\n')
                                else:
                                    card = hitOneCard(new_deck, value_new_deck, 0)
                                    value = checkAceValue(dealer_cards_value, card[0], ace_dealer)
                                    dealer_cards_value += value[0]
                                    ace_dealer = value[1]
                                    dealer_cards.append(card[1])
                                    if len(dealer_cards) == 2:
                                        dealer_blackjack = checkBlackjack(dealer_cards_value)
                                    setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                    
                                    if dealer_blackjack:
                                        print('Insurance pay', insurance*2, '$\n')
                                        money = addMoney(money, insurance*2)
                                    else:
                                        print('You lose your insurance', insurance, '$\n')
                                        money = addMoney(money, - insurance)

                                    print('Too many. You lose your bet', bet, '$\n')
                                money = addMoney(money, - bet)
                                choice = False
                                player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                        else:
                            print('You have already 21\n')
                    elif choice == '2':
                        print('Dealing...')
                        while dealer_cards_value < 17:
                            # print(ace_player, ace_dealer)
                            card = hitOneCard(new_deck, value_new_deck, 0)
                            value = checkAceValue(dealer_cards_value, card[0], ace_dealer)
                            dealer_cards_value += value[0]
                            ace_dealer = value[1]
                            dealer_cards.append(card[1])
                            if len(dealer_cards) == 2:
                                ace_dealer.append( checkAce(card[0]) )
                                dealer_blackjack = checkBlackjack(dealer_cards_value)
                        setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)

                        if insurance:
                            if dealer_blackjack:
                                print('Insurance pay', insurance*2, '$\n')
                                money = addMoney(money, insurance*2)
                            else:
                                print('You lose your insurance', insurance, '$\n')
                                money = addMoney(money, - insurance)

                        if (dealer_cards_value > player_cards_value) and (dealer_cards_value <= 21):
                            print('You lose your bet', bet, '$\n')
                            money = addMoney(money, - bet)
                        elif dealer_cards_value == player_cards_value:
                            if player_blackjack and not dealer_blackjack:
                                print('Blackjack beats 21. You win', bet + (bet/2), '$\n')
                                money = addMoney(money, bet + (bet/2))
                            elif dealer_blackjack and not player_blackjack:
                                print('Blackjack beats 21. You lose:', bet, '$\n')
                                money = addMoney(money, - bet)
                            else:
                                print('Stand\n')
                        elif dealer_cards_value < player_cards_value:
                            if not player_blackjack:
                                print('You win', bet, '$\n')
                                money = addMoney(money, bet)
                            else:
                                print('You win', bet + (bet/2), '$\n')
                                money = addMoney(money, bet + (bet/2))
                        else:
                            print('The dealer got busted. You win', bet, '$\n')
                            if not player_blackjack:
                                print('You win', bet, '$\n')
                                money = addMoney(money, bet)
                            else:
                                print('You win', bet + (bet/2), '$\n')
                                money = addMoney(money, bet + (bet/2))
                        player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                        choice = False
                    elif choice == '3':
                        if not (player_cards_value == 21):
                            if double:
                                if checkBet(money, bet*2):
                                    bet *= 2
                                    print('Dealing...')
                                    card = hitOneCard(new_deck, value_new_deck, 0)
                                    value = checkAceValue(player_cards_value, card[0], ace_player)
                                    player_cards_value += value[0]
                                    ace_player = value[1]
                                    player_cards.append(card[1])
                                    if player_cards_value > 21:
                                        if not insurance:
                                            setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                            print('Too many. You lose your bet', bet, '$\n')
                                        else:
                                            card = hitOneCard(new_deck, value_new_deck, 0)
                                            value = checkAceValue(dealer_cards_value, card[0], ace_dealer)
                                            dealer_cards_value += value[0]
                                            ace_dealer = value[1]
                                            dealer_cards.append(card[1])
                                            if len(dealer_cards) == 2:
                                                dealer_blackjack = checkBlackjack(dealer_cards_value)
                                            setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                        
                                            if dealer_blackjack:
                                                print('Insurance pay', insurance*2, '$\n')
                                                money = addMoney(money, insurance*2)
                                            else:
                                                print('You lose your insurance', insurance, '$\n')
                                                money = addMoney(money, - insurance)
                                        money = addMoney(money, - bet)
                                        print('Too many. You lose your bet', bet, '$\n')
                                        choice = False
                                        player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                    else:
                                        while dealer_cards_value < 17:
                                            card = hitOneCard(new_deck, value_new_deck, 0)
                                            value = checkAceValue(dealer_cards_value, card[0], ace_dealer)
                                            dealer_cards_value += value[0]
                                            ace_dealer = value[1]
                                            dealer_cards.append(card[1])
                                            if len(dealer_cards) == 2:
                                                dealer_blackjack = checkBlackjack(dealer_cards_value)
                                        setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)

                                        if insurance:
                                            if dealer_blackjack:
                                                print('Insurance pay', insurance*2, '$\n')
                                                money = addMoney(money, insurance*2)
                                            else:
                                                print('You lose your insurance', insurance, '$\n')
                                                money = addMoney(money, - insurance)

                                        if (dealer_cards_value > player_cards_value) and (dealer_cards_value <= 21):
                                            print('You lose your bet', bet, '$\n')
                                            money = addMoney(money, - bet)
                                        elif dealer_cards_value == player_cards_value:
                                            if dealer_blackjack and not player_blackjack:
                                                print('Blackjack beats 21. You lose:', bet, '$\n')
                                                money = addMoney(money, - bet)
                                            else:
                                                print('Stand\n')
                                        elif dealer_cards_value < player_cards_value:
                                            print('You win', bet, '$\n')
                                            money = addMoney(money, bet)
                                        else:
                                            print('The dealer got busted. You win', bet, '$\n')
                                            money = addMoney(money, bet)
                                        player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                                    choice = False
                                else:
                                    print('You don\'t have enough money\n')
                            else:
                                print('You can\'t double your bet after you have taken one card\n')
                        else:
                            print('You have already 21\n')
                    else:
                        print('Can you choose somenthing right?\n')
                        choice = True
            elif not money and not deb:
                deb, money, hands, hands_copy = menuShark(money)
                if deb:
                    bet_choice = True
                else:
                    print('You have lose everything! Bye bye\n')
                    bet_choice = False
            elif not money and deb:
                print('You haven\'t pay the shark! He beat you to death! Bye bye\n')
                bet_choice = False
            else:
                print('You have lose everything! Bye bye\n')
                bet_choice = False
        else:
            print('You are dead! Bye Bye')
            bet_choice = False

def menuShark(money):
    choice = True

    while choice:
        print('Do you need help?\n[1] Yes\n[2] No\n')
        choice = input()

        if choice == '1':
            choice_stake = True

            while choice_stake:
                print('How much do you need?\n[1] 20$ (stake 100%)\n[2] 50$ (stake 120%)\n[3] 100$ (stake 150%)\n[0] Leave\n')
                choice_stake = input()

                if choice_stake == '1':
                    deb = debts(20, 100)
                    return deb, 20, 3, 3
                elif choice_stake == '2':
                    deb = debts(50, 120)
                    return deb, 50, 6, 6
                elif choice_stake == '3':
                    deb = debts(100, 150)
                    return deb, 100, 10, 10
                elif choice_stake == '0':
                    return 0, 0, 0, 0
                else:
                    print('\nCan you choose somenthing right?\n')
                    choice_stake = True
        elif choice == '2':
            return 0, 0, 0, 0
        else:
            print('\nCan you choose somenthing right?\n')
            choice = True

def debts(money, stake):
    deb = 0
    deb += money + (money / 100) * stake
    return deb

def setLife(life):
    heart = '\u2665'
    life_str = ''

    for x in range(life):
        life_str += heart
        life_str += ' '

    return life_str
    
def copyDeck(cards):
    "Function that copy a deck"
    i = 0
    deck = []
    
    while i < len(cards):
        deck.append(cards[i])
        i += 1

    return deck

def subCards(deck, deck_value, index):
    "Function that delete cards from the deck"
    i = 0

    while i < index:
        deck.pop(0)
        deck_value.pop(0)
        i += 1

def shuffleDeck(cards):
    "Function that shuffle the deck passed by argument. This function creates a copy of the parameter"
    deck = copyDeck(cards)
    shuffled_deck = []
    length = len(deck)

    for i in range( length ):
        deck_length = len(deck)
        random_card = random.randrange(0, deck_length)
        shuffled_deck.append( deck[random_card] )
        deck.pop(random_card)
    
    return shuffled_deck

def deckValue(cards):
    "Function that replace values instead of letters. This function creates a copy of the parameter"
    i = 0
    deck = copyDeck(cards)

    while i < len(cards):
        if (deck[i] == 'J') or (deck[i] == 'Q') or (deck[i] == 'K'):
            deck[i] = 10
        elif deck[i] == 'A':
            deck[i] = 11
        i += 1

    return deck

def firstHand(deck, deck_value, player_cards_value, player_cards, dealer_cards_value, dealer_cards):
    "Function that deal one hand"
    ace_player = []
    ace_dealer = []

    card = hitOneCard(deck, deck_value, 0)
    ace_player.append( checkAce(card[0]) )
    value = checkAceValue(player_cards_value, card[0], ace_player)
    player_cards_value += value[0]
    player_cards.append(card[1])

    card = hitOneCard(deck, deck_value, 0)
    ace_dealer.append( checkAce(card[0]) )
    value = checkAceValue(dealer_cards_value, card[0], ace_dealer)
    dealer_cards_value += value[0]
    dealer_cards.append(card[1])

    card = hitOneCard(deck, deck_value, 0)
    ace_player.append( checkAce(card[0]) )
    value = checkAceValue(player_cards_value, card[0], ace_player)
    player_cards_value += value[0]
    player_cards.append(card[1])

    return player_cards_value, dealer_cards_value, ace_player, ace_dealer

def subHands(deb):
    if deb:
        return 1
    return 0

def payStake(money, deb):
    money -= deb
    deb = 0
    return money, deb

def hitOneCard(deck, deck_value, index):
    "Function for the hit of the player"
    sub = 1
    
    card_value = deck_value[index]
    card = deck[index]
    card_info = [card_value, card]

    subCards(deck, deck_value, sub)

    return card_info

def setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards):

    p_cards , d_cards = '', ''

    for card in player_cards:
        p_cards += str(card)
        p_cards += ' '

    for card in dealer_cards:
        d_cards += str(card)
        d_cards += ' '

    print('\nYour hand:', player_cards_value, '\t\tDealer hand:', dealer_cards_value)
    print('Your cards:', p_cards, '\tDealer card:', d_cards, '\n')

def checkAceValue(cards_value, card_value, ace):
    # global ace
    ace_val = False

    for x in range(0,len(ace)):
        if ace[x]:
            ace_val = True

    if (cards_value > 10) and (card_value == 11):
        card_value = 1
        return card_value, ace
    elif (cards_value + card_value > 21) and ace_val:
        ace = [False]
        return card_value - 10, ace
    else:
        return card_value, ace

def checkAce(card_value):
    if card_value == 11:
        return True
    return False

def clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards):
    player_cards_value = 0
    dealer_cards_value = 0
    del player_cards[:]
    del dealer_cards[:]
    return player_cards_value, dealer_cards_value

def checkBlackjack(cards_value):
    if cards_value == 21:
        return True
    else:
        return False

def addMoney(money, bet):
    money += bet
    return money

def checkBet(money, bet):
    if (money - bet) >= 0:
        return True
    else:
        return False