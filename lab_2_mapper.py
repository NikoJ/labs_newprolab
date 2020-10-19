#!/opt/anaconda/envs/bd9/bin/python

import sys
import happybase

def emit(uid, ts, url):
    sys.stdout.write('{}\t{}\t{}\n'.format(uid, str(ts), url)) # for check on hdfs
    connect = happybase.Connection('bd-node2.newprolab.com')
    table = connect.table('nikolay.potapov')
    table.put(uid, {'data:url':url}, ts)

def map(line):
    objects = line.split("\t")
    if len(objects) != 3:
        return None
    (uid, timestamp, url) = objects
    # validate
    if uid is None or len(uid) < 5 or str(uid).isdigit() is False:
        return None
    if timestamp is None or len(timestamp) < 5 or is_float(timestamp) is False:
        return None
    if url is None or len(url) < 5 or str(url).lower().startswith('http') is False:
        return None
    # check uid
    if int(uid) % 256 != 154:
        return None
    # convert timestamp
    timestamp = int(float(timestamp) * 1000)
    emit(uid, timestamp, url)

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
