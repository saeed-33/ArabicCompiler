// Generated from c:/Users/USER/Desktop/Sh3raa/ArabicCompiler/grammar/ShGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ShGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, VAR=5, IF=6, ELSE=7, WHILE=8, PRINT=9, 
		TRUE=10, FALSE=11, INT_T=12, FLOAT_T=13, ASSIGN=14, PLUS=15, MINUS=16, 
		MUL=17, DIV=18, GT=19, LT=20, LPAREN=21, RPAREN=22, LBRACE=23, RBRACE=24, 
		COLON=25, SEMI=26, NUMBER=27, ID=28, WS=29, LINE_COMMENT=30;
	public static final int
		RULE_program = 0, RULE_statement = 1, RULE_block = 2, RULE_varDecl = 3, 
		RULE_assignStmt = 4, RULE_printStmt = 5, RULE_ifStmt = 6, RULE_whileStmt = 7, 
		RULE_exprStmt = 8, RULE_type = 9, RULE_expr = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "statement", "block", "varDecl", "assignStmt", "printStmt", 
			"ifStmt", "whileStmt", "exprStmt", "type", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'=='", "'!='", "'<='", "'>='", "'\\u0645\\u062A\\u063A\\u064A\\u0631'", 
			null, null, "'\\u0628\\u064A\\u0646\\u0645\\u0627'", "'\\u0627\\u0643\\u062A\\u0628'", 
			"'\\u0635\\u062D'", "'\\u063A\\u0644\\u0637'", "'\\u0635\\u062D\\u064A\\u062D'", 
			"'\\u0639\\u0634\\u0631\\u064A'", "'='", "'+'", "'-'", "'*'", "'/'", 
			"'>'", "'<'", "'('", "')'", "'{'", "'}'", "':'", "'\\u061B'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "VAR", "IF", "ELSE", "WHILE", "PRINT", 
			"TRUE", "FALSE", "INT_T", "FLOAT_T", "ASSIGN", "PLUS", "MINUS", "MUL", 
			"DIV", "GT", "LT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", 
			"NUMBER", "ID", "WS", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ShGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ShGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ShGrammarParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 404754272L) != 0)) {
				{
				{
				setState(22);
				statement();
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(28);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public VarDeclContext varDecl() {
			return getRuleContext(VarDeclContext.class,0);
		}
		public AssignStmtContext assignStmt() {
			return getRuleContext(AssignStmtContext.class,0);
		}
		public PrintStmtContext printStmt() {
			return getRuleContext(PrintStmtContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public WhileStmtContext whileStmt() {
			return getRuleContext(WhileStmtContext.class,0);
		}
		public ExprStmtContext exprStmt() {
			return getRuleContext(ExprStmtContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(36);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				varDecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(31);
				assignStmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(32);
				printStmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				ifStmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(34);
				whileStmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(35);
				exprStmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(ShGrammarParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ShGrammarParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(LBRACE);
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 404754272L) != 0)) {
				{
				{
				setState(39);
				statement();
				}
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(45);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarDeclContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(ShGrammarParser.VAR, 0); }
		public TerminalNode ID() { return getToken(ShGrammarParser.ID, 0); }
		public TerminalNode COLON() { return getToken(ShGrammarParser.COLON, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(ShGrammarParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ShGrammarParser.SEMI, 0); }
		public VarDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecl; }
	}

	public final VarDeclContext varDecl() throws RecognitionException {
		VarDeclContext _localctx = new VarDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_varDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(VAR);
			setState(48);
			match(ID);
			setState(49);
			match(COLON);
			setState(50);
			type();
			setState(51);
			match(ASSIGN);
			setState(52);
			expr(0);
			setState(53);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignStmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ShGrammarParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(ShGrammarParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ShGrammarParser.SEMI, 0); }
		public AssignStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignStmt; }
	}

	public final AssignStmtContext assignStmt() throws RecognitionException {
		AssignStmtContext _localctx = new AssignStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assignStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(ID);
			setState(56);
			match(ASSIGN);
			setState(57);
			expr(0);
			setState(58);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintStmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(ShGrammarParser.PRINT, 0); }
		public TerminalNode LPAREN() { return getToken(ShGrammarParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ShGrammarParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(ShGrammarParser.SEMI, 0); }
		public PrintStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStmt; }
	}

	public final PrintStmtContext printStmt() throws RecognitionException {
		PrintStmtContext _localctx = new PrintStmtContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_printStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(PRINT);
			setState(61);
			match(LPAREN);
			setState(62);
			expr(0);
			setState(63);
			match(RPAREN);
			setState(64);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfStmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(ShGrammarParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(ShGrammarParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ShGrammarParser.RPAREN, 0); }
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ShGrammarParser.ELSE, 0); }
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(IF);
			setState(67);
			match(LPAREN);
			setState(68);
			expr(0);
			setState(69);
			match(RPAREN);
			setState(70);
			block();
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(71);
				match(ELSE);
				setState(72);
				block();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileStmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(ShGrammarParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(ShGrammarParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ShGrammarParser.RPAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStmt; }
	}

	public final WhileStmtContext whileStmt() throws RecognitionException {
		WhileStmtContext _localctx = new WhileStmtContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_whileStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(WHILE);
			setState(76);
			match(LPAREN);
			setState(77);
			expr(0);
			setState(78);
			match(RPAREN);
			setState(79);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprStmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(ShGrammarParser.SEMI, 0); }
		public ExprStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprStmt; }
	}

	public final ExprStmtContext exprStmt() throws RecognitionException {
		ExprStmtContext _localctx = new ExprStmtContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_exprStmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			expr(0);
			setState(82);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT_T() { return getToken(ShGrammarParser.INT_T, 0); }
		public TerminalNode FLOAT_T() { return getToken(ShGrammarParser.FLOAT_T, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			_la = _input.LA(1);
			if ( !(_la==INT_T || _la==FLOAT_T) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(ShGrammarParser.LPAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(ShGrammarParser.RPAREN, 0); }
		public TerminalNode TRUE() { return getToken(ShGrammarParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(ShGrammarParser.FALSE, 0); }
		public TerminalNode NUMBER() { return getToken(ShGrammarParser.NUMBER, 0); }
		public TerminalNode ID() { return getToken(ShGrammarParser.ID, 0); }
		public TerminalNode MUL() { return getToken(ShGrammarParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ShGrammarParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(ShGrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ShGrammarParser.MINUS, 0); }
		public TerminalNode GT() { return getToken(ShGrammarParser.GT, 0); }
		public TerminalNode LT() { return getToken(ShGrammarParser.LT, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				{
				setState(87);
				match(LPAREN);
				setState(88);
				expr(0);
				setState(89);
				match(RPAREN);
				}
				break;
			case TRUE:
				{
				setState(91);
				match(TRUE);
				}
				break;
			case FALSE:
				{
				setState(92);
				match(FALSE);
				}
				break;
			case NUMBER:
				{
				setState(93);
				match(NUMBER);
				}
				break;
			case ID:
				{
				setState(94);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(108);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(106);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(97);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(98);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(99);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(100);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(101);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(102);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(103);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(104);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1572894L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(105);
						expr(6);
						}
						break;
					}
					} 
				}
				setState(110);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 10:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001ep\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0005\u0000\u0018"+
		"\b\u0000\n\u0000\f\u0000\u001b\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"%\b\u0001\u0001\u0002\u0001\u0002\u0005\u0002)\b\u0002\n\u0002\f\u0002"+
		",\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"J\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n`\b\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005"+
		"\nk\b\n\n\n\f\nn\t\n\u0001\n\u0000\u0001\u0014\u000b\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0000\u0004\u0001\u0000\f\r\u0001"+
		"\u0000\u0011\u0012\u0001\u0000\u000f\u0010\u0002\u0000\u0001\u0004\u0013"+
		"\u0014s\u0000\u0019\u0001\u0000\u0000\u0000\u0002$\u0001\u0000\u0000\u0000"+
		"\u0004&\u0001\u0000\u0000\u0000\u0006/\u0001\u0000\u0000\u0000\b7\u0001"+
		"\u0000\u0000\u0000\n<\u0001\u0000\u0000\u0000\fB\u0001\u0000\u0000\u0000"+
		"\u000eK\u0001\u0000\u0000\u0000\u0010Q\u0001\u0000\u0000\u0000\u0012T"+
		"\u0001\u0000\u0000\u0000\u0014_\u0001\u0000\u0000\u0000\u0016\u0018\u0003"+
		"\u0002\u0001\u0000\u0017\u0016\u0001\u0000\u0000\u0000\u0018\u001b\u0001"+
		"\u0000\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u0019\u001a\u0001"+
		"\u0000\u0000\u0000\u001a\u001c\u0001\u0000\u0000\u0000\u001b\u0019\u0001"+
		"\u0000\u0000\u0000\u001c\u001d\u0005\u0000\u0000\u0001\u001d\u0001\u0001"+
		"\u0000\u0000\u0000\u001e%\u0003\u0006\u0003\u0000\u001f%\u0003\b\u0004"+
		"\u0000 %\u0003\n\u0005\u0000!%\u0003\f\u0006\u0000\"%\u0003\u000e\u0007"+
		"\u0000#%\u0003\u0010\b\u0000$\u001e\u0001\u0000\u0000\u0000$\u001f\u0001"+
		"\u0000\u0000\u0000$ \u0001\u0000\u0000\u0000$!\u0001\u0000\u0000\u0000"+
		"$\"\u0001\u0000\u0000\u0000$#\u0001\u0000\u0000\u0000%\u0003\u0001\u0000"+
		"\u0000\u0000&*\u0005\u0017\u0000\u0000\')\u0003\u0002\u0001\u0000(\'\u0001"+
		"\u0000\u0000\u0000),\u0001\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000"+
		"*+\u0001\u0000\u0000\u0000+-\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000"+
		"\u0000-.\u0005\u0018\u0000\u0000.\u0005\u0001\u0000\u0000\u0000/0\u0005"+
		"\u0005\u0000\u000001\u0005\u001c\u0000\u000012\u0005\u0019\u0000\u0000"+
		"23\u0003\u0012\t\u000034\u0005\u000e\u0000\u000045\u0003\u0014\n\u0000"+
		"56\u0005\u001a\u0000\u00006\u0007\u0001\u0000\u0000\u000078\u0005\u001c"+
		"\u0000\u000089\u0005\u000e\u0000\u00009:\u0003\u0014\n\u0000:;\u0005\u001a"+
		"\u0000\u0000;\t\u0001\u0000\u0000\u0000<=\u0005\t\u0000\u0000=>\u0005"+
		"\u0015\u0000\u0000>?\u0003\u0014\n\u0000?@\u0005\u0016\u0000\u0000@A\u0005"+
		"\u001a\u0000\u0000A\u000b\u0001\u0000\u0000\u0000BC\u0005\u0006\u0000"+
		"\u0000CD\u0005\u0015\u0000\u0000DE\u0003\u0014\n\u0000EF\u0005\u0016\u0000"+
		"\u0000FI\u0003\u0004\u0002\u0000GH\u0005\u0007\u0000\u0000HJ\u0003\u0004"+
		"\u0002\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000J\r\u0001"+
		"\u0000\u0000\u0000KL\u0005\b\u0000\u0000LM\u0005\u0015\u0000\u0000MN\u0003"+
		"\u0014\n\u0000NO\u0005\u0016\u0000\u0000OP\u0003\u0004\u0002\u0000P\u000f"+
		"\u0001\u0000\u0000\u0000QR\u0003\u0014\n\u0000RS\u0005\u001a\u0000\u0000"+
		"S\u0011\u0001\u0000\u0000\u0000TU\u0007\u0000\u0000\u0000U\u0013\u0001"+
		"\u0000\u0000\u0000VW\u0006\n\uffff\uffff\u0000WX\u0005\u0015\u0000\u0000"+
		"XY\u0003\u0014\n\u0000YZ\u0005\u0016\u0000\u0000Z`\u0001\u0000\u0000\u0000"+
		"[`\u0005\n\u0000\u0000\\`\u0005\u000b\u0000\u0000]`\u0005\u001b\u0000"+
		"\u0000^`\u0005\u001c\u0000\u0000_V\u0001\u0000\u0000\u0000_[\u0001\u0000"+
		"\u0000\u0000_\\\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_^\u0001"+
		"\u0000\u0000\u0000`l\u0001\u0000\u0000\u0000ab\n\u0007\u0000\u0000bc\u0007"+
		"\u0001\u0000\u0000ck\u0003\u0014\n\bde\n\u0006\u0000\u0000ef\u0007\u0002"+
		"\u0000\u0000fk\u0003\u0014\n\u0007gh\n\u0005\u0000\u0000hi\u0007\u0003"+
		"\u0000\u0000ik\u0003\u0014\n\u0006ja\u0001\u0000\u0000\u0000jd\u0001\u0000"+
		"\u0000\u0000jg\u0001\u0000\u0000\u0000kn\u0001\u0000\u0000\u0000lj\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000m\u0015\u0001\u0000\u0000"+
		"\u0000nl\u0001\u0000\u0000\u0000\u0007\u0019$*I_jl";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}