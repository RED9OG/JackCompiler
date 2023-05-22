import utils

from LexicalElements import symbols
from LexicalElements import keyword 



class JackTokenizer(object):
    tokenizedData = []
    
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
            if x.startswith('//') or x == '' or x.startswith('/'):
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
                
                    index = code.find(symbol) 
                    newCode = code[:index] + ' ' + symbol + ' ' + code[index+1:]
                    code = newCode
            temp.append(newCode) 
 
 
    
        for x in temp:
            string = string + x
        for x in string.split(" "):
            obj = {'tokenType': self.tokenType(x)}
    
            if self.tokenType(x) == 'KEYWORD':
                obj['keyword'] = self.keyWord(x)
            elif self.tokenType(x) == 'SYMBOL':
                obj['symbol'] = self.symbol(x)
            elif self.tokenType(x) == 'IDENTIFIER':
                obj['identifier'] = self.identifier(x)
            elif self.tokenType(x) == 'INT_CONST':
                obj['intVal'] = self.intVal(x)
            elif self.tokenType(x) == 'STRING_CONST':
                obj['stringVal'] = self.stringVal(x) 
            if x != '':
                
                tokenized.append(obj)
                
            else:
                pass
    
        self.tokenizedData = tokenized
    
    def tokenType(self,token):
        numbers = '0123456789'
        returnValue = ''
        
        if token in keyword:
            returnValue = 'KEYWORD'
        elif token in symbols:  
            returnValue = 'SYMBOL'
        elif token.isnumeric():
            returnValue = 'INT_CONST'
        elif token.startswith('"') and token.endswith('"'):
            returnValue = 'STRING_CONST'
        else:
            returnValue = 'IDENTIFIER'
        return returnValue

            
    def symbol(self,arg):
        return arg
        
    
    def identifier(self,arg):
        return arg
       
        
    
    def intVal(self,arg):
        return arg
    
    
    def stringVal(self,arg):
        return arg
        
              
    def keyWord(self,arg):
        returnValue = ''
        if arg == 'constructor':
            returnValue = 'CONSTRUCTOR'
        elif arg == 'class':
            returnValue = 'CLASS'
        elif arg == 'method':
            returnValue = 'METHOD'
        elif arg == 'function':
            returnValue = 'FUNCTION'
        elif arg == 'boolean':
            returnValue = 'BOOLEAN'
        elif arg == 'char':
            returnValue = 'CHAR'
        elif arg == 'void':
            returnValue = 'VOID'
        elif arg == 'static':
            returnValue = 'STATIC'
        elif arg == 'field':
            returnValue = 'FIELD'
        elif arg == 'let':
            returnValue = 'LET'
        elif arg == 'do':
            returnValue = 'DO'
        elif arg == 'if':
            returnValue = 'IF'
        elif arg == 'else':
            returnValue = 'ELSE'
        elif arg == 'while':
            returnValue = 'WHILE'
        elif arg == 'return':
            returnValue = 'RETURN'
        elif arg == 'true':
            returnValue = 'TRUE'
        elif arg == 'false':
            returnValue = 'FALSE'
        elif arg == 'null':
            returnValue = 'NULL'
        elif arg == 'this':
            returnValue = 'THIS'
        elif arg == 'int':
            returnValue = 'INT'
        elif arg == 'var':
            returnValue = 'VAR'
            
        else:
            returnValue = ''
        return returnValue
            
              
  
