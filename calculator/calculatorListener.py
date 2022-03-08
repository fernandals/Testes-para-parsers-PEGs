# Generated from calculator.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calculatorParser import calculatorParser
else:
    from calculatorParser import calculatorParser

# This class defines a complete listener for a parse tree produced by calculatorParser.
class calculatorListener(ParseTreeListener):

    # Enter a parse tree produced by calculatorParser#equation.
    def enterEquation(self, ctx:calculatorParser.EquationContext):
        print("entrei na equação")
        pass

    # Exit a parse tree produced by calculatorParser#equation.
    def exitEquation(self, ctx:calculatorParser.EquationContext):
        pass

    # Enter a parse tree produced by calculatorParser#expression.
    def enterExpression(self, ctx:calculatorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by calculatorParser#expression.
    def exitExpression(self, ctx:calculatorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by calculatorParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:calculatorParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by calculatorParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:calculatorParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by calculatorParser#powExpression.
    def enterPowExpression(self, ctx:calculatorParser.PowExpressionContext):
        pass

    # Exit a parse tree produced by calculatorParser#powExpression.
    def exitPowExpression(self, ctx:calculatorParser.PowExpressionContext):
        pass


    # Enter a parse tree produced by calculatorParser#signedAtom.
    def enterSignedAtom(self, ctx:calculatorParser.SignedAtomContext):
        pass

    # Exit a parse tree produced by calculatorParser#signedAtom.
    def exitSignedAtom(self, ctx:calculatorParser.SignedAtomContext):
        pass


    # Enter a parse tree produced by calculatorParser#atom.
    def enterAtom(self, ctx:calculatorParser.AtomContext):
        pass

    # Exit a parse tree produced by calculatorParser#atom.
    def exitAtom(self, ctx:calculatorParser.AtomContext):
        pass


    # Enter a parse tree produced by calculatorParser#scientific.
    def enterScientific(self, ctx:calculatorParser.ScientificContext):
        pass

    # Exit a parse tree produced by calculatorParser#scientific.
    def exitScientific(self, ctx:calculatorParser.ScientificContext):
        pass


    # Enter a parse tree produced by calculatorParser#constant.
    def enterConstant(self, ctx:calculatorParser.ConstantContext):
        pass

    # Exit a parse tree produced by calculatorParser#constant.
    def exitConstant(self, ctx:calculatorParser.ConstantContext):
        pass


    # Enter a parse tree produced by calculatorParser#variable.
    def enterVariable(self, ctx:calculatorParser.VariableContext):
        pass

    # Exit a parse tree produced by calculatorParser#variable.
    def exitVariable(self, ctx:calculatorParser.VariableContext):
        pass


    # Enter a parse tree produced by calculatorParser#func_.
    def enterFunc_(self, ctx:calculatorParser.Func_Context):
        pass

    # Exit a parse tree produced by calculatorParser#func_.
    def exitFunc_(self, ctx:calculatorParser.Func_Context):
        pass


    # Enter a parse tree produced by calculatorParser#funcname.
    def enterFuncname(self, ctx:calculatorParser.FuncnameContext):
        pass

    # Exit a parse tree produced by calculatorParser#funcname.
    def exitFuncname(self, ctx:calculatorParser.FuncnameContext):
        pass


    # Enter a parse tree produced by calculatorParser#relop.
    def enterRelop(self, ctx:calculatorParser.RelopContext):
        pass

    # Exit a parse tree produced by calculatorParser#relop.
    def exitRelop(self, ctx:calculatorParser.RelopContext):
        pass



del calculatorParser
