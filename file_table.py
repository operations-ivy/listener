import os
import pandas as pd

root_path = '/srv'

for root, dirs, files in os.walk(root_path):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
