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
        
def tokenizer(linesOfCode):
    arr = []
    temp = []
    tokenized = []
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

    for code in arr:
        newCode = ""
        for symbol in symbols:
            if code.find(symbol) != -1:
                # print(code.find(symbol),symbol,code)
                index = code.find(symbol) 
                newCode = code[:index] + ' ' + symbol + ' ' + code[index+1:]
                code = newCode
        temp.append(newCode) 
  
    
    for x in temp:
        string = string + x
    for x in string.split(" "):
        if x != '':
            tokenized.append(x)
        else:
            pass
            
    return tokenized
