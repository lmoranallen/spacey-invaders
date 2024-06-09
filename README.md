## Coding Challenge #65

This challenge is to build your own version of space invaders.

### Requirements

Space invaders is a relatively simple game, the gameplay has the player moving their ‘ship’ horizontally across the bottom of the screen and firing at aliens above. There are some bases for the player to take cover underneath.

In the original version the aliens begin in five rows of eleven that move left and right as a group, shifting down the screen each time they reach a screen edge. The player wins by shooting all of the aliens.

As the aliens move across the screen they occasionally drop bombs which fall towards the player and either damage the bases the player has or kill the player, taking one of their lives. The player’s shots also damage the bases.

The player has three lives and the game ends when either they run out of lives or the invaders reach the bottom of the screen.


### Confirming Setup
- Python version: `Python 3.10.12`
- Create virtual environment: `python3 -m venv {ENV_NAME}`
- Start virtual environment: `source {ENV_NAME}/bin/activate`
- Install required packages: `python3 -m pip install -r requirements.txt`
- Confirm packages are connected by starting PyGame: `python3 -m pygame.examples.aliens`


### Best Practice Bonus Points
- [] Test Coverage
- [] Pythonic best-practices

### Checklist
- [] Game starts as expected
- [] Game is playable with moving characters 
- [] Collision events work as expected
- [] Player wins and game ends
- [] Player loses and game ends
- [] Endgame state
- [] Level progression
- [] Random bonuses


### Extensions in the form of future PRs
- Colour Customisation
- Deployed exectuable
- Reinforcement Learning algorithm 