import sys
from antlr4 import *
from bnfLexer import bnfLexer
from bnfParser import bnfParser
from bnfListener import MyTest

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = bnfLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = bnfParser(stream)
    tree = parser.rulelist()

    printer = MyTest()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)

