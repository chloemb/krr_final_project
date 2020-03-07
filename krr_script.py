import csv

# print('\n\n\n\n\n')
#
# with open('spreadsheet.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     classes = []
#     for row in csv_reader:
#         # noinspection PyInterpreter
#         if line_count == 0:
#             for x in range(1, len(row)):
#                 classes.append(row[x])
#             # print(classes)
#             line_count += 1
#         else:
#             for x in range(0, len(row)-1):
#                 if row[x+1] == '':
#                     value = str(1)
#                 else:
#                     if int(row[x+1]) < 50:
#                         value = str(int(row[x+1]))
#                     else:
#                         value = str(row[x+1])
#                 string = '(ClassSkillValue ' + str(classes[x]) + 'Class ' + str(row[0]) + 'Skill ' + value + ')'
#                 print(string)
#             line_count += 1
#     print('\n\n\n\n\n')
#     print(f'Processed {line_count} lines.')

print('\n\n\n\n\n')

with open('word_bank.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    classes = []
    for row in csv_reader:
        for word in row:
            if word is not ' ' and word is not '\t' and word is not '\n':
                print(word)
            line_count += 1
    print('\n\n\n\n\n')
    print(f'Processed {line_count} lines.')
