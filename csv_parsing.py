from datetime import datetime
import csv


class CSVParsing:

    def __init__(self):
        pass

    #################### 1 ###########################
    def file_to_csv_first(self):
        words = []
        with open('output_first.csv', 'w') as csvfile:
            file = open(r'test.txt')
            read_data = file.read().lower().split()
            # print(read_data)
            writer = csv.writer(csvfile)
            # print(read_data)
            for i in read_data:
                x = read_data.count(i)
                words.append(f"{i}-{x}")
            writer = csv.writer(csvfile, delimiter='\n')
            writer.writerow(words)
            print(f'First task parsing:\n{words}\n')

    #################### 2 ###########################
    def file_to_csv_second(self):

        words_counted = []
        words_counted_all = []
        percentage = []
        # letter = []
        count_uppercase = 0
        # cnt_uppercase = []
        with open('output_second.csv', 'w', newline='') as csvfile:
            file = open(r'test.txt')
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            read_data = file.read()
            # abc
            new_read_data = ''
            for letter in read_data:
                for ch in letter:
                    if ch.isalpha():
                        new_read_data += ch

            count_all = len(new_read_data)
            # print(new_read_data)

            for i in new_read_data:
                x = new_read_data.count(i)
                if i.isupper():
                    count_uppercase += 1
                words_counted.append(i)
                words_counted_all.append(x)
                percentage.append(x / count_all * 100)

            # words_counted = set(words_counted)
            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='\n')
            writer.writeheader()
            writer.writerow(
                {'letter': words_counted, 'count_all': words_counted_all, 'count_uppercase': count_uppercase,
                 'percentage': percentage})
            print(f'Second task parsing:\n'
                  f'letter: {words_counted} \ncount_all: {words_counted_all} \ncount_uppercase: {count_uppercase}'
                  f'\npercentage: {percentage}')
