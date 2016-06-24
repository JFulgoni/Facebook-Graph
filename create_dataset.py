__author__ = 'johnfulgoni'

import main
import csv
import sys
import math

def import_raw_file(filename):
    data = []
    counter = 0
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
        for row in csvreader:
            if should_continue(row):
                continue
            data.append(row[0])
            counter += 1

            # if counter > 10:
            #     break

    csvfile.close()
    # print "Number of Friends: " + str(counter)
    # print data
    return data

def should_continue(row):
    if (not row) or (row[0] == 'FriendFriends') or ('friends' in row[0]):
        return True

def anonymize_data(key_list, data, name):
    values = key_list.values()
    keys = key_list.keys()
    if len(values) < 1:
        max_value = -1
    else:
        max_value = max(values)

    if name not in values:
        max_value += 1
        key_list[name] = max_value

    for friend in data:
        if friend not in values:
            max_value += 1
            key_list[friend] = max_value

    return key_list

if __name__ == '__main__':
    main.main()