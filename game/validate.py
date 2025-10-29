def is_valid_guess(guess: str, length: int) -> tuple[bool, str]:
    if len(guess)!=length:
        print("you need",length,"digits unique")
        return False
    for i in range(len(guess)-1):
        if guess[i]==guess[i+1]:
            print("you need",length,"digits unique")
            return False
    try:
        guess=int(guess)
    except:
        print("you need",length,"digits unique")
        return False
    return True

def is_new_guess(guess: str, seen: set[str]) -> bool:
    return str(guess) not in seen

        