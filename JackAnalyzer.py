import os, sys
import utils
From JackTokenizer import JackTokenizer


class JackAnalyzer(object):
    def __init__(self):
        self.start()

    def start(self):
        files = utils.getFiles(sys.argv[1])
        for x in files:
            JackTokenizer(x)
            


JackAnalyzer()
