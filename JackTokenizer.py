import utils


class JackTokenizer(object):
    def __init__(self, file):
        self.file = file
        self.tokenizer()

    def tokenizer(self):
        file = open(self.file, 'r')

        lines = utils.tokenizer(file.read().splitlines())
