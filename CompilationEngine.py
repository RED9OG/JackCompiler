import sys
import utils
class CompilationEngine(object):
    start = 3
    end = 0
    xml = []
    def __init__(self,tokenizedData):
        self.tokenizedData = tokenizedData
        self.CompileClass(tokenizedData)
        # print(CompilationEngine.xml)
       
 


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
            CompilationEngine.xml.append('</identifier>')
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
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'STATIC':
                end = self.CompileClassVarDec(x,tokens) 
                CompilationEngine.start = end
            else:
                pass
                     
        for x in range(CompilationEngine.start,len(tokens)):
            # print(tokens[x])
            if tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'FUNCTION':
                end = self.CompileSubroutine(x,tokens) 
                CompilationEngine.start = end
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'CONSTRUCTOR':
                end = self.CompileSubroutine(x,tokens) 
                CompilationEngine.start = end
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'METHOD':
                # print('hl')
                end = self.CompileSubroutine(x,tokens) 
                CompilationEngine.start = end
            else:
                pass
                 
                    
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
        # print(tokens[start],start)
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
            sys.exit('Error:syntax error in function declaration')
                     


        # print(tokens[start+1])            
        if tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'VOID':
            CompilationEngine.xml.append('<keyword>') 
            CompilationEngine.xml.append(tokens[start+1]['keyword'].lower())
            CompilationEngine.xml.append('</keyword>')
            
        elif tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'INT':
            utils.handleKeyword(start+1,'INT','type error',tokens)
            
        elif tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'CHAR':
            utils.handleKeyword(start+1,'CHAR','type error',tokens)
            
        elif tokens[start+1]['tokenType'] == 'KEYWORD' and tokens[start+1]['keyword'] == 'BOOLEAN':
            utils.handleKeyword(start+1,'BOOLEAN','type error',tokens)
            
        elif tokens[start+1]['tokenType'] == 'IDENTIFIER':
            utils.handleIdentifier(start+1,'type error',tokens)
            
        else:
            sys.exit("Error:function type not defined")
            
        if tokens[start+2]['tokenType'] == 'IDENTIFIER':
            CompilationEngine.xml.append('<identifier>') 
            CompilationEngine.xml.append(tokens[start+2]['identifier'].lower())
            CompilationEngine.xml.append('</identifier>')
        else:
            sys.exit("Error:subroutineName ")

        utils.handleSymbol(start+3,'(','( not found in function parameterList',tokens)
        # print(tokens)
        self.compileParameterList(start+4,tokens)
        start = CompilationEngine.end 
        utils.handleSymbol(start,')','( not found in function parameterList',tokens)
        
         # function starts 
        utils.handleSymbol(start+1,'{',' { function starting Not proper symbol',tokens)    
      
     
        start = CompilationEngine.end + 1 
                
 
    
        self.compileStatements(start,tokens) 
   
        
        end = CompilationEngine.end
         
        utils.handleSymbol(end,'}','} not found in function ending',tokens)    
        CompilationEngine.xml.append("</subroutineDec>")
        return end+1   
     
    def compileParameterList(self,start,tokens):
        end = 0
        CompilationEngine.xml.append("<parameterList>")
     
        for x in range(start,len(tokens)):
        
            if tokens[x]['tokenType'] == 'KEYWORD':
                utils.handleType(x,'parameterList  type',tokens)            
            elif tokens[x]['tokenType'] == 'IDENTIFIER':
                utils.handleIdentifier(x,'wrong parameterList identifier',tokens)
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ',':
          
                utils.handleSymbol(x,tokens[x]['symbol'],'parameterList symbol',tokens)
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ')':
                CompilationEngine.end = x
                break
            else:
                pass
               
                
        CompilationEngine.xml.append("</parameterList>")
        # print(CompilationEngine.xml)

    def compileVarDec(self,start,tokens):
        # print(CompilationEngine.xml)
        # print(tokens)

        utils.handleKeyword(start,'VAR','wrong variable declaration',tokens)
        utils.handleType(start+1,'wrong type variable declaration',tokens)
       
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
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'VAR':
                self.compileVarDec(x,tokens)
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'IF':
                self.compileIf(x,tokens)
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'WHILE':
                self.compileWhile(x,tokens)
    
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'DO':
                self.compileDo(x,tokens)
            
            elif tokens[x]['tokenType'] == 'KEYWORD' and tokens[x]['keyword'] == 'RETURN':
                self.compileReturn(x,tokens)
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == '}':
                CompilationEngine.end = x
                break
            else:
                pass
 
                
                        
    def compileDo(self,start,tokens):
       
        utils.handleKeyword(start,'DO',' do keyword error',tokens) 
        self.compileTerm(start+1,tokens) 
        print('as')
        start = CompilationEngine.end
        # print("x-------------------x-------------------x---------------------x------------------x")
        # print(CompilationEngine.xml)
        # print(tokens[start])
        utils.handleSymbol(start,';','syssmbol error',tokens)
      
        
    def compileLet(self,start,tokens):
  
        utils.handleKeyword(start,'LET','Let statement ',tokens)
        utils.handleIdentifier(start+1,'Wrong let identifier',tokens)
     
        if tokens[start+2]['symbol'] == '[':
            utils.handleSymbol(start+2,'[','Let statementsymbol Error',tokens)
            self.compileExpression(start+3,'Let statementWrong return expression',tokens)
            utils.handleSymbol(start+4,']','Let statementsymbol Error',tokens)
            CompilationEngine.end = start+5
            
        elif tokens[start+2]['symbol'] == '=': 
            
            utils.handleSymbol(start+2,'=','Let statementsymbol Error',tokens)
            self.compileExpression(start+3,tokens)
            start = CompilationEngine.end

            utils.handleSymbol(start,';','Let statementsymbol Error',tokens)
            CompilationEngine.end = start+1
   
                               
    def compilewhile(self,start,tokens):
        utils.handleKeyword(start,'WHILE','while keyword error',tokens)
        utils.handleSymbol(start+1,'(','while symbol Error',tokens)
        self.compileExpression(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,')','while symbol Error',tokens)
        utils.handleSymbol(start+1,'{','while symbol Error',tokens)
        self.compileStatements(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,'}','while symbol Error',tokens)
        CompilationEngine.end = start+1
        
                           
    def compileReturn(self,start,tokens):
        
        CompilationEngine.xml.append('<returnStatement>')
     
        utils.handleKeyword(start,'RETURN','Return statement not found',tokens)
        if tokens[start+1]['tokenType'] != ';':
            self.compileExpression(start+1,tokens)
       
        else:
            CompilationEngine.end = start+2
            utils.handleSymbol(start+1,';','return ; not found',tokens)
       
        CompilationEngine.xml.append('</returnStatement>')
        
       
        

    def compileIf(self,start,tokens):
        utils.handleKeyword(start,'IF','IF keyword error',tokens)
        utils.handleSymbol(start+1,'(','IFsymbol Error',tokens)
        self.compileExpression(start+2,tokens)
        start = CompilationEngine.end
        # print(CompilationEngine.xml)
        # print(tokens[start])
        utils.handleSymbol(start,')','IaaaFsybol Error',tokens)
        utils.handleSymbol(start+1,'{','IFsymbol Error',tokens)
        self.compileStatements(start+2,tokens)
        start = CompilationEngine.end
        utils.handleSymbol(start,'}','IFsymbol Error',tokens)
        CompilationEngine.end = start+1
        if tokens[start+1]['keyword'] == 'else':
            utils.handleKeyword(start,'ELSE','IFkeyword error',tokens)
            utils.handleSymbol(start+1,'{','IFsymbol Error',tokens)
            self.compileStatements(start+2,tokens)
            start = CompilationEngine.end
            utils.handleSymbol(start,'}','IFsymbol Error',tokens)
            CompilationEngine.end = start+1
                               
        
            
    def compileTerm(self,start,tokens):
  
   
        # print("-------------x-------------------x-------------------x--------------------------x")
        # print(tokens[start])
        
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
            # print(tokens[start])       
            # utils.handleKeyword(start,tokens[start]['keyword'],"term false keyword",tokens)
            CompilationEngine.end = start +1
        
        elif tokens[start]['tokenType'] == 'IDENTIFIER':
            # print(tokens[start])
            utils.handleIdentifier(start,"term false identifier",tokens)
            CompilationEngine.end = start+1
            if tokens[start]['tokenType'] == 'SYMBOL' and tokens[start+1]['symbol'] == '[':
                # utils.handleIdentifier(start,"term false identifier",tokens)
                utils.handleSymbol(start+1,'[','variablename Experssion wrong symbol',tokens)
                self.compileExpression(start,tokens) 
                start = CompilationEngine.end
                utils.handleSymbol(start,']','term wrong symbol',tokens)
            elif tokens[start]['tokenType'] == 'SYMBOL' and tokens[start]['symbol'] == '(':
                utils.handleSymbol(start,'(''term symbol errr',tokens)
                self.compileExpression(start,tokens)
                start = CompilationEngine.end
                utils.handleSymbol(start,')''term symbol r',tokens)
            elif tokens[start+1]['tokenType'] == 'SYMBOL' and tokens[start+1]['symbol'] == '(':
                # utils.handleIdentifier(start,'subroutine call term identifier error',tokens)
                utils.handleSymbol(start+1,'(','term symbl er',tokens)
                self.compileExpressionList(start+2,tokens)
                start = CompilationEngine.end
                # print(tokens[start])
               
                utils.handleSymbol(start,')','term symol er',tokens)
                CompilationEngine.end = start +1
                                                
            elif  tokens[start+1]['tokenType'] == 'SYMBOL' and tokens[start+1]['symbol'] == '.':
                # utils.handleIdentifier(start,'iterm dentifier error',tokens)
                                                
                utils.handleSymbol(start+1,'.','term ymbol er',tokens)
                utils.handleIdentifier(start+2,'iterm dentifier error',tokens)
                utils.handleSymbol(start+3,'(','ter symbol er',tokens)
                # print(CompilationEngine.xml)
                self.compileExpressionList(start+4,tokens)
                # print(tokens[start+4])
                start = CompilationEngine.end
                utils.handleSymbol(start,')','term bol er',tokens)
                CompilationEngine.end = start+1
                                                
            elif  tokens[start]['tokenType'] == 'SYMBOL' and tokens[start]['symbol'] == '-':
                utils.handleSymbol(start,'-','term symbol er',tokens)
                self.compileTerm(start+1,tokens)
        else:
            pass
       
        
    def compileExpression(self,start,tokens):
        # print(tokens[start])
        
        self.compileTerm(start,tokens)
        start = CompilationEngine.end
        # print(CompilationEngine.xml)
        for x in range(start,len(tokens)):
            
            if tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ';':
                CompilationEngine.end = x
                break
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ')':
                CompilationEngine.end = x
                break                       
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ']':
                CompilationEngine.end = x
                break                       
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ',':
                CompilationEngine.end = x
                break 
            elif tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] != ';':
                # print(CompilationEngine.xml)
                # print(tokens[x])
                utils.handleSymbol(x,tokens[x]['symbol'],'expression symbol  error',tokens)
                self.compileTerm(x,tokens)                                                
            else:
                print(tokens[x])
                self.compileTerm(x,tokens)                                                
                
                
        
    def compileExpressionList(self,start,tokens):
        # self.compileExpression(start,tokens)  
        # start = CompilationEngine.end
        # print(tokens[start])
        for x in range(start,len(tokens)):
            # print(tokens[x])
            if tokens[x]['tokenType'] == 'SYMBOL' and tokens[x]['symbol'] == ')':
                # print(tokens[x],x)
                # if tokens[x+1]['symbol'] == ';':
                    # print("gotcha")
                utils.handleSymbol(x,tokens[x]['symbol'],'Expression symbol list',tokens)
                CompilationEngine.end = x+1
                # print('as')
                break
            elif tokens[x]['tokenType'] == 'SYMBOL':
                # print(tokens[x])
                utils.handleSymbol(x,tokens[x]['symbol'],'Expression symbol list',tokens)
            else:
                # print(tokens[x])
                self.compileExpression(x,tokens)
        
