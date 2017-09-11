import random, string

def generator():
    # pick a random letter
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    # conjoin 4 letters to foem a name
    name = letter1 + letter2 + letter3 + letter4

    return (name)

print(generator())
