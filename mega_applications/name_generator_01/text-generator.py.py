import string, random

# establish vowels and consonants
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase

# user input to select either vowels or consonants
letter_input_1=raw_input("What letter would you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:  ")
letter_input_2=raw_input("What letter would you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:  ")
letter_input_3=raw_input("What letter would you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:  ")
letter_input_4=raw_input("What letter would you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter:  ")

print (letter_input_1+letter_input_2+letter_input_3+letter_input_4)

def generator():
    # pick a random letter for first letter
    if letter_input_1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letter)
    else:
        letter1 = letter_input_1
    # second letter
    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letter)
    else:
        letter2 = letter_input_2
    # third letter
    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letter)
    else:
        letter3 = letter_input_3
    # fourth letter
    if letter_input_4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input_4 == 'c':
        letter4 = random.choice(consonants)
    elif letter_input_4 == 'l':
        letter4 = random.choice(letter)
    else:
        letter4 = letter_input_4
    # conjoin 4 letters to foem a name
    name = letter1 + letter2 + letter3 + letter4

    return (name)

print(generator())
