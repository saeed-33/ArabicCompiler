# Generated from ShGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,74,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,96,8,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,107,8,10,10,10,12,10,110,9,10,
        1,10,0,1,20,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,12,13,1,0,17,
        18,1,0,15,16,2,0,1,4,19,20,115,0,25,1,0,0,0,2,36,1,0,0,0,4,38,1,
        0,0,0,6,47,1,0,0,0,8,55,1,0,0,0,10,60,1,0,0,0,12,66,1,0,0,0,14,75,
        1,0,0,0,16,81,1,0,0,0,18,84,1,0,0,0,20,95,1,0,0,0,22,24,3,2,1,0,
        23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,
        0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,37,3,6,3,0,31,
        37,3,8,4,0,32,37,3,10,5,0,33,37,3,12,6,0,34,37,3,14,7,0,35,37,3,
        16,8,0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,36,
        34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,42,5,23,0,0,39,41,3,2,1,
        0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,
        1,0,0,0,44,42,1,0,0,0,45,46,5,24,0,0,46,5,1,0,0,0,47,48,5,5,0,0,
        48,49,5,28,0,0,49,50,5,25,0,0,50,51,3,18,9,0,51,52,5,14,0,0,52,53,
        3,20,10,0,53,54,5,26,0,0,54,7,1,0,0,0,55,56,5,28,0,0,56,57,5,14,
        0,0,57,58,3,20,10,0,58,59,5,26,0,0,59,9,1,0,0,0,60,61,5,9,0,0,61,
        62,5,21,0,0,62,63,3,20,10,0,63,64,5,22,0,0,64,65,5,26,0,0,65,11,
        1,0,0,0,66,67,5,6,0,0,67,68,5,21,0,0,68,69,3,20,10,0,69,70,5,22,
        0,0,70,73,3,4,2,0,71,72,5,7,0,0,72,74,3,4,2,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,13,1,0,0,0,75,76,5,8,0,0,76,77,5,21,0,0,77,78,3,20,10,
        0,78,79,5,22,0,0,79,80,3,4,2,0,80,15,1,0,0,0,81,82,3,20,10,0,82,
        83,5,26,0,0,83,17,1,0,0,0,84,85,7,0,0,0,85,19,1,0,0,0,86,87,6,10,
        -1,0,87,88,5,21,0,0,88,89,3,20,10,0,89,90,5,22,0,0,90,96,1,0,0,0,
        91,96,5,10,0,0,92,96,5,11,0,0,93,96,5,27,0,0,94,96,5,28,0,0,95,86,
        1,0,0,0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,
        96,108,1,0,0,0,97,98,10,7,0,0,98,99,7,1,0,0,99,107,3,20,10,8,100,
        101,10,6,0,0,101,102,7,2,0,0,102,107,3,20,10,7,103,104,10,5,0,0,
        104,105,7,3,0,0,105,107,3,20,10,6,106,97,1,0,0,0,106,100,1,0,0,0,
        106,103,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,
        109,21,1,0,0,0,110,108,1,0,0,0,7,25,36,42,73,95,106,108
    ]

class ShGrammarParser ( Parser ):

    grammarFileName = "ShGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'=='", "'!='", "'<='", "'>='", "'\\u0645\\u062A\\u063A\\u064A\\u0631'", 
                     "<INVALID>", "<INVALID>", "'\\u0628\\u064A\\u0646\\u0645\\u0627'", 
                     "'\\u0627\\u0643\\u062A\\u0628'", "'\\u0635\\u062D'", 
                     "'\\u063A\\u0644\\u0637'", "'\\u0635\\u062D\\u064A\\u062D'", 
                     "'\\u0639\\u0634\\u0631\\u064A'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'('", "')'", "'{'", "'}'", 
                     "':'", "'\\u061B'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "PRINT", 
                      "TRUE", "FALSE", "INT_T", "FLOAT_T", "ASSIGN", "PLUS", 
                      "MINUS", "MUL", "DIV", "GT", "LT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "COLON", "SEMI", "NUMBER", "ID", 
                      "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_varDecl = 3
    RULE_assignStmt = 4
    RULE_printStmt = 5
    RULE_ifStmt = 6
    RULE_whileStmt = 7
    RULE_exprStmt = 8
    RULE_type = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "block", "varDecl", "assignStmt", 
                   "printStmt", "ifStmt", "whileStmt", "exprStmt", "type", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    VAR=5
    IF=6
    ELSE=7
    WHILE=8
    PRINT=9
    TRUE=10
    FALSE=11
    INT_T=12
    FLOAT_T=13
    ASSIGN=14
    PLUS=15
    MINUS=16
    MUL=17
    DIV=18
    GT=19
    LT=20
    LPAREN=21
    RPAREN=22
    LBRACE=23
    RBRACE=24
    COLON=25
    SEMI=26
    NUMBER=27
    ID=28
    WS=29
    LINE_COMMENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ShGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ShGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ShGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ShGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 404754272) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(ShGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ShGrammarParser.VarDeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.AssignStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.WhileStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return ShGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ShGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.printStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.exprStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ShGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ShGrammarParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(ShGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return ShGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ShGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ShGrammarParser.LBRACE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 404754272) != 0):
                self.state = 39
                self.statement()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(ShGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ShGrammarParser.VAR, 0)

        def ID(self):
            return self.getToken(ShGrammarParser.ID, 0)

        def COLON(self):
            return self.getToken(ShGrammarParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(ShGrammarParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(ShGrammarParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ShGrammarParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ShGrammarParser.VAR)
            self.state = 48
            self.match(ShGrammarParser.ID)
            self.state = 49
            self.match(ShGrammarParser.COLON)
            self.state = 50
            self.type_()
            self.state = 51
            self.match(ShGrammarParser.ASSIGN)
            self.state = 52
            self.expr(0)
            self.state = 53
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ShGrammarParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ShGrammarParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = ShGrammarParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ShGrammarParser.ID)
            self.state = 56
            self.match(ShGrammarParser.ASSIGN)
            self.state = 57
            self.expr(0)
            self.state = 58
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ShGrammarParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(ShGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ShGrammarParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = ShGrammarParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ShGrammarParser.PRINT)
            self.state = 61
            self.match(ShGrammarParser.LPAREN)
            self.state = 62
            self.expr(0)
            self.state = 63
            self.match(ShGrammarParser.RPAREN)
            self.state = 64
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ShGrammarParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ShGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ShGrammarParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShGrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(ShGrammarParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ShGrammarParser.ELSE, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = ShGrammarParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ShGrammarParser.IF)
            self.state = 67
            self.match(ShGrammarParser.LPAREN)
            self.state = 68
            self.expr(0)
            self.state = 69
            self.match(ShGrammarParser.RPAREN)
            self.state = 70
            self.block()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 71
                self.match(ShGrammarParser.ELSE)
                self.state = 72
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ShGrammarParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ShGrammarParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ShGrammarParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ShGrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return ShGrammarParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = ShGrammarParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ShGrammarParser.WHILE)
            self.state = 76
            self.match(ShGrammarParser.LPAREN)
            self.state = 77
            self.expr(0)
            self.state = 78
            self.match(ShGrammarParser.RPAREN)
            self.state = 79
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ShGrammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = ShGrammarParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.expr(0)
            self.state = 82
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_T(self):
            return self.getToken(ShGrammarParser.INT_T, 0)

        def FLOAT_T(self):
            return self.getToken(ShGrammarParser.FLOAT_T, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ShGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ShGrammarParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(ShGrammarParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ShGrammarParser.RPAREN, 0)

        def TRUE(self):
            return self.getToken(ShGrammarParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ShGrammarParser.FALSE, 0)

        def NUMBER(self):
            return self.getToken(ShGrammarParser.NUMBER, 0)

        def ID(self):
            return self.getToken(ShGrammarParser.ID, 0)

        def MUL(self):
            return self.getToken(ShGrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(ShGrammarParser.DIV, 0)

        def PLUS(self):
            return self.getToken(ShGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ShGrammarParser.MINUS, 0)

        def GT(self):
            return self.getToken(ShGrammarParser.GT, 0)

        def LT(self):
            return self.getToken(ShGrammarParser.LT, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.state = 87
                self.match(ShGrammarParser.LPAREN)
                self.state = 88
                self.expr(0)
                self.state = 89
                self.match(ShGrammarParser.RPAREN)
                pass
            elif token in [10]:
                self.state = 91
                self.match(ShGrammarParser.TRUE)
                pass
            elif token in [11]:
                self.state = 92
                self.match(ShGrammarParser.FALSE)
                pass
            elif token in [27]:
                self.state = 93
                self.match(ShGrammarParser.NUMBER)
                pass
            elif token in [28]:
                self.state = 94
                self.match(ShGrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 106
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 98
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 101
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 104
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1572894) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(6)
                        pass

             
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




