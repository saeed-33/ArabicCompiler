# Generated from ShGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ShGrammarParser import ShGrammarParser
else:
    from ShGrammarParser import ShGrammarParser

# This class defines a complete listener for a parse tree produced by ShGrammarParser.
class ShGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ShGrammarParser#program.
    def enterProgram(self, ctx:ShGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#program.
    def exitProgram(self, ctx:ShGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by ShGrammarParser#statement.
    def enterStatement(self, ctx:ShGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#statement.
    def exitStatement(self, ctx:ShGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by ShGrammarParser#varDecl.
    def enterVarDecl(self, ctx:ShGrammarParser.VarDeclContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#varDecl.
    def exitVarDecl(self, ctx:ShGrammarParser.VarDeclContext):
        pass


    # Enter a parse tree produced by ShGrammarParser#exprStmt.
    def enterExprStmt(self, ctx:ShGrammarParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#exprStmt.
    def exitExprStmt(self, ctx:ShGrammarParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ShGrammarParser#type.
    def enterType(self, ctx:ShGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#type.
    def exitType(self, ctx:ShGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by ShGrammarParser#expr.
    def enterExpr(self, ctx:ShGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by ShGrammarParser#expr.
    def exitExpr(self, ctx:ShGrammarParser.ExprContext):
        pass



del ShGrammarParser