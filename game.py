from Deck import Deck
from Players import Players

if __name__ == "__main__":
    # Initialize the deck, and shuffle the cards
    deck = Deck()
    deck.shuffle()

    # Initialize players, and distribute the cards in the deck among them
    number_of_players = int(input("Number of players? "))
    players = Players(number_of_players)
    players.distribute_cards(deck)

    # Show remaining cards in the deck
    deck.show()

    # Show the cards each player has on their hand
    players.show()
