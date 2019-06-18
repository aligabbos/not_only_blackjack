import random

def menu():
    #single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
    #complete_deck = single_deck * 6

    single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    print('Shuffling...')
    new_deck = shuffleDeck(single_deck)
    value_new_deck = deckValue(new_deck)

    print('Shuffled deck:', new_deck)
    #print('Value deck:', value_new_deck)

    first_hand = firstHand(new_deck, value_new_deck)
    player = first_hand[0]
    dealer = first_hand[1]
    
    player_cards_value = player[0]
    player_cards = [ player[1][0], player[1][1] ]

    dealer_card_value = dealer[0]
    dealer_card = dealer[1]
    
    print('\nYour hand:', player_cards_value, '\t\tDealer hand:', dealer_card_value)
    print('Your cards:', player_cards[0], player_cards[1], '\tDealer card:', dealer_card)
    print('\nShuffled deck after first hand:', new_deck)
    #print('Value deck after first hand:', value_new_deck)

    hit = hitOneCard(new_deck, value_new_deck, 0)

    player_cards_value += hit[0]
    player_cards.append(hit[1])

    print('\nYour hand:', player_cards_value, '\t\tDealer hand:', dealer_card_value)
    print('Your cards:', player_cards[0], player_cards[1], player_cards[2], '\tDealer card:', dealer_card)
    print('\nShuffled deck after hit:', new_deck)
    #print('Value deck after hit:', value_new_deck)
    
    #print('[1]Give me a card\n[2]Stay') 
    #choice = input()

    

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

def firstHand(deck, deck_value):
    "Function that deal one hand"
    CONST_PLAYER = 2
    CONST_DEALER = 1
    sub = 3
    i = 0
    
    player_cards_value = deck_value[i] + deck_value[CONST_PLAYER]
    dealer_card_value = deck_value[CONST_DEALER]

    player_cards = [deck[i], deck[CONST_PLAYER]]
    dealer_card = deck[CONST_DEALER]

    player = [player_cards_value, player_cards]
    dealer = [dealer_card_value, dealer_card]
    hand = [player, dealer]

    subCards(deck, deck_value, sub)

    return hand;   

def hitOneCard(deck, deck_value, index):
    "Function for the hit of the player"
    sub = 1
    
    card_value = deck_value[index]
    card = deck[index]
    hit = [card_value, card]

    subCards(deck, deck_value, sub)

    return hit;
