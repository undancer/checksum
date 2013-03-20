__author__ = 'undancer'

import os
import hashlib


def md5hash(path):
    with open(path, 'rb', 2 * 1024 * 1024) as f:
        return hashlib.md5(f.read()).hexdigest()


for root, dirs, files in os.walk('/share/data', True):
    for name in files:
        path = os.path.join(root, name)
        checksum = md5hash(path)
        if name != checksum:
            print("name : " + name + " -> hash:" + checksum)
print('done.')
