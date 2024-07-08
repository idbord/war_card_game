import asyncio
import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np
from src.war_game import WarGame
from src.player import Player
from src.deck import Deck

async def run_game(executor):
    loop = asyncio.get_running_loop()
    iterations = []

    def play_war_game():
        deck = Deck()
        deck.shuffle()
        player1 = Player(name="Player 1", hand=deck.cards[:26])
        player2 = Player(name="Player 2", hand=deck.cards[26:])
        warGame = WarGame(player1, player2)
        warGame.play()
        return warGame.iteration

    futures = [loop.run_in_executor(executor, play_war_game) for _ in range(1_000_000)]
    for future in asyncio.as_completed(futures):
        iterations.append(await future)

    return iterations

def analyze_and_chart_iterations(iterations):
    mean_iterations = np.mean(iterations)
    median_iterations = np.median(iterations)
    std_iterations = np.std(iterations)
    highest = np.max(iterations)
    lowest = np.min(iterations)

    print(f"Mean iterations: {mean_iterations}")
    print(f"Median iterations: {median_iterations}")
    print(f"Standard deviation: {std_iterations}")
    print(f"Highest iterations: {highest}")
    print(f"Lowest iterations: {lowest}")

    plt.hist(iterations, bins=25, edgecolor='black')
    plt.title('Distribution of War Game Iterations')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Frequency')
    plt.axvline(mean_iterations, color='r', linestyle='dashed', linewidth=1, label=f'Mean: {mean_iterations:.2f}')
    plt.axvline(median_iterations, color='g', linestyle='dashed', linewidth=1, label=f'Median: {median_iterations:.2f}')
    plt.axvline(mean_iterations + std_iterations, color='b', linestyle='dashed', linewidth=1, label=f'Standard Deviation: {std_iterations:.2f}')
    plt.axvline(mean_iterations - std_iterations, color='b', linestyle='dashed', linewidth=1)
    plt.legend()
    plt.show()

async def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        iterations = await run_game(executor)
    analyze_and_chart_iterations(iterations)

if __name__ == '__main__':
    # time how long it takes to run the main function
    import time
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time taken: {end - start} seconds")
