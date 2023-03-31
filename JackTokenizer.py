import utils

from LexicalElements import symbols
from LexicalElements import keyword 



class JackTokenizer(object):
    def __init__(self, file):
        self.file = file
        self.start()

    def start(self):
        file = open(self.file, 'r')

        lines = self.tokenizer(file.read().splitlines())
        return lines
       
    def tokenizer(self,linesOfCode):
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
    
    def tokenType(token):
        returnValue = ''
        if token in keyword:
            returnValue = 'KEYWORD'
        elif token in symbols:  
            returnValue = 'SYMBOL'
           
                 

    def keyWord(arg):
        pass

    def symbol(arg):
        pass
    
    def identifier(arg):
        pass
    
    def intVal(arg):
        pass
    
    def stringVal(arg):
        pass
    
   

