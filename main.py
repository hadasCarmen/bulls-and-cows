from game.io import *
from game.logic import *
from game.secret import *
from game.validate import *



def play(length: int = 4, max_tries: int | None = 12) -> None:
    if __name__ == "__main__":
        
        secret=generate_secret(length)
        state=init_state(secret,length,10)
        while not is_lose(state):
            guess=prompt_guess(length)
            while not is_valid_guess(guess,length) or not is_new_guess(guess,state["seen"]):
                guess=prompt_guess(length)
            apply_guess(state,guess)
            bulls=state["history"][-1][1]
            cows=state["history"][-1][2]
            if is_won(bulls,length):
                break
            print_feedback(guess,bulls,cows)
            print_status(state)
        print_result(state)
        
        return
play(4,5)

            
        
