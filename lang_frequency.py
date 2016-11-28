from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, 'r') as reader:
        raw_data = reader.read()
    return raw_data


def prepare_data(text):
    if not text:
        print('Given file is empty!')
        sys.exit(0)
    words = re.findall('\w+', text)
    cooked_words = [word.lower() for word in words]
    return cooked_words


def get_most_frequent_words(words_list, top_frequent=10):
    counter = Counter(words_list)
    return counter.most_common(top_frequent)


if __name__ == '__main__':
    text = load_data(input('Path to the text file: '))
    words_list = prepare_data(text)
    top_words = get_most_frequent_words(words_list)
    print('Up to 10 top words in given text:\n')
    for word, frequency in top_words:
        print('\'{0}\', {1} occurances'.format(word, frequency))
