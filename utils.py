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
        
def objectMaker(code):
    obj = {'tokenType': tokenType(code)}
    if obj['tokenType'] == 'KEYWORD':
        obj = {'tokenType':obj['tokenType'],'keyWord':self.key}
        
    elif obj['tokenType'] == 'SYMBOL':
        pass
    elif obj['tokenType'] == 'IDENTIFIER':
        pass
    elif obj['tokenType'] == 'STRING_CONST':
        pass
    elif obj['tokenType'] == 'INT_CONST':
        pass
    
   return obj
    
    

