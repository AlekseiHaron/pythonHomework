from datetime import datetime
import csv
from collections import Counter


###################1 draft#########################################
words = []
words_counted = []
letter = []
count_uppercase = 0
count_uppercase = []

with open('output.csv', 'w') as csvfile:
    file = open(r'C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\test.txt')
    read_data = file.read().lower().split()
    # print(read_data)
    writer = csv.writer(csvfile)
    # print(read_data)
    for i in read_data:
        x = read_data.count(i)
        words_counted.append(f"{i}-{x}")
    writer = csv.writer(csvfile, delimiter='\n')
    writer.writerow(words_counted)
    print(words_counted)

# s = ['BuckyBarnes@123', 'qwerty']
# # res = "".join([ch for ch in s if ch.isalpha()])
# # print(res)
# # keep only letters
# res = []
# resres = []
# for ch in s:
#     for chch in ch:
#         if chch.isalpha():
#             ch.append(chch)
#         # res += ch
#     res.append(ch)
# print(res)


# with open('output.csv', 'w') as csvfile:
#     file = open(r'C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\test.txt')
#     read_data = file.read().lower().split()
#
#     # writer = csv.writer(csvfile)
#     print(read_data)
#     for i in read_data:
#         x = read_data.count(i)
#         # words_counted.append((i, x))
#         writer = csv.writer(csvfile, delimiter='-')
#         writer.writerow([i, x])
###############################################



# with open('output.csv', 'w', newline = '') as csvfile:
#     file = open(r'C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\test.txt')
#     headers = ['letter', 'cout_all', 'count_uppercase']
#     read_data = file.read()
#     # abc
#     # set
#     read_data = ''.join(read_data.split())
#     print(read_data)
#     # writer = csv.writer(csvfile)
#     for i in read_data:
#         x = read_data.count(i)
#         if i.isupper():
#             # y = i.count(i)
#             count_uppercase += 1
#             # count_uppercase.append(y)
#
#         # writer = csv.writer(csvfile, delimiter='\n')
#         words_counted.append(f"{i}-{x}")
#     # writer = csv.writer(csvfile, delimiter='\n')
#     # count_all = len(read_data)  переделать
#     writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='|')
#     writer.writeheader()
#     writer.writerow({'letter': words_counted, 'count_all': count_all, 'count_uppercase': count_uppercase})
#     print(count_uppercase)


# with open('output.csv', 'w', newline='') as csvfile:
#     file = open(r'C:\Users\Oleksii_Kushnir\PycharmProjects\pythonHomework\test.txt')
#     headers = ['letter', 'count_all', 'count_uppercase']
#     read_data = file.read()
#     read_data = ''.join(read_data.split())
#
#     for i in read_data:
#         x = read_data.count(i)
#         # writer = csv.writer(csvfile, delimiter='\n')
#         letter.append(i)
#         words_counted.append(x)
#
#         if i.isupper():
#             print(i)
#             y = i.count(i)
#             count_uppercase.append(y)
#
#     count_all = len(read_data)
#     writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='|')
#     writer.writeheader()
#     writer.writerow({'letter': letter, 'count_all': words_counted, 'count_uppercase': count_uppercase})