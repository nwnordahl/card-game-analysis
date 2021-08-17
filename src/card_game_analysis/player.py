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


if __name__ == "__main__":
    pass
