# Generated from bnf.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6\63")
        buf.write("\13\6\3\7\7\7\66\n\7\f\7\16\79\13\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b@\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\2\2")
        buf.write("\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2O\2\37\3\2\2")
        buf.write("\2\4$\3\2\2\2\6(\3\2\2\2\b*\3\2\2\2\n,\3\2\2\2\f\67\3")
        buf.write("\2\2\2\16?\3\2\2\2\20A\3\2\2\2\22E\3\2\2\2\24I\3\2\2\2")
        buf.write("\26M\3\2\2\2\30O\3\2\2\2\32S\3\2\2\2\34\36\5\4\3\2\35")
        buf.write("\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3")
        buf.write("\2\2\2!\37\3\2\2\2\"#\7\2\2\3#\3\3\2\2\2$%\5\6\4\2%&\7")
        buf.write("\3\2\2&\'\5\b\5\2\'\5\3\2\2\2()\5\30\r\2)\7\3\2\2\2*+")
        buf.write("\5\n\6\2+\t\3\2\2\2,\61\5\f\7\2-.\7\n\2\2.\60\5\f\7\2")
        buf.write("/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\13\3\2\2\2\63\61\3\2\2\2\64\66\5\16\b\2\65\64\3\2\2\2")
        buf.write("\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\r\3\2\2\29\67")
        buf.write("\3\2\2\2:@\5\20\t\2;@\5\22\n\2<@\5\24\13\2=@\5\26\f\2")
        buf.write(">@\5\30\r\2?:\3\2\2\2?;\3\2\2\2?<\3\2\2\2?=\3\2\2\2?>")
        buf.write("\3\2\2\2@\17\3\2\2\2AB\7\t\2\2BC\5\n\6\2CD\7\b\2\2D\21")
        buf.write("\3\2\2\2EF\7\7\2\2FG\5\n\6\2GH\7\6\2\2H\23\3\2\2\2IJ\7")
        buf.write("\5\2\2JK\5\n\6\2KL\7\4\2\2L\25\3\2\2\2MN\7\r\2\2N\27\3")
        buf.write("\2\2\2OP\7\f\2\2PQ\5\32\16\2QR\7\13\2\2R\31\3\2\2\2ST")
        buf.write("\7\r\2\2T\33\3\2\2\2\6\37\61\67?")
        return buf.getvalue()


class bnfParser ( Parser ):

    grammarFileName = "bnf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::='", "')'", "'('", "'}'", "'{'", "']'", 
                     "'['", "'|'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LEND", "REND", "BAR", "GT", "LT", "ID", 
                      "WS" ]

    RULE_rulelist = 0
    RULE_rule_ = 1
    RULE_lhs = 2
    RULE_rhs = 3
    RULE_alternatives = 4
    RULE_alternative = 5
    RULE_element = 6
    RULE_optional_ = 7
    RULE_zeroormore = 8
    RULE_oneormore = 9
    RULE_text_ = 10
    RULE_id_ = 11
    RULE_ruleid = 12

    ruleNames =  [ "rulelist", "rule_", "lhs", "rhs", "alternatives", "alternative", 
                   "element", "optional_", "zeroormore", "oneormore", "text_", 
                   "id_", "ruleid" ]

    EOF = Token.EOF
    ASSIGN=1
    LPAREN=2
    RPAREN=3
    LBRACE=4
    RBRACE=5
    LEND=6
    REND=7
    BAR=8
    GT=9
    LT=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RulelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(bnfParser.EOF, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.Rule_Context)
            else:
                return self.getTypedRuleContext(bnfParser.Rule_Context,i)


        def getRuleIndex(self):
            return bnfParser.RULE_rulelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRulelist" ):
                listener.enterRulelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRulelist" ):
                listener.exitRulelist(self)




    def rulelist(self):

        localctx = bnfParser.RulelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rulelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bnfParser.LT:
                self.state = 26
                self.rule_()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(bnfParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(bnfParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(bnfParser.ASSIGN, 0)

        def rhs(self):
            return self.getTypedRuleContext(bnfParser.RhsContext,0)


        def getRuleIndex(self):
            return bnfParser.RULE_rule_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_" ):
                listener.enterRule_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_" ):
                listener.exitRule_(self)




    def rule_(self):

        localctx = bnfParser.Rule_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.lhs()
            self.state = 35
            self.match(bnfParser.ASSIGN)
            self.state = 36
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(bnfParser.Id_Context,0)


        def getRuleIndex(self):
            return bnfParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)




    def lhs(self):

        localctx = bnfParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternatives(self):
            return self.getTypedRuleContext(bnfParser.AlternativesContext,0)


        def getRuleIndex(self):
            return bnfParser.RULE_rhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhs" ):
                listener.enterRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhs" ):
                listener.exitRhs(self)




    def rhs(self):

        localctx = bnfParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.alternatives()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(bnfParser.AlternativeContext,i)


        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(bnfParser.BAR)
            else:
                return self.getToken(bnfParser.BAR, i)

        def getRuleIndex(self):
            return bnfParser.RULE_alternatives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternatives" ):
                listener.enterAlternatives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternatives" ):
                listener.exitAlternatives(self)




    def alternatives(self):

        localctx = bnfParser.AlternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_alternatives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.alternative()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==bnfParser.BAR:
                self.state = 43
                self.match(bnfParser.BAR)
                self.state = 44
                self.alternative()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bnfParser.ElementContext)
            else:
                return self.getTypedRuleContext(bnfParser.ElementContext,i)


        def getRuleIndex(self):
            return bnfParser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)




    def alternative(self):

        localctx = bnfParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.element() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_(self):
            return self.getTypedRuleContext(bnfParser.Optional_Context,0)


        def zeroormore(self):
            return self.getTypedRuleContext(bnfParser.ZeroormoreContext,0)


        def oneormore(self):
            return self.getTypedRuleContext(bnfParser.OneormoreContext,0)


        def text_(self):
            return self.getTypedRuleContext(bnfParser.Text_Context,0)


        def id_(self):
            return self.getTypedRuleContext(bnfParser.Id_Context,0)


        def getRuleIndex(self):
            return bnfParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = bnfParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_element)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [bnfParser.REND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.optional_()
                pass
            elif token in [bnfParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.zeroormore()
                pass
            elif token in [bnfParser.RPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.oneormore()
                pass
            elif token in [bnfParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.text_()
                pass
            elif token in [bnfParser.LT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.id_()
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


    class Optional_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REND(self):
            return self.getToken(bnfParser.REND, 0)

        def alternatives(self):
            return self.getTypedRuleContext(bnfParser.AlternativesContext,0)


        def LEND(self):
            return self.getToken(bnfParser.LEND, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_optional_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_" ):
                listener.enterOptional_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_" ):
                listener.exitOptional_(self)




    def optional_(self):

        localctx = bnfParser.Optional_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_optional_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(bnfParser.REND)
            self.state = 64
            self.alternatives()
            self.state = 65
            self.match(bnfParser.LEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ZeroormoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RBRACE(self):
            return self.getToken(bnfParser.RBRACE, 0)

        def alternatives(self):
            return self.getTypedRuleContext(bnfParser.AlternativesContext,0)


        def LBRACE(self):
            return self.getToken(bnfParser.LBRACE, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_zeroormore

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZeroormore" ):
                listener.enterZeroormore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZeroormore" ):
                listener.exitZeroormore(self)




    def zeroormore(self):

        localctx = bnfParser.ZeroormoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_zeroormore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(bnfParser.RBRACE)
            self.state = 68
            self.alternatives()
            self.state = 69
            self.match(bnfParser.LBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OneormoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPAREN(self):
            return self.getToken(bnfParser.RPAREN, 0)

        def alternatives(self):
            return self.getTypedRuleContext(bnfParser.AlternativesContext,0)


        def LPAREN(self):
            return self.getToken(bnfParser.LPAREN, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_oneormore

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOneormore" ):
                listener.enterOneormore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOneormore" ):
                listener.exitOneormore(self)




    def oneormore(self):

        localctx = bnfParser.OneormoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_oneormore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(bnfParser.RPAREN)
            self.state = 72
            self.alternatives()
            self.state = 73
            self.match(bnfParser.LPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Text_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(bnfParser.ID, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_text_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText_" ):
                listener.enterText_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText_" ):
                listener.exitText_(self)




    def text_(self):

        localctx = bnfParser.Text_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_text_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(bnfParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(bnfParser.LT, 0)

        def ruleid(self):
            return self.getTypedRuleContext(bnfParser.RuleidContext,0)


        def GT(self):
            return self.getToken(bnfParser.GT, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_id_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_" ):
                listener.enterId_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_" ):
                listener.exitId_(self)




    def id_(self):

        localctx = bnfParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_id_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(bnfParser.LT)
            self.state = 78
            self.ruleid()
            self.state = 79
            self.match(bnfParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(bnfParser.ID, 0)

        def getRuleIndex(self):
            return bnfParser.RULE_ruleid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleid" ):
                listener.enterRuleid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleid" ):
                listener.exitRuleid(self)




    def ruleid(self):

        localctx = bnfParser.RuleidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ruleid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(bnfParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





