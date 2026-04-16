# Generated from ShGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ShGrammarParser import ShGrammarParser
else:
    from ShGrammarParser import ShGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ShGrammarParser.

class ShGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShGrammarParser#program.
    def visitProgram(self, ctx:ShGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#statement.
    def visitStatement(self, ctx:ShGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#block.
    def visitBlock(self, ctx:ShGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#varDecl.
    def visitVarDecl(self, ctx:ShGrammarParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#assignStmt.
    def visitAssignStmt(self, ctx:ShGrammarParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#printStmt.
    def visitPrintStmt(self, ctx:ShGrammarParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#ifStmt.
    def visitIfStmt(self, ctx:ShGrammarParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#whileStmt.
    def visitWhileStmt(self, ctx:ShGrammarParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#exprStmt.
    def visitExprStmt(self, ctx:ShGrammarParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#type.
    def visitType(self, ctx:ShGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShGrammarParser#expr.
    def visitExpr(self, ctx:ShGrammarParser.ExprContext):
        return self.visitChildren(ctx)



del ShGrammarParser