from card_game_analysis.deck import Deck
from card_game_analysis.stack import Stack
from card_game_analysis.players import Players
import itertools

if __name__ == "__main__":
    # Initialize the deck, and shuffle the cards
    deck = Deck()
    deck.shuffle()

    # Initialize the stack
    stack = Stack()

    # Initialize players, and distribute the cards in the deck among them
    number_of_players = 4
    players = Players(number_of_players)
    players.distribute_cards(deck)

    # Sort the cards each player has on their hand
    players.sort()

    players.show()

    # Cycle through the players indefinitely times
    for player_name in itertools.cycle(players.player_names):
        player = players.player_dict[player_name]
        # Add the lowest card in value if stack is empty
        if stack.size() == 0:
            stack.add(player.pull())
            print(player_name)

            # Check if the player has won by getting rid of all their cards
            if player.size() == 0:
                print(f"{player_name} won!")
                break
        else:
            # Find a card that is higher or equal in value to previous card in stack
            for index in range(player.size()):
                if player.hand[index].value >= stack.previous_card().value:
                    stack.add(player.pull(index))
                    print(player_name)
                    break

                # Check if player is not able to play
                if index == player.size() - 1:
                    stack.empty()

            # Check if the player has won by getting rid of all their cards
            if player.size() == 0:
                print(f"{player_name} won!")
                break
