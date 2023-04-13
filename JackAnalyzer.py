import os, sys
import utils
from JackTokenizer import JackTokenizer
from CompilationEngine import CompilationEngine




class JackAnalyzer(object):
    def __init__(self):
        self.start()

    def start(self):
        files = utils.getFiles(sys.argv[1])
        for x in files:
            tokenizedData = JackTokenizer(x).tokenizedData 
           
            compiled = CompilationEngine(tokenizedData)
        
            
         
            
            


JackAnalyzer()
