#!/usr/bin/python3

import sys

def emit(key, value):
    sys.stdout.write('{}\t{}\n'.format(key, value))

def map(line):
    objects = line.split("\t")
    if len(objects) != 3:
        return None
    (uid, timestamp, url) = objects
    # validate
    if uid is None or len(uid) < 1 or str(uid).isdigit() is False:
        return None
    if url is None or len(url) < 1 or str(url).lower().startswith('http') is False:
        return None
    emit(url, 1)

def main():
    for line in sys.stdin:
        map(line.strip())

def is_float(ts):
    try:
        float(ts)
        return True
    except ValueError:
        return False
        
if __name__ == '__main__':
    main()
