import os
from LexicalElements import symbol


def getFiles(arg):
    files = []
    if arg.endswith('.jack'):
        files.append(arg)
    elif os.path.exists(arg):
        for x in os.listdir(arg):
            files.append(f'{arg}/{x}')
    return files


def tokenizer(linesOfCode):
    arr = []
    string = ''
    for x in linesOfCode:
        if x.startswith('//') or x == '':
            pass
        elif x.find('//') != -1:
            index = x.find('//')
            newx = x[:index]
            arr.append(newx)
        else:
            arr.append(x)

    for x in arr:
        string = string + x
    for x in symbol:
        if string.find(x):
            index = string.find(x)

            string = string[:index] + ' ' + string[index:]
    print(string)
