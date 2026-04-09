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
        4,1,26,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,47,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,58,
        8,5,10,5,12,5,61,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,4,1,0,8,9,1,0,13,
        14,1,0,11,12,1,0,15,16,65,0,15,1,0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,
        6,32,1,0,0,0,8,35,1,0,0,0,10,46,1,0,0,0,12,14,3,2,1,0,13,12,1,0,
        0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,
        1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,23,3,4,2,0,21,23,3,6,3,0,22,
        20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,1,0,0,25,26,5,24,0,
        0,26,27,5,21,0,0,27,28,3,8,4,0,28,29,5,10,0,0,29,30,3,10,5,0,30,
        31,5,22,0,0,31,5,1,0,0,0,32,33,3,10,5,0,33,34,5,22,0,0,34,7,1,0,
        0,0,35,36,7,0,0,0,36,9,1,0,0,0,37,38,6,5,-1,0,38,39,5,17,0,0,39,
        40,3,10,5,0,40,41,5,18,0,0,41,47,1,0,0,0,42,47,5,6,0,0,43,47,5,7,
        0,0,44,47,5,23,0,0,45,47,5,24,0,0,46,37,1,0,0,0,46,42,1,0,0,0,46,
        43,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,59,1,0,0,0,48,49,10,7,
        0,0,49,50,7,1,0,0,50,58,3,10,5,8,51,52,10,6,0,0,52,53,7,2,0,0,53,
        58,3,10,5,7,54,55,10,5,0,0,55,56,7,3,0,0,56,58,3,10,5,6,57,48,1,
        0,0,0,57,51,1,0,0,0,57,54,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,
        60,1,0,0,0,60,11,1,0,0,0,61,59,1,0,0,0,5,15,22,46,57,59
    ]

class ShGrammarParser ( Parser ):

    grammarFileName = "ShGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u0645\\u062A\\u063A\\u064A\\u0631'", 
                     "<INVALID>", "<INVALID>", "'\\u0628\\u064A\\u0646\\u0645\\u0627'", 
                     "'\\u0627\\u0643\\u062A\\u0628'", "'\\u0635\\u062D'", 
                     "'\\u063A\\u0644\\u0637'", "'\\u0635\\u062D\\u064A\\u062D'", 
                     "'\\u0639\\u0634\\u0631\\u064A'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'>'", "'<'", "'('", "')'", "'{'", "'}'", 
                     "':'", "'\\u061B'" ]

    symbolicNames = [ "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "PRINT", 
                      "TRUE", "FALSE", "INT_T", "FLOAT_T", "ASSIGN", "PLUS", 
                      "MINUS", "MUL", "DIV", "GT", "LT", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "COLON", "SEMI", "NUMBER", "ID", 
                      "WS", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDecl = 2
    RULE_exprStmt = 3
    RULE_type = 4
    RULE_expr = 5

    ruleNames =  [ "program", "statement", "varDecl", "exprStmt", "type", 
                   "expr" ]

    EOF = Token.EOF
    VAR=1
    IF=2
    ELSE=3
    WHILE=4
    PRINT=5
    TRUE=6
    FALSE=7
    INT_T=8
    FLOAT_T=9
    ASSIGN=10
    PLUS=11
    MINUS=12
    MUL=13
    DIV=14
    GT=15
    LT=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    COLON=21
    SEMI=22
    NUMBER=23
    ID=24
    WS=25
    LINE_COMMENT=26

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




    def program(self):

        localctx = ShGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 25297090) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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




    def statement(self):

        localctx = ShGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.varDecl()
                pass
            elif token in [6, 7, 17, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.exprStmt()
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




    def varDecl(self):

        localctx = ShGrammarParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ShGrammarParser.VAR)
            self.state = 25
            self.match(ShGrammarParser.ID)
            self.state = 26
            self.match(ShGrammarParser.COLON)
            self.state = 27
            self.type_()
            self.state = 28
            self.match(ShGrammarParser.ASSIGN)
            self.state = 29
            self.expr(0)
            self.state = 30
            self.match(ShGrammarParser.SEMI)
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




    def exprStmt(self):

        localctx = ShGrammarParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.expr(0)
            self.state = 33
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




    def type_(self):

        localctx = ShGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 38
                self.match(ShGrammarParser.LPAREN)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(ShGrammarParser.RPAREN)
                pass
            elif token in [6]:
                self.state = 42
                self.match(ShGrammarParser.TRUE)
                pass
            elif token in [7]:
                self.state = 43
                self.match(ShGrammarParser.FALSE)
                pass
            elif token in [23]:
                self.state = 44
                self.match(ShGrammarParser.NUMBER)
                pass
            elif token in [24]:
                self.state = 45
                self.match(ShGrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 49
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 52
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ShGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(6)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self._predicates[5] = self.expr_sempred
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
         




