__author__ = 'johnfulgoni'

import main
import csv
import sys
import math

def process_file(filename):

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

if __name__ == '__main__':
    main.main()