import csv

print('\n\n\n\n\n')

with open('spreadsheet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    classes = []
    for row in csv_reader:
        if line_count == 0:
            for x in range(1, len(row)):
                classes.append(row[x])
            # print(classes)
            line_count += 1
        else:
            for x in range(0, len(row)-2):
                if row[x+1] == '':
                    value = str(0)
                else:
                    value = str(row[x+1])
                string = '(ClassSkillValue ' + str(classes[x]) + 'Class ' + str(row[0]) + 'Skill ' + value + ')'
                print(string)
            line_count += 1
    print('\n\n\n\n\n')
    print(f'Processed {line_count} lines.')
