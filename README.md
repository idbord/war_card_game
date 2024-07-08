# War Card Game Simulation

This project simulates the card game "War" to determine how many iterations it takes to complete the game. The purpose of this project arose from curiosity after playing a few games with my girlfriend and wondering about the average length of the game.

## Project Structure

```
war_card_game/
│
├── README.md
├── requirements.txt
├── simulations.py
└── src/
    ├── __pycache__/
    │   ├── card.cpython-311.pyc
    │   ├── deck.cpython-311.pyc
    │   ├── player.cpython-311.pyc
    │   └── war_game.cpython-311.pyc
    ├── card.py
    ├── deck.py
    ├── player.py
    └── war_game.py
```

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine

### 2. Set Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. Here are the steps to set up a virtual environment using `venv`:

#### On Windows

```sh
python -m venv venv
venv\Scripts\activate
```

#### On macOS and Linux

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### 4. Run the Simulations

To run the simulations and analyze the iterations it takes to complete the game, execute the `simulations.py` script:

```sh
python simulations.py
```

This will run 100,000 simulations of the War card game and display a histogram of the number of iterations required to complete each game, along with some statistical data.

## Project Components

### Main Code

- **src/card.py**: Defines the `Card` class.
- **src/deck.py**: Defines the `Deck` class.
- **src/player.py**: Defines the `Player` class.
- **src/war_game.py**: Defines the `WarGame` class where the main game logic is implemented.
- **simulations.py**: Script to run the simulations and plot the results.

## Analyzing the Results

The script will print the following statistical data about the iterations:

- Mean iterations
- Median iterations
- Standard deviation
- Highest iterations
- Lowest iterations

It will also display a histogram showing the distribution of the number of iterations across 100,000 games.
