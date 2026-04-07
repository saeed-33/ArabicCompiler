// Generated from e:/ArabicCompiler/grammar/ShLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ShLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, IF=2, ELSE=3, WHILE=4, PRINT=5, TRUE=6, FALSE=7, INT_T=8, FLOAT_T=9, 
		ASSIGN=10, PLUS=11, MINUS=12, MUL=13, DIV=14, GT=15, LT=16, LPAREN=17, 
		RPAREN=18, LBRACE=19, RBRACE=20, COLON=21, SEMI=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "IF", "ELSE", "WHILE", "PRINT", "TRUE", "FALSE", "INT_T", "FLOAT_T", 
			"ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "COLON", "SEMI"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\\u0645\\u062A\\u063A\\u064A\\u0631'", null, null, "'\\u0628\\u064A\\u0646\\u0645\\u0627'", 
			"'\\u0627\\u0643\\u062A\\u0628'", "'\\u0635\\u062D'", "'\\u063A\\u0644\\u0637'", 
			"'\\u0635\\u062D\\u064A\\u062D'", "'\\u0639\\u0634\\u0631\\u064A'", "'='", 
			"'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'('", "')'", "'{'", "'}'", 
			"':'", "'\\u061B'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "IF", "ELSE", "WHILE", "PRINT", "TRUE", "FALSE", "INT_T", 
			"FLOAT_T", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI"
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


	public ShLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ShLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016}\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001<\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002F\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0000"+
		"\u0000\u0016\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b"+
		"\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b"+
		"\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016"+
		"\u0001\u0000\u0000\u007f\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003"+
		"\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007"+
		"\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001"+
		"\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000"+
		"\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000"+
		"\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000"+
		"\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000"+
		"\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000"+
		"\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000"+
		")\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0001-\u0001"+
		"\u0000\u0000\u0000\u0003;\u0001\u0000\u0000\u0000\u0005E\u0001\u0000\u0000"+
		"\u0000\u0007G\u0001\u0000\u0000\u0000\tM\u0001\u0000\u0000\u0000\u000b"+
		"R\u0001\u0000\u0000\u0000\rU\u0001\u0000\u0000\u0000\u000fY\u0001\u0000"+
		"\u0000\u0000\u0011^\u0001\u0000\u0000\u0000\u0013c\u0001\u0000\u0000\u0000"+
		"\u0015e\u0001\u0000\u0000\u0000\u0017g\u0001\u0000\u0000\u0000\u0019i"+
		"\u0001\u0000\u0000\u0000\u001bk\u0001\u0000\u0000\u0000\u001dm\u0001\u0000"+
		"\u0000\u0000\u001fo\u0001\u0000\u0000\u0000!q\u0001\u0000\u0000\u0000"+
		"#s\u0001\u0000\u0000\u0000%u\u0001\u0000\u0000\u0000\'w\u0001\u0000\u0000"+
		"\u0000)y\u0001\u0000\u0000\u0000+{\u0001\u0000\u0000\u0000-.\u0005\u0645"+
		"\u0000\u0000./\u0005\u062a\u0000\u0000/0\u0005\u063a\u0000\u000001\u0005"+
		"\u064a\u0000\u000012\u0005\u0631\u0000\u00002\u0002\u0001\u0000\u0000"+
		"\u000034\u0005\u0644\u0000\u00004<\u0005\u0648\u0000\u000056\u0005\u0625"+
		"\u0000\u000067\u0005\u0630\u0000\u00007<\u0005\u0627\u0000\u000089\u0005"+
		"\u0627\u0000\u00009:\u0005\u0630\u0000\u0000:<\u0005\u0627\u0000\u0000"+
		";3\u0001\u0000\u0000\u0000;5\u0001\u0000\u0000\u0000;8\u0001\u0000\u0000"+
		"\u0000<\u0004\u0001\u0000\u0000\u0000=>\u0005\u0648\u0000\u0000>?\u0005"+
		"\u0627\u0000\u0000?@\u0005\u0644\u0000\u0000@F\u0005\u0627\u0000\u0000"+
		"AB\u0005\u0648\u0000\u0000BC\u0005\u0625\u0000\u0000CD\u0005\u0644\u0000"+
		"\u0000DF\u0005\u0627\u0000\u0000E=\u0001\u0000\u0000\u0000EA\u0001\u0000"+
		"\u0000\u0000F\u0006\u0001\u0000\u0000\u0000GH\u0005\u0628\u0000\u0000"+
		"HI\u0005\u064a\u0000\u0000IJ\u0005\u0646\u0000\u0000JK\u0005\u0645\u0000"+
		"\u0000KL\u0005\u0627\u0000\u0000L\b\u0001\u0000\u0000\u0000MN\u0005\u0627"+
		"\u0000\u0000NO\u0005\u0643\u0000\u0000OP\u0005\u062a\u0000\u0000PQ\u0005"+
		"\u0628\u0000\u0000Q\n\u0001\u0000\u0000\u0000RS\u0005\u0635\u0000\u0000"+
		"ST\u0005\u062d\u0000\u0000T\f\u0001\u0000\u0000\u0000UV\u0005\u063a\u0000"+
		"\u0000VW\u0005\u0644\u0000\u0000WX\u0005\u0637\u0000\u0000X\u000e\u0001"+
		"\u0000\u0000\u0000YZ\u0005\u0635\u0000\u0000Z[\u0005\u062d\u0000\u0000"+
		"[\\\u0005\u064a\u0000\u0000\\]\u0005\u062d\u0000\u0000]\u0010\u0001\u0000"+
		"\u0000\u0000^_\u0005\u0639\u0000\u0000_`\u0005\u0634\u0000\u0000`a\u0005"+
		"\u0631\u0000\u0000ab\u0005\u064a\u0000\u0000b\u0012\u0001\u0000\u0000"+
		"\u0000cd\u0005=\u0000\u0000d\u0014\u0001\u0000\u0000\u0000ef\u0005+\u0000"+
		"\u0000f\u0016\u0001\u0000\u0000\u0000gh\u0005-\u0000\u0000h\u0018\u0001"+
		"\u0000\u0000\u0000ij\u0005*\u0000\u0000j\u001a\u0001\u0000\u0000\u0000"+
		"kl\u0005/\u0000\u0000l\u001c\u0001\u0000\u0000\u0000mn\u0005>\u0000\u0000"+
		"n\u001e\u0001\u0000\u0000\u0000op\u0005<\u0000\u0000p \u0001\u0000\u0000"+
		"\u0000qr\u0005(\u0000\u0000r\"\u0001\u0000\u0000\u0000st\u0005)\u0000"+
		"\u0000t$\u0001\u0000\u0000\u0000uv\u0005{\u0000\u0000v&\u0001\u0000\u0000"+
		"\u0000wx\u0005}\u0000\u0000x(\u0001\u0000\u0000\u0000yz\u0005:\u0000\u0000"+
		"z*\u0001\u0000\u0000\u0000{|\u0005\u061b\u0000\u0000|,\u0001\u0000\u0000"+
		"\u0000\u0003\u0000;E\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}