import sys
import random


def guess(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_guess():
        nonlocal name
        nonlocal player_wins
        
        player_guess = input(f"Hey {name}, guess which number I'm thinking of...1, 2, or 3.\n\n")

        if player_guess not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2 or 3.")   
            return play_guess() 
        
        computer_thought = random.choice("123")
        
        print(f"\n{name}, you chose {player_guess}.")
        print(f"I was thinking about the number {computer_thought}.\n")

        player = int(player_guess)
        computer = int(computer_thought)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"Weldone {name}, you win! 🎉"
            else:
                return f"Sorry {name}, better luck next time 🥲"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:    
            play_again = input(f"\n(Y) for Yes or \n(Q) to Quit\n")  
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if play_again.lower() == "y":
            return play_guess()
        else:
            print(f"\n 🎉🎉🎉")
            print(f"Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    return play_guess


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )
    args = parser.parse_args()

    guess_my_number = guess(args.name)
    guess_my_number()
        


            













