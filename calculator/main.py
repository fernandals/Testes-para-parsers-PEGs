import sys
from antlr4 import *
from calculatorLexer import calculatorLexer
from calculatorParser import calculatorParser
from calculatorListener import calculatorListener
#from calculatorCustomListener import calculatorCustomListener

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = calculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = calculatorParser(stream)
    tree = parser.equation()

    printer = calculatorListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
