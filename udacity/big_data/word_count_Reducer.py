import sys


def reducer():
    word_count = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, count = data

        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, word_count)
            word_count = 0

        old_key = this_key
        word_count += float(count)

    if old_key != None:
        print "{0}\t{1}".format(old_key, word_count)

if __name__ == '__main__':
    reducer()
# to run locally the MapReduce function
 # $ cat ./data/man_in_arena.txt | python big_data/word_count_with_Mapper.py | sort | python big_data/word_count_Reducer.py
