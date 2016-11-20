from collections import Counter
import re


def load_data(filepath):
    with open(filepath, 'r') as reader:
        raw_data = reader.readlines()
    text = str()
    for line in raw_data:
        text += line.lower()
    return text.replace('\n', '')


def get_most_frequent_words(text):
    counter = Counter(re.findall('\w+', text))
    return counter.most_common(10)


if __name__ == '__main__':
    text = load_data(input('Path to the text file: '))
    print('Up to 10 top words in given text:')
    for word, frequency in get_most_frequent_words(text):
        print('{0}: {1}'.format(word, frequency))
