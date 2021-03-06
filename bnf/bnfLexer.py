# Generated from bnf.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\6\f\64\n\f\r")
        buf.write("\f\16\f\65\3\r\3\r\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\4\2C\\c|\7")
        buf.write("\2\"\"//\62;C\\c|\5\2\13\f\17\17\"\"\2;\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\37\3\2\2")
        buf.write("\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3")
        buf.write("\2\2\2\21+\3\2\2\2\23-\3\2\2\2\25/\3\2\2\2\27\61\3\2\2")
        buf.write("\2\31\67\3\2\2\2\33\34\7<\2\2\34\35\7<\2\2\35\36\7?\2")
        buf.write("\2\36\4\3\2\2\2\37 \7+\2\2 \6\3\2\2\2!\"\7*\2\2\"\b\3")
        buf.write("\2\2\2#$\7\177\2\2$\n\3\2\2\2%&\7}\2\2&\f\3\2\2\2\'(\7")
        buf.write("_\2\2(\16\3\2\2\2)*\7]\2\2*\20\3\2\2\2+,\7~\2\2,\22\3")
        buf.write("\2\2\2-.\7@\2\2.\24\3\2\2\2/\60\7>\2\2\60\26\3\2\2\2\61")
        buf.write("\63\t\2\2\2\62\64\t\3\2\2\63\62\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65\63\3\2\2\2\65\66\3\2\2\2\66\30\3\2\2\2\678\t\4\2\2")
        buf.write("89\3\2\2\29:\b\r\2\2:\32\3\2\2\2\4\2\65\3\b\2\2")
        return buf.getvalue()


class bnfLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ASSIGN = 1
    LPAREN = 2
    RPAREN = 3
    LBRACE = 4
    RBRACE = 5
    LEND = 6
    REND = 7
    BAR = 8
    GT = 9
    LT = 10
    ID = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'::='", "')'", "'('", "'}'", "'{'", "']'", "'['", "'|'", "'>'", 
            "'<'" ]

    symbolicNames = [ "<INVALID>",
            "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LEND", "REND", 
            "BAR", "GT", "LT", "ID", "WS" ]

    ruleNames = [ "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LEND", 
                  "REND", "BAR", "GT", "LT", "ID", "WS" ]

    grammarFileName = "bnf.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


