import pprint
from game.logic import *
def prompt_guess(length: int) -> str:
    guess=input(f"write your guess  {length}  digits: ")
    return guess

def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print("in guess:",guess,"your bulls:",bulls,"your cows:",cows)
    return

def print_status(state) -> None:
    pprint.pprint(state["history"])
    print("and now tour guess:",state["history"][-1])
    return

def print_result(state) -> None:
    if is_won(state["history"][-1][1],state["length"]):
        print("you win the secret number is:",state["secret"])
        print("you try:",state["tries_used"],"times.well done")
        return
    print("you lose the secret number is:",state["secret"])
    print("you try:",state["tries_used"],"times.maybe next time")
    return

