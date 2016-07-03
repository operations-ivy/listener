import os
import pandas as pd

root_path = '/srv'
nfs_exports = ['movies', 'tv']
names = []

for export in nfs_exports:
    for root, dirs, files in os.walk(root_path):
        for name in files:
            names.append(name)
        #print(os.path.join(root, name))
    #for name in dirs:
        #print(os.path.join(root, name))

print names
