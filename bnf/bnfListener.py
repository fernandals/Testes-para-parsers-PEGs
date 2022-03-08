# Generated from bnf.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .bnfParser import bnfParser
else:
    from bnfParser import bnfParser

# This class defines a complete listener for a parse tree produced by bnfParser.
class bnfListener(ParseTreeListener):

    # Enter a parse tree produced by bnfParser#rulelist.
    def enterRulelist(self, ctx:bnfParser.RulelistContext):
        pass

    # Exit a parse tree produced by bnfParser#rulelist.
    def exitRulelist(self, ctx:bnfParser.RulelistContext):
        print("Oh, a rule list...")
        print("The number of child is ", ctx.getChildCount())

    # Enter a parse tree produced by bnfParser#rule_.
    def enterRule_(self, ctx:bnfParser.Rule_Context):
        pass

    # Exit a parse tree produced by bnfParser#rule_.
    def exitRule_(self, ctx:bnfParser.Rule_Context):
        pass


    # Enter a parse tree produced by bnfParser#lhs.
    def enterLhs(self, ctx:bnfParser.LhsContext):
        pass

    # Exit a parse tree produced by bnfParser#lhs.
    def exitLhs(self, ctx:bnfParser.LhsContext):
        pass


    # Enter a parse tree produced by bnfParser#rhs.
    def enterRhs(self, ctx:bnfParser.RhsContext):
        pass

    # Exit a parse tree produced by bnfParser#rhs.
    def exitRhs(self, ctx:bnfParser.RhsContext):
        #print("after id ", ctx.getText())
        pass

    # Enter a parse tree produced by bnfParser#alternatives.
    def enterAlternatives(self, ctx:bnfParser.AlternativesContext):
        pass

    # Exit a parse tree produced by bnfParser#alternatives.
    def exitAlternatives(self, ctx:bnfParser.AlternativesContext):
        print(ctx.getText())
        #pass


    # Enter a parse tree produced by bnfParser#alternative.
    def enterAlternative(self, ctx:bnfParser.AlternativeContext):
        pass

    # Exit a parse tree produced by bnfParser#alternative.
    def exitAlternative(self, ctx:bnfParser.AlternativeContext):
        pass


    # Enter a parse tree produced by bnfParser#element.
    def enterElement(self, ctx:bnfParser.ElementContext):
        pass

    # Exit a parse tree produced by bnfParser#element.
    def exitElement(self, ctx:bnfParser.ElementContext):
        pass

    # Enter a parse tree produced by bnfParser#optional_.
    def enterOptional_(self, ctx:bnfParser.Optional_Context):
        pass

    # Exit a parse tree produced by bnfParser#optional_.
    def exitOptional_(self, ctx:bnfParser.Optional_Context):
        pass


    # Enter a parse tree produced by bnfParser#zeroormore.
    def enterZeroormore(self, ctx:bnfParser.ZeroormoreContext):
        pass

    # Exit a parse tree produced by bnfParser#zeroormore.
    def exitZeroormore(self, ctx:bnfParser.ZeroormoreContext):
        pass


    # Enter a parse tree produced by bnfParser#oneormore.
    def enterOneormore(self, ctx:bnfParser.OneormoreContext):
        pass

    # Exit a parse tree produced by bnfParser#oneormore.
    def exitOneormore(self, ctx:bnfParser.OneormoreContext):
        pass


    # Enter a parse tree produced by bnfParser#text_.
    def enterText_(self, ctx:bnfParser.Text_Context):
        pass

    # Exit a parse tree produced by bnfParser#text_.
    def exitText_(self, ctx:bnfParser.Text_Context):
        pass


    # Enter a parse tree produced by bnfParser#id_.
    def enterId_(self, ctx:bnfParser.Id_Context):
        pass

    # Exit a parse tree produced by bnfParser#id_.
    def exitId_(self, ctx:bnfParser.Id_Context):
        #id = ctx.getText()
        #print(id)
        pass

    # Enter a parse tree produced by bnfParser#ruleid.
    def enterRuleid(self, ctx:bnfParser.RuleidContext):
        pass

    # Exit a parse tree produced by bnfParser#ruleid.
    def exitRuleid(self, ctx:bnfParser.RuleidContext):
        pass

# custom behavior
class MyTest(bnfListener):
    def exitRule_(self, ctx:bnfParser.Rule_Context):
        print("Oh, a rule!")


del bnfParser
