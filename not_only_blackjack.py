import random

single_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
complete_deck = single_deck * 6

def shuffleDeck(cards):
    "Function that shuffle the deck passed by argument"
    deck = cards
    length = len(deck)
    shuffled_deck = []

    for i in range( length ):
        deck_length = len(deck)
        random_card = random.randrange(0, deck_length)
        shuffled_deck.append( deck[random_card] )
        deck.pop(random_card)
    
    return shuffled_deck;

print(  shuffleDeck(complete_deck) )
