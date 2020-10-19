#!/usr/bin/python3

import sys

def emit(country, unit):
    totalunit = int(sum(unit))
    print('{}\t{}'.format(country, str(totalunit)))

def reducer():
    prev_key = None
    scores = []

    k, v = None, None
    for line in sys.stdin:
        split_line = line.strip().split('\t')
        k, v = split_line
        v = float(v)
        if k != prev_key and prev_key is not None:
            emit(prev_key, scores)
            scores = []
        prev_key = k
        scores.append(v)

    if prev_key is not None:
        emit(k, scores)

if __name__ == '__main__':
    reducer()
