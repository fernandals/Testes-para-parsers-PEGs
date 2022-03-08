# Generated from calculator.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\7\3\"\n\3\f\3\16\3%\13\3\3\4\3\4")
        buf.write("\3\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\3\5\7\5\62\n\5\f")
        buf.write("\5\16\5\65\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\5\7F\n\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\7\13S\n\13\f\13\16\13V\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\2\7\3\2\16\17\3\2\20\21\3\2\30\32\3\2")
        buf.write("\3\13\3\2\22\24\2[\2\32\3\2\2\2\4\36\3\2\2\2\6&\3\2\2")
        buf.write("\2\b.\3\2\2\2\n<\3\2\2\2\fE\3\2\2\2\16G\3\2\2\2\20I\3")
        buf.write("\2\2\2\22K\3\2\2\2\24M\3\2\2\2\26Y\3\2\2\2\30[\3\2\2\2")
        buf.write("\32\33\5\4\3\2\33\34\5\30\r\2\34\35\5\4\3\2\35\3\3\2\2")
        buf.write("\2\36#\5\6\4\2\37 \t\2\2\2 \"\5\6\4\2!\37\3\2\2\2\"%\3")
        buf.write("\2\2\2#!\3\2\2\2#$\3\2\2\2$\5\3\2\2\2%#\3\2\2\2&+\5\b")
        buf.write("\5\2\'(\t\3\2\2(*\5\b\5\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,\7\3\2\2\2-+\3\2\2\2.\63\5\n\6\2/\60\7\27")
        buf.write("\2\2\60\62\5\n\6\2\61/\3\2\2\2\62\65\3\2\2\2\63\61\3\2")
        buf.write("\2\2\63\64\3\2\2\2\64\t\3\2\2\2\65\63\3\2\2\2\66\67\7")
        buf.write("\16\2\2\67=\5\n\6\289\7\17\2\29=\5\n\6\2:=\5\24\13\2;")
        buf.write("=\5\f\7\2<\66\3\2\2\2<8\3\2\2\2<:\3\2\2\2<;\3\2\2\2=\13")
        buf.write("\3\2\2\2>F\5\16\b\2?F\5\22\n\2@F\5\20\t\2AB\7\f\2\2BC")
        buf.write("\5\4\3\2CD\7\r\2\2DF\3\2\2\2E>\3\2\2\2E?\3\2\2\2E@\3\2")
        buf.write("\2\2EA\3\2\2\2F\r\3\2\2\2GH\7\34\2\2H\17\3\2\2\2IJ\t\4")
        buf.write("\2\2J\21\3\2\2\2KL\7\33\2\2L\23\3\2\2\2MN\5\26\f\2NO\7")
        buf.write("\f\2\2OT\5\4\3\2PQ\7\25\2\2QS\5\4\3\2RP\3\2\2\2SV\3\2")
        buf.write("\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2WX\7\r\2\2")
        buf.write("X\25\3\2\2\2YZ\t\5\2\2Z\27\3\2\2\2[\\\t\6\2\2\\\31\3\2")
        buf.write("\2\2\b#+\63<ET")
        return buf.getvalue()


class calculatorParser ( Parser ):

    grammarFileName = "calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cos'", "'sin'", "'tan'", "'acos'", "'asin'", 
                     "'atan'", "'ln'", "'log'", "'sqrt'", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "','", 
                     "'.'", "'^'", "'pi'", "<INVALID>", "'i'" ]

    symbolicNames = [ "<INVALID>", "COS", "SIN", "TAN", "ACOS", "ASIN", 
                      "ATAN", "LN", "LOG", "SQRT", "LPAREN", "RPAREN", "PLUS", 
                      "MINUS", "TIMES", "DIV", "GT", "LT", "EQ", "COMMA", 
                      "POINT", "POW", "PI", "EULER", "I", "VARIABLE", "SCIENTIFIC_NUMBER", 
                      "WS" ]

    RULE_equation = 0
    RULE_expression = 1
    RULE_multiplyingExpression = 2
    RULE_powExpression = 3
    RULE_signedAtom = 4
    RULE_atom = 5
    RULE_scientific = 6
    RULE_constant = 7
    RULE_variable = 8
    RULE_func_ = 9
    RULE_funcname = 10
    RULE_relop = 11

    ruleNames =  [ "equation", "expression", "multiplyingExpression", "powExpression", 
                   "signedAtom", "atom", "scientific", "constant", "variable", 
                   "func_", "funcname", "relop" ]

    EOF = Token.EOF
    COS=1
    SIN=2
    TAN=3
    ACOS=4
    ASIN=5
    ATAN=6
    LN=7
    LOG=8
    SQRT=9
    LPAREN=10
    RPAREN=11
    PLUS=12
    MINUS=13
    TIMES=14
    DIV=15
    GT=16
    LT=17
    EQ=18
    COMMA=19
    POINT=20
    POW=21
    PI=22
    EULER=23
    I=24
    VARIABLE=25
    SCIENTIFIC_NUMBER=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(calculatorParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(calculatorParser.RelopContext,0)


        def getRuleIndex(self):
            return calculatorParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)




    def equation(self):

        localctx = calculatorParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.expression()
            self.state = 25
            self.relop()
            self.state = 26
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplyingExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.MultiplyingExpressionContext)
            else:
                return self.getTypedRuleContext(calculatorParser.MultiplyingExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.PLUS)
            else:
                return self.getToken(calculatorParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.MINUS)
            else:
                return self.getToken(calculatorParser.MINUS, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = calculatorParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.multiplyingExpression()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==calculatorParser.PLUS or _la==calculatorParser.MINUS:
                self.state = 29
                _la = self._input.LA(1)
                if not(_la==calculatorParser.PLUS or _la==calculatorParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.multiplyingExpression()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def powExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.PowExpressionContext)
            else:
                return self.getTypedRuleContext(calculatorParser.PowExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.TIMES)
            else:
                return self.getToken(calculatorParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.DIV)
            else:
                return self.getToken(calculatorParser.DIV, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_multiplyingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplyingExpression" ):
                listener.enterMultiplyingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplyingExpression" ):
                listener.exitMultiplyingExpression(self)




    def multiplyingExpression(self):

        localctx = calculatorParser.MultiplyingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multiplyingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.powExpression()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==calculatorParser.TIMES or _la==calculatorParser.DIV:
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==calculatorParser.TIMES or _la==calculatorParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 38
                self.powExpression()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signedAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.SignedAtomContext)
            else:
                return self.getTypedRuleContext(calculatorParser.SignedAtomContext,i)


        def POW(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.POW)
            else:
                return self.getToken(calculatorParser.POW, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_powExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpression" ):
                listener.enterPowExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpression" ):
                listener.exitPowExpression(self)




    def powExpression(self):

        localctx = calculatorParser.PowExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.signedAtom()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==calculatorParser.POW:
                self.state = 45
                self.match(calculatorParser.POW)
                self.state = 46
                self.signedAtom()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignedAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(calculatorParser.PLUS, 0)

        def signedAtom(self):
            return self.getTypedRuleContext(calculatorParser.SignedAtomContext,0)


        def MINUS(self):
            return self.getToken(calculatorParser.MINUS, 0)

        def func_(self):
            return self.getTypedRuleContext(calculatorParser.Func_Context,0)


        def atom(self):
            return self.getTypedRuleContext(calculatorParser.AtomContext,0)


        def getRuleIndex(self):
            return calculatorParser.RULE_signedAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedAtom" ):
                listener.enterSignedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedAtom" ):
                listener.exitSignedAtom(self)




    def signedAtom(self):

        localctx = calculatorParser.SignedAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_signedAtom)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calculatorParser.PLUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(calculatorParser.PLUS)
                self.state = 53
                self.signedAtom()
                pass
            elif token in [calculatorParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(calculatorParser.MINUS)
                self.state = 55
                self.signedAtom()
                pass
            elif token in [calculatorParser.COS, calculatorParser.SIN, calculatorParser.TAN, calculatorParser.ACOS, calculatorParser.ASIN, calculatorParser.ATAN, calculatorParser.LN, calculatorParser.LOG, calculatorParser.SQRT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.func_()
                pass
            elif token in [calculatorParser.LPAREN, calculatorParser.PI, calculatorParser.EULER, calculatorParser.I, calculatorParser.VARIABLE, calculatorParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(calculatorParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(calculatorParser.VariableContext,0)


        def constant(self):
            return self.getTypedRuleContext(calculatorParser.ConstantContext,0)


        def LPAREN(self):
            return self.getToken(calculatorParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(calculatorParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(calculatorParser.RPAREN, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = calculatorParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calculatorParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.scientific()
                pass
            elif token in [calculatorParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.variable()
                pass
            elif token in [calculatorParser.PI, calculatorParser.EULER, calculatorParser.I]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.constant()
                pass
            elif token in [calculatorParser.LPAREN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(calculatorParser.LPAREN)
                self.state = 64
                self.expression()
                self.state = 65
                self.match(calculatorParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScientificContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(calculatorParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)




    def scientific(self):

        localctx = calculatorParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(calculatorParser.SCIENTIFIC_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PI(self):
            return self.getToken(calculatorParser.PI, 0)

        def EULER(self):
            return self.getToken(calculatorParser.EULER, 0)

        def I(self):
            return self.getToken(calculatorParser.I, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = calculatorParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << calculatorParser.PI) | (1 << calculatorParser.EULER) | (1 << calculatorParser.I))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(calculatorParser.VARIABLE, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = calculatorParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(calculatorParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcname(self):
            return self.getTypedRuleContext(calculatorParser.FuncnameContext,0)


        def LPAREN(self):
            return self.getToken(calculatorParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculatorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(calculatorParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(calculatorParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(calculatorParser.COMMA)
            else:
                return self.getToken(calculatorParser.COMMA, i)

        def getRuleIndex(self):
            return calculatorParser.RULE_func_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_" ):
                listener.enterFunc_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_" ):
                listener.exitFunc_(self)




    def func_(self):

        localctx = calculatorParser.Func_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.funcname()
            self.state = 76
            self.match(calculatorParser.LPAREN)
            self.state = 77
            self.expression()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==calculatorParser.COMMA:
                self.state = 78
                self.match(calculatorParser.COMMA)
                self.state = 79
                self.expression()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(calculatorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(calculatorParser.COS, 0)

        def TAN(self):
            return self.getToken(calculatorParser.TAN, 0)

        def SIN(self):
            return self.getToken(calculatorParser.SIN, 0)

        def ACOS(self):
            return self.getToken(calculatorParser.ACOS, 0)

        def ATAN(self):
            return self.getToken(calculatorParser.ATAN, 0)

        def ASIN(self):
            return self.getToken(calculatorParser.ASIN, 0)

        def LOG(self):
            return self.getToken(calculatorParser.LOG, 0)

        def LN(self):
            return self.getToken(calculatorParser.LN, 0)

        def SQRT(self):
            return self.getToken(calculatorParser.SQRT, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_funcname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncname" ):
                listener.enterFuncname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncname" ):
                listener.exitFuncname(self)




    def funcname(self):

        localctx = calculatorParser.FuncnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << calculatorParser.COS) | (1 << calculatorParser.SIN) | (1 << calculatorParser.TAN) | (1 << calculatorParser.ACOS) | (1 << calculatorParser.ASIN) | (1 << calculatorParser.ATAN) | (1 << calculatorParser.LN) | (1 << calculatorParser.LOG) | (1 << calculatorParser.SQRT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(calculatorParser.EQ, 0)

        def GT(self):
            return self.getToken(calculatorParser.GT, 0)

        def LT(self):
            return self.getToken(calculatorParser.LT, 0)

        def getRuleIndex(self):
            return calculatorParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = calculatorParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << calculatorParser.GT) | (1 << calculatorParser.LT) | (1 << calculatorParser.EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





