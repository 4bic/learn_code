import sys
import string

def mapper():
    word_counts = {} #initialize an empty dictionary
    # cycle through lines of input
    for line in sys.stdin:

        # tokenize line of data
        data = line.strip.split(" ")

        for i in data:
            # clean the data
            cleaned_data = i.translate(string.maketrans("","",string.punctuation).lower)
            # emit a key-value pair
            print "{0}\t{1}".format(cleaned_data, 1)

mapper()
