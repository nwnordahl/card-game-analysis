from Deck import Deck


class Player:
    """Player class."""

    def __init__(self):
        self.hand = []

    def add(self, card):
        """Add card to the hand."""
        self.hand.append(card)

    def pull(self, index=0):
        """Pull out a card with a specific index out of the player's hand."""
        card = self.hand[index]
        del self.hand[index]
        return card

    def sort(self):
        """Sort the cards ranging from lowest value to highest value."""
        self.hand.sort(key=lambda card: card.value)

    def show(self, player_name="the player"):
        """Show the cards the player has on their hand in the terminal."""
        print(f"Cards on {player_name}'s hand:\n---------------------------")
        for card in self.hand:
            print(f"Value: {card.value}, Color: {card.color}")

    def size(self):
        """Return amount of cards on the player's hand."""
        return len(self.hand)


class Players:
    """Players class."""

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.player_names = [
            f"player_{n}" for n in range(1, number_of_players + 1)]
        self.player_dict = {player_name: Player()
                            for player_name in self.player_names}

    def card_split_amount(self):
        """
        Calculate number of cards given to each player
        at the start of the game.
        """
        number_of_players = self.number_of_players
        return int((52 - (52 % number_of_players))/number_of_players)

    def distribute_cards(self, deck):
        """Distribute the cards among the players."""
        player_dict = self.player_dict
        for i in range(self.card_split_amount()):
            for player in player_dict:
                player_dict[player].add(deck.pull())

    def sort(self):
        """
        Sort the cards each player has on their hand
        ranging from lowest value to highest value.
        """
        for player in self.player_dict:
            self.player_dict[player].sort()

    def show(self):
        """Show the cards each player has on their hand in the terminal."""
        for player in self.player_dict:
            self.player_dict[player].show(player)
            print()

    def size(self):
        """Return amount of players."""
        return self.number_of_players


if __name__ == "__main__":
    # Example of use:
    # Initialize the deck, and shuffle the cards
    deck = Deck()
    deck.shuffle()

    # Initialize 5 players, and distribute the cards among the players
    players = Players(5)
    players.distribute_cards(deck)

    # Show remaining cards in the deck
    deck.show()

    # Sort the cards each player has on their hand
    players.sort()

    # Show the cards each player has on their hand
    players.show()
