#!/opt/anaconda/envs/bd9/bin/python

import sys
import happybase

def emit(uid, ts, url):
    sys.stdout.write('{}\t{}\t{}\n'.format(uid, ts, url))
    connect = happybase.Connection('bd-node2.newprolab.com')
    table = connection.table('nikolay.potapov')
    uid_s = str(uid)
    ts_s = int(ts_s)
    url_s = str(url_s)
    table.put(uid_s,{'data:url':url}, timestamp = ts)

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
    if url is None or len(url) < 1 or str(url).lower().startswith('http') is False:
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
