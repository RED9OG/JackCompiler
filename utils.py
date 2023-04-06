import os
from LexicalElements import symbols


def getFiles(arg):
    files = []
    if arg.endswith('.jack'):
        files.append(arg)
    elif os.path.exists(arg):
        for x in os.listdir(arg):
            files.append(f'{arg}/{x}')
    return files

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
        

