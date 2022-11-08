# Uses a finite state machine
#   Should have at least: "win", "quit", "lower", "higher"

# creates a "game loop" within a rungame() function
# Setups base variables using an init() function

# Checks the value of the state and alters it with the fuctions:
#   getsuit
#   getvalue
#   may have a getsuit_and_value function
#   update
#   render

# exits when the player enters Null (nothing) or quit
# exits when the player guesses their card

# Simple number guessing game to show state machine, spin lock, and event based programming
from random import sample

# global constant of possible states and return values
states = {
        "win": "This is correct! You win!",
        "quit": "Thanks for playing. Bye!",
        "notsuit": "This is not the correct suit",
        "lower": "The correct number is lower",
        "higher": "The correct number is higher"
        }

suits = {"hearts", "spades", "clubs", "diamonds"}
values = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "joker", "queen", "king", "Ace"}


def init():
    """
    Initialize game, and generates a random int (1 - 10)
    And prints our intro screen

    returns:
    * gamestate - None object as we just started
    """
    global suits
    global values

    print("Welcome Player! Please guess card with suit and value.")
    return "", sample(suits, 1)[0], int(sample(values, 1)[0])


def getsuit():
    guess_suit = input("What is the correct suit?")
    if guess_suit.lower() == "quit":
        return None

    return guess_suit


def getvalue():
    while True:
        value = input("What is the correct value?")

        try:
            guess_value = int(value)
            break
        except ValueError:
            print("Please type a number without decimals!")
            continue

    return guess_value


def update(gamestate, correct_suit, correct_value, guess_suit, guess_value):
    """
    Update game state: this is a very simple finite state machine
    more a rule based thing

    parameters:
      * gamestate: the state of the game
      * correct_num: the suit to find
      * correct_value: the value to find
      * guess_suit: player's suit guess
      * guess_value: player's value guess
    return:
      * gamestate: the state
    """
    if guess_suit is None:
        gamestate = "quit"
    elif correct_suit != guess_suit:
        gamestate = "notsuit"
    elif correct_suit == guess_suit and correct_value == guess_value:
        gamestate = "win"
    elif correct_value < guess_value and correct_suit == guess_suit:
        gamestate = "lower"
    elif correct_value > guess_value and correct_suit == guess_suit:
        gamestate = "higher"

    return gamestate


def render(gamestate):
    """
    Render game state

    Parameters:
      * gamestate: the current state of the game, "win", "quit", "lower" or "higher"
    """
    global states

    # Cases (switch statement Python style)
    if gamestate in states:
        print(states[gamestate])
    else:
        raise RuntimeError("Unexpected state {}".format(gamestate))


def rungame():
    # Game loop
    gamestate, correct_suit, correct_value = init()
    print(correct_suit)
    print(correct_value)
    while gamestate != "win" and gamestate != "quit":
        guess_suit = getsuit()
        guess_value = getvalue()

        gamestate = update(gamestate, correct_suit, correct_value, guess_suit, guess_value)
        render(gamestate)


# Launch the game
rungame()