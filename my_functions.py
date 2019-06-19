import random

def menu():
    single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    complete_deck = single_deck * 6

    #single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    print('Shuffling...')
    print('Dealing...')
    new_deck = shuffleDeck(complete_deck)
    value_new_deck = deckValue(new_deck)

    player_cards_value, dealer_cards_value = 0, 0
    player_cards = []
    dealer_cards = []

    while True:
        #print('Deck:', new_deck)
        player_cards_value, dealer_cards_value = firstHand(new_deck, value_new_deck, player_cards_value, player_cards, dealer_cards_value, dealer_cards)
        setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
        player_blackjack = checkBlackjack(player_cards_value)

        if player_blackjack:
            print('Blackjack!')

        choice = True

        while choice != 0:
            print('[1] Give me a card\n[2] Stay\n[0] Go smoking a cigarette') 
            choice = input()

            if choice == '1':
                if (not player_blackjack) or (not (player_cards_value == 21)):
                    print('Dealing...')
                    card = hitOneCard(new_deck, value_new_deck, 0)
                    player_cards_value += checkAceValue(player_cards_value, card[0])
                    player_cards.append(card[1])
                    setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                    if player_cards_value > 21:
                        print('Too many')
                        player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                        choice = False
                else:
                    print('You have already 21')
            elif choice == '2':
                print('Dealing...')
                while dealer_cards_value < 17:
                    card = hitOneCard(new_deck, value_new_deck, 0)
                    dealer_cards_value += checkAceValue(dealer_cards_value, card[0])
                    dealer_cards.append(card[1])
                setOverwiew(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                if (dealer_cards_value > player_cards_value) and (dealer_cards_value <= 21):
                    print('Dealer wins')
                elif dealer_cards_value == player_cards_value:
                    print('Stand')
                elif dealer_cards_value < player_cards_value:
                    print('You win')
                else:
                    print('The dealer got busted')
                player_cards_value, dealer_cards_value = clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards)
                choice = False
            elif choice == '0':
                print('See ya')
                choice = False
            else:
                print('Can you choose somenthing right? Fucking dumb')

    

def copyDeck(cards):
    "Function that copy a deck"
    i = 0
    deck = []
    
    while i < len(cards):
        deck.append(cards[i])
        i += 1

    return deck;

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
    
    return shuffled_deck;

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

    return deck;

def firstHand(deck, deck_value, player_cards_value, player_cards, dealer_cards_value, dealer_cards):
    "Function that deal one hand"

    card = hitOneCard(deck, deck_value, 0)
    player_cards_value += card[0]
    player_cards.append(card[1])

    card = hitOneCard(deck, deck_value, 0)
    dealer_cards_value += card[0]
    dealer_cards.append(card[1])

    card = hitOneCard(deck, deck_value, 0)
    player_cards_value += checkAceValue(player_cards_value, card[0])
    player_cards.append(card[1])

    return player_cards_value, dealer_cards_value;   

def hitOneCard(deck, deck_value, index):
    "Function for the hit of the player"
    sub = 1
    
    card_value = deck_value[index]
    card = deck[index]
    card_info = [card_value, card]

    subCards(deck, deck_value, sub)

    return card_info;

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

def checkAceValue(cards_value, card_value):
    if (cards_value > 10) and (card_value == 11):
        card_value = 1
        return card_value;
    else:
        return card_value;

def clearHand(player_cards_value, player_cards, dealer_cards_value, dealer_cards):
    player_cards_value = 0
    dealer_cards_value = 0
    del player_cards[:]
    del dealer_cards[:]
    return player_cards_value, dealer_cards_value;

def checkBlackjack(cards_value):
    if cards_value == 21:
        return True
    else:
        return False