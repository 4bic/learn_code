import sys
import string

def word_count():
    word_counts = {} #initialize an empty dictionary
    # cycle through lines of input
    for line in sys.stdin:
        # create an array of words
        data = line.strip().split(" ")

        for i in data:
            key = i.translate(string.maketrans("",""),string.punctuation).lower()
            if key in word_counts.key():
                word_counts[key] += 1
            else:
                word_counts[key] = 1

        print word_counts


word_count()
