# Card Game Analysis: Tools to analyse card games

This project was started with the motivation of showing how unfair the card game Daifugo is. Please note that the project is under active development, and there's still a lot of things to add.

## Install/Update/Uninstall with [pip](https://pypi.org/project/pip/)

The recommended way to install is by using [pip](https://pypi.org/project/pip/).

### Install

```shell
$ python -m pip install card-game-analysis
```

### Update

```shell
$ python -m pip install -U card-game-analysis
```

### Uninstall

```shell
$ python -m pip uninstall card-game-analysis
```

## Quick Usage Example

Here is a quick example, using IDLE, demonstrating how to construct a new Deck instance, 
as well as how to shuffle the deck, and pull out a card of the deck.
Then we'll print a listing of the contents of the remaining of the deck.

```pycon
>>> import card_game_analysis as cga # Import the package
>>> deck = cga.Deck() # Create a deck instance
>>> deck.shuffle() # Shuffle the deck
>>> card = deck.pull() # Pull out a card of the deck
>>> print(card.value, card.color) # Print card value and color to the terminal
10 spades
>>> print(deck.size()) # Print the amount of cards that is left in the deck to the terminal
51
>>> deck.show() # Print the remaining cards to the terminal
Remaining cards in the deck:
----------------------------
Value: 2, Color: hearts
Value: 5, Color: diamonds
Value: 13, Color: clubs
            .
            .
            .
Value: 5, Color: hearts
```

## Documentation

Documentation is hosted on readthedocs.org:

https://card-game-analysis.readthedocs.io/en/latest

## Testing
First of all you need to locally install this package with pip.
This can be done by running the following command in the terminal:

```console
$ python -m pip install .
```

You need pytest to run the tests. The recommended way to install is by using [pip](https://pypi.org/project/pip/):

```console
$ python -m pip install -U pytest
```

Tests can be run in the root directory with the command

```console
$ pytest
```

## Relevant links

[Standard 52-card deck Wikipedia article](https://en.wikipedia.org/wiki/Standard_52-card_deck)

[Daifugo Wikipedia article](https://en.wikipedia.org/wiki/Daifug%C5%8D)

## License

Card-game-analysis is [MIT licensed](https://github.com/nwnordahl/card-game-analysis/blob/master/LICENSE).