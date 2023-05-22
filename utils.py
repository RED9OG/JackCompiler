import os
import sys
from LexicalElements import symbols
from CompilationEngine import CompilationEngine


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

def handleKeyword(index,keyword,error,tokens):
    if tokens[index]['tokenType'] == 'KEYWORD' and tokens[index]['keyword'] == keyword: 
        CompilationEngine.xml.append('<keyword>') 
        CompilationEngine.xml.append(tokens[index]['keyword'].lower())
        CompilationEngine.xml.append('</keyword>')
    else:
        print(CompilationEngine.xml)
        
        sys.exit(f'Error:{error}')
        

def handleSymbol(index,symbol,error,tokens):
    if tokens[index]['tokenType'] == 'SYMBOL' and tokens[index]['symbol'] == symbol: 
        CompilationEngine.xml.append('<symbol>') 
        CompilationEngine.xml.append(tokens[index]['symbol'].lower())
        CompilationEngine.xml.append('</symbol>')
    else:
        print(CompilationEngine.xml)
        sys.exit(f'Error:{error}')
        
def handleIdentifier(index,error,tokens):
    if tokens[index]['tokenType'] == 'IDENTIFIER': 
        CompilationEngine.xml.append('<identifier>') 
        CompilationEngine.xml.append(tokens[index]['identifier'])
        CompilationEngine.xml.append('</identifier>')
    else:
        print(CompilationEngine.xml)
        sys.exit(f'Error:{error}')
        
def handleType(index,error,tokens):
    if tokens[index]['tokenType'] == 'KEYWORD' and tokens[index]['keyword'] == 'INT':
        CompilationEngine.xml.append('<keyword>') 
        CompilationEngine.xml.append(tokens[index]['keyword'].lower())
        CompilationEngine.xml.append('</keyword>')
    elif tokens[index]['tokenType'] == 'KEYWORD' and tokens[index]['keyword'] == 'CHAR':
        CompilationEngine.xml.append('<keyword>') 
        CompilationEngine.xml.append(tokens[index]['keyword'].lower())
        CompilationEngine.xml.append('</keyword>')
    elif tokens[index]['tokenType'] == 'KEYWORD' and tokens[index]['keyword'] == 'BOOLEAN':
        CompilationEngine.xml.append('<keyword>') 
        CompilationEngine.xml.append(tokens[index]['keyword'].lower())
        CompilationEngine.xml.append('</keyword>')
    elif tokens[index]['tokenType'] == 'IDENTIFIER':
        CompilationEngine.xml.append('<identifier>') 
        CompilationEngine.xml.append(tokens[index]['keyword'].lower())
        CompilationEngine.xml.append('</identifier>')
 
    else:
        print(CompilationEngine.xml)
        sys.exit('Error:type not defined')
        
def handleIdentifier(index,error,tokens):
    if tokens[index]['tokenType'] == 'IDENTIFIER': 
        CompilationEngine.xml.append('<identifier>') 
        CompilationEngine.xml.append(tokens[index]['identifier'].lower())
        CompilationEngine.xml.append('</identifier>')
    else:
        print(CompilationEngine.xml)
        sys.exit(f'Error:{error}')
     
