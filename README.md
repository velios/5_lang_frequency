# Frequency Analysis of Words

The script count the most used words in the text

# Running on linux
To analyze a single file, type
$ python lang_frequency.py filename.txt -c 6
For multiple files
$ python lang_frequency.py filename1.txt filename2.txt -c 6
or use wildcards
$ python lang_frequency.py *.txt -c 6

# Output:
Список 6 самых часто используемых слов в файле filename.txt
[('и', 2101),
 ('в', 1814),
 ('Гарри', 1607),
 ('не', 1378),
 ('на', 1232),
 ('что', 1071)]


Running on Windows in the same way

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
