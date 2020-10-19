#!/usr/bin/python3

import sys

def emit(key, value):
    sys.stdout.write('{}\t{}\n'.format(key, value))

def map(line):
    objects = line.split(', ')
    (ip, userid, country, bannerid, payout) = objects
    emit(country, payout)

def main():
    for line in sys.stdin:
        map(line.strip())

if __name__ == '__main__':
    main()
