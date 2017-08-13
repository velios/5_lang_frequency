import os
import argparse
import string
from collections import Counter


def load_data_from_file(filepath, encoding='utf-8'):
    if not os.path.exists(filepath):
        print('Неверное имя или файл "{0}" не существет'.format(filepath))
        return None
    with open(filepath, "r", encoding=encoding) as data_from_file:
        return data_from_file.read()


def remove_punctuation_from_string(raw_string):
    string_without_punctuation = ""
    for char in raw_string:
        if char not in [string.punctuation, '—', '«', '»', '…', '-', ',', '.']:
            string_without_punctuation = string_without_punctuation + char
    return string_without_punctuation


def make_words_list_from_string(raw_string):
    return raw_string.lower().split()


def get_most_frequent_words(words_list, number_of_results=10):
    return Counter(words_list).most_common(number_of_results)


def configurate_cmd_parser():
    parser_description = ("\n"
                          "    Скрипт на вход принимает файл с текстом и выводит в консоль <n> самых популярных слов в порядке убывания частоты \n"
                          "    Файл для примера можно скачать в библиотеке Мошкова http://lib.ru \n"
                          "    ")
    arguments_from_cmd = argparse.ArgumentParser(description=parser_description)
    arguments_from_cmd.add_argument('filepaths', help='Файл с текстом', type=str, nargs='+')
    arguments_from_cmd.add_argument('-c', '--count', type=int, default=10,
                                    help='Сколько часто употребляемых слов надо выводить. 10 по умолчанию.')
    return arguments_from_cmd.parse_args()


def output_frequency_result_to_console(most_frequent_words_list):
    for index, word in enumerate(most_frequent_words_list):
        print('{0:4}  {1:15} {2:6}'.format(index + 1, word[0], word[1]))


if __name__ == '__main__':
    cmd_arguments = configurate_cmd_parser()

    for filepath in cmd_arguments.filepaths:
        data_from_file = load_data_from_file(filepath)
        most_frequent_words_list = get_most_frequent_words(
            make_words_list_from_string(
                remove_punctuation_from_string(data_from_file)), number_of_results=cmd_arguments.count)
        print('\nСписок {} самых часто используемых слов в файле {}\n'.format(cmd_arguments.count,
                                                                              os.path.basename(filepath)))
        output_frequency_result_to_console(most_frequent_words_list)
