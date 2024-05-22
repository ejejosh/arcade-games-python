from rps import rps
from guess_number import guess
import sys


def play_game(name="playerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        player_choice = input(f"Please chose a game:\n1 = Rock Paper Scissors \n2 = Guessing My Number\n\n Or press \"X \" to Exit the Arcade\n\n")

        if player_choice not in ["1", "2", "x"]:
            print(f"\{name}, please enter 1, 2, or X.")
            return play_game(name)
        
        welcome_back = True
        
        if player_choice == "1":
            rock_paper_scissors =  rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_my_number = guess(name)
            guess_my_number()
        else:
            print(f"\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(
        description="Personalize gaming experience"
    )

    parse.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parse.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🎮")

    play_game(args.name)    


