import sys
import utils
class CompilationEngine(object):
    start = 3
    end = 0
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
            sys.exit('Error:class keyword not found')
                   
        if tokens[1]['tokenType']  == 'IDENTIFIER':
            CompilationEngine.xml.append('<identifier>') 
            CompilationEngine.xml.append(tokens[1]['identifier'])
            CompilationEngine.xml.append('</keyword>')
        else:
            sys.exit('Error:Wrong identifier or not written classname')
             
             
        
        if tokens[2]['tokenType']  == 'SYMBOL':
            CompilationEngine.xml.append('<symbol>') 
            CompilationEngine.xml.append(tokens[2]['symbol'])
            CompilationEngine.xml.append('</symbol>')
        else:
            sys.exit('Error:{ not found')
                     
                     
        for x in range(CompilationEngine.start,len(tokens)):
           
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'FIELD':
                end = self.CompileClassVarDec(x,tokens) 
                CompilationEngine.start = end
                     
        for x in range(CompilationEngine.start,len(tokens)):
            
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'FUNCTION':
                end = self.CompileSubroutine(x,tokens) 
                CompilationEngine.start = end
               
                    
        if tokens[len(tokens)-1]['tokenType']  == 'SYMBOL':
         
            CompilationEngine.xml.append('<symbol>') 
            CompilationEngine.xml.append(tokens[len(tokens)-1]['symbol'])
            CompilationEngine.xml.append('</symbol>')
        else:
            sys.exit('Error:} not found')
        
        
        CompilationEngine.xml.append("</class>")
           
        
        
    def CompileClassVarDec(self,start,tokens):
    
    
        CompilationEngine.xml.append('<classVarDec>')
        end = 0
        if tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'FIELD':            
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        elif tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'STATIC':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')

        else:
            sys.exit('Error:static or field not found')
                     
     
        if tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'INT':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        elif tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'CHAR':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        elif tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'BOOLEAN':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        elif tokens[start+1]['tokenType'] == 'IDENTIFIER':
            CompilationEngine.xml.append('<identifier>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</identifier>')
 
        else:
            sys.exit('Error:type not defined')
        
        for x in range(start+2,len(tokens)):
          
      
            if tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ';':
                end = x 
                break
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ',':
                CompilationEngine.xml.append('<symbol>')
                CompilationEngine.xml.append(tokens[x]['symbol'].lower())
                CompilationEngine.xml.append('</symbol>')
            elif tokens[x]['tokenType'] == 'IDENTIFIER':
                CompilationEngine.xml.append('<identifier>')
                CompilationEngine.xml.append(tokens[x]['identifier'].lower())
                CompilationEngine.xml.append('</identifier>')
               
        CompilationEngine.xml.append("</classVarDec>")   
        return end





    
    def CompileSubroutine(self,start,tokens):
        end = 0
        CompilationEngine.xml.append("<subroutineDec>")
        if tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'CONSTRUCTOR':           
            
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
            
        elif tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'FUNCTION':
            
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
            
        elif tokens[start]['tokenType'] == 'KEYWORD' and tokens[start]['keyword'] == 'METHOD':
            
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
            
        else:
            sys.exit('Error:syntaxerror in function')
                     


                     
        if tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'VOID':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
        else:
            sys.exit("Error:Type not defined")
            
        if tokens[start+2]['tokenType'] == 'IDENTIFIER':
            CompilationEngine.xml.append('<identifier>') 
            CompilationEngine.xml.append(tokens[start+2]['identifier'].lower())
            CompilationEngine.xml.append('</identifier>')
        else:
            sys.exit("Error:identifier ")

        utils.handleSymbol(start+3,'(','Not proper symbol',tokens)
        self.compileParameterList(start+4,tokens)
        start = CompilationEngine.end 
        utils.handleSymbol(start,')','Not proper symbol',tokens)
        
         # function starts 
        utils.handleSymbol(start+1,'{','Not proper symbol',tokens)    
        self.compileVarDec(start+2,tokens)
        start = CompilationEngine.end + 1 
                
 
    
        self.compileStatements(start,tokens) 
   
        end = CompilationEngine.end
         
       
        utils.handleSymbol(end+1,'}','} not found',tokens)    
        CompilationEngine.xml.append("</subroutineDec>")
        return end   
     
    def compileParameterList(self,start,tokens):
        end = 0
        CompilationEngine.xml.append("<parameterList>")
     
        for x in range(start,len(tokens)):
        
            if tokens[x]['tokenType'] == 'KEYWORD':
                utils.handleType(x,'wrong type',tokens)            
            elif tokens[x]['tokenType'] == 'IDENTIFIER':
                utils.handleIdentifier(x,'wrong identifier',tokens)
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ',':
                utils.handleSymbol(x,tokens[x],'wrong symbol',tokens)
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ')':
                CompilationEngine.end = x
                break
            else:
                pass
               
                
        CompilationEngine.xml.append("</parameterList>")

    def compileVarDec(self,start,tokens):
        # print(CompilationEngine.xml)
        # print(tokens)
        
        utils.handleKeyword(start,'VAR','wrong variable declaration',tokens)
        utils.handleType(start+1,'wrong type',tokens)
       
        for x in range(start+2,len(tokens)):
          
      
            if tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ';':
                CompilationEngine.end = x 
                break
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ',':
                CompilationEngine.xml.append('<symbol>')
                CompilationEngine.xml.append(tokens[x]['symbol'].lower())
                CompilationEngine.xml.append('</symbol>')
            elif tokens[x]['tokenType'] == 'IDENTIFIER':
                CompilationEngine.xml.append('<identifier>')
                CompilationEngine.xml.append(tokens[x]['identifier'].lower())
                CompilationEngine.xml.append('</identifier>')
        
    def compileStatements(self,start,tokens):

        for x in range(start,len(tokens)):
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'LET': 
             
                self.compileLet(x,tokens)
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'IF':
                self.compileIf(x,tokens)
              
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'WHILE':
                self.compileWhile(x,tokens)
    
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'DO':
                self.compileDo(x,tokens)
            
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'RETURN':
                self.compileReturn(x,tokens)
            else:
                pass
 
                
                        
    def compileDo(self,start,tokens):
        utils.handleKeyword(start,'DO','keyword error',tokens) 
        self.compileTerm(start,tokens) 
        # CompilationEngine.end = start+1
        
    def compileLet(self,start,tokens):
  
        utils.handleKeyword(start,'LET','Let statement ',tokens)
        utils.handleIdentifier(start+1,'Wrong return identifier',tokens)
        if tokens[start+2]['symbol'] == '[':
            utils.handleSymbol(start+2,'[','symbol Error',tokens)
            self.compileExpression(start+3,'Wrong return expression',tokens)
            utils.handleSymbol(start+4,'[','symbol Error',tokens)
            CompilationEngine.end = start+5
            
        elif tokens[start+2]['symbol'] == '=': 
            utils.handleSymbol(start+2,'=','symbol Error',tokens)
            self.compileExpression(start+3,tokens)
            start = CompilationEngine.end
            utils.handleSymbol(start,';','symbol Error',tokens)
            CompilationEngine.end = start+1
   
                               
    def compilewhile(self,start,tokens):
        utils.handleKeyword(start,'WHILE','keyword error',tokens)
        utils.handleSymbol(start+1,'(','symbol Error',tokens)
        self.compileExpression(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,')','symbol Error',tokens)
        utils.handleSymbol(start+1,'{','symbol Error',tokens)
        self.compileStatements(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,'}','symbol Error',tokens)
        CompilationEngine.end = start+1
        
                           
    def compileReturn(self,start,tokens):
        CompilationEngine.xml.append('<returnStatement>')
     
        utils.handleKeyword(start,'RETURN','Return statement not found',tokens)
        if tokens[start+1]['tokenType'] == 'IDENTIFIER':
            utils.handleIdentifier(start+1,'Wrong return identifier',tokens)
            utils.handleSymbol(start+2,';',"; not found",tokens)
            CompilationEngine.end = start+2
        else:
            CompilationEngine.end = start+1
            utils.handleSymbol(start+1,';','; not found',tokens)
       
        CompilationEngine.xml.append('</returnStatement>')
        
       
        

    def compileIf(self,start,tokens):
        utils.handleKeyword(start,'IF','keyword error',tokens)
        utils.handleSymbol(start+1,'(','symbol Error',tokens)
        self.compileExpression(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,')','symbol Error',tokens)
        utils.handleSymbol(start+1,'{','symbol Error',tokens)
        self.compileStatements(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,'}','symbol Error',tokens)
        CompilationEngine.end = start+1
        if tokens[start+1]['keyword'] == 'else':
            utils.handleKeyword(start,'ELSE','keyword error',tokens)
            utils.handleSymbol(start+1,'{','symbol Error',tokens)
            self.compileStatements(start+2,tokens)
            start = CompilationEngine.end
            utils.handleSymbol(start,'}','symbol Error',tokens)
            CompilationEngine.end = start+1
                               
        
            
    def compileTerm(self,start,tokens):
                               
        if tokens[start]['tokenType'] == 'INT_CONST':
            CompilationEngine.xml.append('<integerConstant>') 
            CompilationEngine.xml.append(tokens[start]['intVal'])
            CompilationEngine.xml.append('</integerConstant>')
            CompilationEngine.end = start +1
            
        elif tokens[start]['tokenType'] == 'STRING_CONST':
       
            CompilationEngine.xml.append('<stringConstant>') 
            CompilationEngine.xml.append(tokens[start]['stringVal'])
            CompilationEngine.xml.append('</stringConstant>')
            CompilationEngine.end = start +1
                               
        elif tokens[start]['tokenType'] == 'KEYWORD':
            utils.handlekeyword(start,tokens[start]['keyword'],"false keyword",tokens)
            CompilationEngine.end = start +1

        elif tokens[start]['tokenType'] == 'IDENTIFIER':
            utils.handleidentifier(start,"false identifier",tokens)
            if tokens[start+1]['symbol'] == '[':
                utils.handleSymbol(start+1,'[','wrong symbol',tokens)
                self.compileExpression(start,tokens) 
                start = CompilationEngine.end
                utils.handleSymbol(start,']','wrong symbol',tokens)
            elif tokens[start]['symbol'] == '(':
                utils.handleSymbol(start,'(''symbol er',tokens)
                self.compileExpression(start,tokens)
                start = CompilationEngine.end
                utils.handleSymbol(start,')''symbol er',tokens)
            elif tokens[start+1]['symbol'] == '(':
                utils.handleIdentifier(start,'identifier error',tokens)
                utils.handleSymbol(start+1,'(''symbol er',tokens)
                self.compileExpressionList(start+2,tokens)
                start = CompilationEngine.end
                utils.handleSymbol(start,')''symbol er',tokens)
            elif tokens[start+1]['symbol'] == '.':
                utils.handleIdentifier(start,'identifier error',tokens)
                utils.handleSymbol(start+1,'.''symbol er',tokens)
                utils.handleIdentifier(start+2,'identifier error',tokens)
                utils.handleSymbol(start+3,'(''symbol er',tokens)
                self.compileExpressionList(start+4,tokens)
                start = CompilationEngine.end
                utils.handleSymbol(start,'.''symbol er',tokens)
            elif tokens[start]['symbol'] == '-':
                utils.handleSymbol(start,'-''symbol er',tokens)
                self.compileTerm(start+1,tokens)
                                                    
       
        
    def compileExpression(self,start,tokens):
        self.compileTerm(start,tokens)
        for x in range(start+1,len(tokens)):
            if tokens[x]['tokenType'] == 'symbol' and tokens[x]['symbol'] != ';':
                utils.handleSymbol(start,tokens[x],'symbol error',tokens)
                self.compileTerm(x,tokens)
            elif tokens[x]['tokenType'] == 'symbol' and tokens[x]['symbol'] == ';':
                CompilationEngine.end = x
                break
            else:
                pass
                
        
    def compileExpressionList(self,start,tokens):
        self.compileExpression(start,tokens)  
        start = CompilationEngine.end
        for x in range(start,len(tokens)):
            if tokens[x]['symbol'] == ')':
                CompilationEngine.end = x
                break
            elif tokens[x]['symbol'] == ',':
                self.compileExpression(x,tokens)
            else:
                pass
        
