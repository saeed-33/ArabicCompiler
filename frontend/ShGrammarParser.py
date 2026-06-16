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
        4,1,34,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,43,8,1,1,2,1,2,5,2,47,8,2,10,2,12,2,50,9,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,86,8,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,109,8,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,5,12,120,8,12,10,12,12,12,123,9,12,
        1,12,0,1,24,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,4,1,0,12,14,1,
        0,20,21,1,0,18,19,2,0,1,4,22,23,129,0,29,1,0,0,0,2,42,1,0,0,0,4,
        44,1,0,0,0,6,53,1,0,0,0,8,61,1,0,0,0,10,66,1,0,0,0,12,69,1,0,0,0,
        14,72,1,0,0,0,16,78,1,0,0,0,18,87,1,0,0,0,20,93,1,0,0,0,22,96,1,
        0,0,0,24,108,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,29,
        27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,0,0,
        1,33,1,1,0,0,0,34,43,3,6,3,0,35,43,3,8,4,0,36,43,3,14,7,0,37,43,
        3,16,8,0,38,43,3,18,9,0,39,43,3,10,5,0,40,43,3,12,6,0,41,43,3,20,
        10,0,42,34,1,0,0,0,42,35,1,0,0,0,42,36,1,0,0,0,42,37,1,0,0,0,42,
        38,1,0,0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,
        0,44,48,5,26,0,0,45,47,3,2,1,0,46,45,1,0,0,0,47,50,1,0,0,0,48,46,
        1,0,0,0,48,49,1,0,0,0,49,51,1,0,0,0,50,48,1,0,0,0,51,52,5,27,0,0,
        52,5,1,0,0,0,53,54,5,5,0,0,54,55,5,32,0,0,55,56,5,28,0,0,56,57,3,
        22,11,0,57,58,5,17,0,0,58,59,3,24,12,0,59,60,5,29,0,0,60,7,1,0,0,
        0,61,62,5,32,0,0,62,63,5,17,0,0,63,64,3,24,12,0,64,65,5,29,0,0,65,
        9,1,0,0,0,66,67,5,15,0,0,67,68,5,29,0,0,68,11,1,0,0,0,69,70,5,16,
        0,0,70,71,5,29,0,0,71,13,1,0,0,0,72,73,5,9,0,0,73,74,5,24,0,0,74,
        75,3,24,12,0,75,76,5,25,0,0,76,77,5,29,0,0,77,15,1,0,0,0,78,79,5,
        6,0,0,79,80,5,24,0,0,80,81,3,24,12,0,81,82,5,25,0,0,82,85,3,4,2,
        0,83,84,5,7,0,0,84,86,3,4,2,0,85,83,1,0,0,0,85,86,1,0,0,0,86,17,
        1,0,0,0,87,88,5,8,0,0,88,89,5,24,0,0,89,90,3,24,12,0,90,91,5,25,
        0,0,91,92,3,4,2,0,92,19,1,0,0,0,93,94,3,24,12,0,94,95,5,29,0,0,95,
        21,1,0,0,0,96,97,7,0,0,0,97,23,1,0,0,0,98,99,6,12,-1,0,99,100,5,
        24,0,0,100,101,3,24,12,0,101,102,5,25,0,0,102,109,1,0,0,0,103,109,
        5,10,0,0,104,109,5,11,0,0,105,109,5,30,0,0,106,109,5,31,0,0,107,
        109,5,32,0,0,108,98,1,0,0,0,108,103,1,0,0,0,108,104,1,0,0,0,108,
        105,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,121,1,0,0,0,110,
        111,10,8,0,0,111,112,7,1,0,0,112,120,3,24,12,9,113,114,10,7,0,0,
        114,115,7,2,0,0,115,120,3,24,12,8,116,117,10,6,0,0,117,118,7,3,0,
        0,118,120,3,24,12,7,119,110,1,0,0,0,119,113,1,0,0,0,119,116,1,0,
        0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,25,1,0,0,
        0,123,121,1,0,0,0,7,29,42,48,85,108,119,121
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
                     "'\\u0639\\u0634\\u0631\\u064A'", "'\\u0646\\u0635'", 
                     "'\\u0627\\u0643\\u0633\\u0631'", "'\\u062A\\u062C\\u0627\\u0648\\u0632'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'('", 
                     "')'", "'{'", "'}'", "':'", "'\\u061B'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "PRINT", 
                      "TRUE", "FALSE", "INT_T", "FLOAT_T", "STRING_T", "BREAK", 
                      "CONTINUE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COLON", "SEMI", "NUMBER", "STRING", "ID", "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_varDecl = 3
    RULE_assignStmt = 4
    RULE_breakStmt = 5
    RULE_continueStmt = 6
    RULE_printStmt = 7
    RULE_ifStmt = 8
    RULE_whileStmt = 9
    RULE_exprStmt = 10
    RULE_type = 11
    RULE_expr = 12

    ruleNames =  [ "program", "statement", "block", "varDecl", "assignStmt", 
                   "breakStmt", "continueStmt", "printStmt", "ifStmt", "whileStmt", 
                   "exprStmt", "type", "expr" ]

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
    STRING_T=14
    BREAK=15
    CONTINUE=16
    ASSIGN=17
    PLUS=18
    MINUS=19
    MUL=20
    DIV=21
    GT=22
    LT=23
    LPAREN=24
    RPAREN=25
    LBRACE=26
    RBRACE=27
    COLON=28
    SEMI=29
    NUMBER=30
    STRING=31
    ID=32
    WS=33
    LINE_COMMENT=34

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7533072224) != 0):
                self.state = 26
                self.statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
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


        def breakStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(ShGrammarParser.ContinueStmtContext,0)


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
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.printStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.breakStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.continueStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 41
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
            self.state = 44
            self.match(ShGrammarParser.LBRACE)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7533072224) != 0):
                self.state = 45
                self.statement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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
            self.state = 53
            self.match(ShGrammarParser.VAR)
            self.state = 54
            self.match(ShGrammarParser.ID)
            self.state = 55
            self.match(ShGrammarParser.COLON)
            self.state = 56
            self.type_()
            self.state = 57
            self.match(ShGrammarParser.ASSIGN)
            self.state = 58
            self.expr(0)
            self.state = 59
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
            self.state = 61
            self.match(ShGrammarParser.ID)
            self.state = 62
            self.match(ShGrammarParser.ASSIGN)
            self.state = 63
            self.expr(0)
            self.state = 64
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ShGrammarParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = ShGrammarParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ShGrammarParser.BREAK)
            self.state = 67
            self.match(ShGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ShGrammarParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(ShGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return ShGrammarParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = ShGrammarParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ShGrammarParser.CONTINUE)
            self.state = 70
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
        self.enterRule(localctx, 14, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ShGrammarParser.PRINT)
            self.state = 73
            self.match(ShGrammarParser.LPAREN)
            self.state = 74
            self.expr(0)
            self.state = 75
            self.match(ShGrammarParser.RPAREN)
            self.state = 76
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
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ShGrammarParser.IF)
            self.state = 79
            self.match(ShGrammarParser.LPAREN)
            self.state = 80
            self.expr(0)
            self.state = 81
            self.match(ShGrammarParser.RPAREN)
            self.state = 82
            self.block()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 83
                self.match(ShGrammarParser.ELSE)
                self.state = 84
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
        self.enterRule(localctx, 18, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(ShGrammarParser.WHILE)
            self.state = 88
            self.match(ShGrammarParser.LPAREN)
            self.state = 89
            self.expr(0)
            self.state = 90
            self.match(ShGrammarParser.RPAREN)
            self.state = 91
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
        self.enterRule(localctx, 20, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expr(0)
            self.state = 94
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

        def STRING_T(self):
            return self.getToken(ShGrammarParser.STRING_T, 0)

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
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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

        def STRING(self):
            return self.getToken(ShGrammarParser.STRING, 0)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 99
                self.match(ShGrammarParser.LPAREN)
                self.state = 100
                self.expr(0)
                self.state = 101
                self.match(ShGrammarParser.RPAREN)
                pass
            elif token in [10]:
                self.state = 103
                self.match(ShGrammarParser.TRUE)
                pass
            elif token in [11]:
                self.state = 104
                self.match(ShGrammarParser.FALSE)
                pass
            elif token in [30]:
                self.state = 105
                self.match(ShGrammarParser.NUMBER)
                pass
            elif token in [31]:
                self.state = 106
                self.match(ShGrammarParser.STRING)
                pass
            elif token in [32]:
                self.state = 107
                self.match(ShGrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 121
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 119
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 111
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 114
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 117
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 12582942) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        self.expr(7)
                        pass

             
                self.state = 123
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
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




