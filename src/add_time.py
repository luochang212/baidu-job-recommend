#-*- coding:utf-8 -*-

"""add timestamp for each job
   last update: 2020-06-18
"""

import datetime

def read_data(file_name):
    """read and process data."""
    with open(file_name, 'r') as f:
       lst = f.read().split('\n')

    for i, e in enumerate(lst):
        if not e or e[0] == '#' or e[0] != '-':
            continue
        if e[-1] != ']':
            lst[i] += ' [' + str(datetime.date.today()) + ']'

    with open(file_name, 'w') as f:
        f.write("\n".join(lst))


if __name__ == '__main__':
    file_name = "../data/技术.md"
    read_data(file_name)
