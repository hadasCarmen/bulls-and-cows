def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls=0
    cows=0
    for i in range(len(secret)):
        if int(guess[i])==secret[i]:
            bulls+=1
        elif int(guess[i]) in secret:
            cows+=1
    return bulls,cows

def is_won(bulls: int, length: int) -> bool:
    return bulls==length

def is_lose(state):
    return state[ "tries_used"]>=state[ "max_tries"]

def init_state(secret: str, length: int, max_tries: int | None):
    seen=set()
    return {
            "secret":secret,
            "length":length,
            "max_tries":max_tries,
            "tries_used":0,
            "history":[ ],
            "seen":seen
            }
# state=init_state(1234,4,10)
# guess=2574
def apply_guess(state, guess: str) -> tuple[int, int]:
    state["tries_used"]+=1
    secret=state["secret"]
    bulls_cows=score_guess(secret,guess)
    bulls=bulls_cows[0]
    cows=bulls_cows[1]
    state["history"].append((guess,bulls,cows))
    state["seen"].add(str(guess))
    return




