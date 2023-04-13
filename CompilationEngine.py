import sys
class CompilationEngine(object):
    xml = []
    def __init__(self,tokenizedData):
        self.tokenizedData = tokenizedData
        self.CompileClass(tokenizedData)
        print(CompilationEngine.xml)
       
 


    def CompileClass(self,tokens):
       
       
        temp = []
        CompilationEngine.xml.append("<class>")
        
       
        
        if tokens[0]['tokenType'] == 'KEYWORD':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append('class')
            CompilationEngine.xml.append('</keyword>')
       
        else:
            sys.exit('ERROR:class keyword not found')
                   
        if tokens[1]['tokenType']  == 'IDENTIFIER':
            CompilationEngine.xml.append('<identifier>') 
            CompilationEngine.xml.append(tokens[1]['identifier'])
            CompilationEngine.xml.append('</keyword>')
        else:
            sys.exit('ERROR:Wrong identifier or not written classname')
             
             
             
        if tokens[2]['tokenType']  == 'SYMBOL':
            CompilationEngine.xml.append('<symbol>') 
            CompilationEngine.xml.append(tokens[2]['symbol'])
            CompilationEngine.xml.append('</symbol>')
        else:
            sys.exit('ERROR:{ not found')
                  
        

        start = 3
        end = 0
        for x in range(start,len(tokens)):  
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'FIELD':
                     start = x
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'STATIC':
                     start = x
                     
            if tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ';':
                     end = x
            if start != 0 and end != 0:
                     self.CompileClassVarDec(start,end,tokens)
                     start = end
                     end = 0
      
      
      
     
       
        if tokens[len(tokens)-1]['tokenType']  == 'SYMBOL':
            CompilationEngine.xml.append('<symbol>') 
            CompilationEngine.xml.append(tokens[2]['symbol'])
            CompilationEngine.xml.append('</symbol>')
        else:
            sys.exit('ERROR:{ not found')
        
        
        CompilationEngine.xml.append("</class>")
           
        
        
    def CompileClassVarDec(self,start,end,tokens):
        print(start,end) 
        if tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'FIELD':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        else:
            sys.exit('error:')
                     
        if tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'INT':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        else:
            sys.exit('ERROR:')
        

            
       
        
        
           

