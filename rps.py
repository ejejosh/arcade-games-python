import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

    
        player_choice = input(f"\n{name} please enter...\n1 for Rock, \n2 for Paper, \nor 3 for Scissors: \n\n")

        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, you please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print(f"\n{name} you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player != computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                computer_wins +=  1
                return f"🖥️ Computer wins\nSorry, {name}...😢"
            

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nComputer wins: {computer_wins}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉")
            print("Thank you for playing")
            if __name__ == "__main__":        
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
    