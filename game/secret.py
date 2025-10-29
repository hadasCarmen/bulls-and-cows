import random
def generate_secret(length: int = 4):
    numbers=random.sample(range(1,9),length)
    return numbers
# generate_secret(4)
