# Card Game Analysis: Tools to analyse card games

This project was started with the motivation of showing how unfair the card game Daifugo is,
but as the project evolved it turned out to be
applicable for analyzing a wide variety of card games.

The package is divided in several parts: *deck*, *players*, *game logic* for different games, and *tools for analyzing games*.
The author has prioritized readability over optimizations.
For example, the program follows an identical order to how one would play cards in the real world:
start with an ordered deck, stack the deck, deal the cards in correct order.

Please note that the project is under active development, and there's still a lot of things to add.

## Install/Update/Uninstall with [pip](https://pypi.org/project/pip/)

This package is hosted at [The Python Package Index (PyPI)](https://pypi.org/).
Therefore, the recommended way to install is by using [pip](https://pypi.org/project/pip/):

### Install

```shell
$ python -m pip install card-game-analysis
```

To verify, run

```console
$ python -m pip show card-game-analysis
```

and you should get some information about the package if the installation was successful.

### Update

To update, simply add the -U (or --upgrade) flag:

```shell
$ python -m pip install -U card-game-analysis
```

**Note:** Sometimes you need administrator privileges to run above command successfully.

### Uninstall

```shell
$ python -m pip uninstall card-game-analysis
```

**Note:** This package has been packaged and distributed according to the steps
described here:

https://packaging.python.org/tutorials/packaging-projects/

### Install Locally

It is also possible to clone this repository, and install the package locally.
To do so, run

```console
$ git clone https://github.com/nwnordahl/card-game-analysis.git
```

to clone the repository, and then

```console
$ python -m pip install .
```

in the root directory of this project to install the package locally on your machine.

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

**Note:** To make things simpler, you can use the following abbrevation when importing
the package into your scripts:

```python
import card_game_analysis as cga
```

## Documentation

Documentation is hosted on readthedocs.org:

https://card-game-analysis.readthedocs.io/en/latest

### Build Locally

The documentation can also be built locally. Clone this directory with Git:

```console
$ git clone https://github.com/nwnordahl/card-game-analysis.git
```

Then make sure you have installed Sphinx with pip:

```console
$ python -m pip install -U sphinx
```

Move to the `docs` directory and run

```console
$ make html
```

You can then read the documentation by open `docs/build/html/index.html` in your web browser.

## Testing

### Setup

First of all you need to locally install this package with pip.
(This step has to be done every time there is a change in the `src`.)
This can be done by running the following command in the terminal:

```console
$ python -m pip install .
```

You need pytest to run the tests. The recommended way to install is by using [pip](https://pypi.org/project/pip/):

```console
$ python -m pip install -U pytest
```

### Testing Framework

Tests can be run in the root directory with the command

```console
$ pytest
```

**Note:** The tests will base itself on the package version that is installed.
This means that if you make changes to the actual source code, these changes will not be included in the testing
until you have reinstalled the package locally.

## Relevant links

[Standard 52-card deck Wikipedia article](https://en.wikipedia.org/wiki/Standard_52-card_deck)

[Card game Wikipedia article](https://en.wikipedia.org/wiki/Card_game)

[Daifugo Wikipedia article](https://en.wikipedia.org/wiki/Daifug%C5%8D)

## License

Card-game-analysis is [MIT licensed](https://github.com/nwnordahl/card-game-analysis/blob/master/LICENSE).