import os
import argparse
import string
import re
import pprint
from collections import Counter


def load_data_from_file(filepath, encoding='utf-8'):
    if not os.path.exists(filepath):
        print('Неверное имя или файл "{0}" не существет'.format(filepath))
        return None
    with open(filepath, "r", encoding=encoding) as data_file:
        return data_file.read()


def make_words_list_from_text(text):
    pass



def get_most_frequent_words(text):
    pass


def configurate_cmd_parser():
    parser_description = """
    Скрипт на вход принимает файл с текстом и выводит в консоль 10 самых популярных слов в порядке убывания частоты 
    Файл для примера можно скачать в библиотеке Мошкова http://lib.ru
    """
    cmd_argument_parser = argparse.ArgumentParser(description=parser_description)
    cmd_argument_parser.add_argument('filepath', help='Файл с текстом', type=str)
    return cmd_argument_parser.parse_args()


if __name__ == '__main__':
    data_from_file = load_data_from_file('Garri_Potter_i_uznik_Azbakana_(Garri_Potter_-_3).txt')
    # words_list = re.split(r"[\s,.!?:]+", data_from_file)
    # print(words_list)
    # string_without_punctuation = data_from_file.translate string.punctuation)
    # print(Counter(words_list).most_common(10))
    # Program to all punctuation from the string provided by the user

    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # remove punctuation from the string
    no_punct = ""
    for char in data_from_file:
        if char not in punctuations:
            no_punct = no_punct + char

    # display the unpunctuated string
    pprint.pprint(Counter(no_punct.lower().split()))