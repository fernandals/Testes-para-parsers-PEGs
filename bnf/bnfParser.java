// Generated from bnf.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class bnfParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSIGN=1, LPAREN=2, RPAREN=3, LBRACE=4, RBRACE=5, LEND=6, REND=7, BAR=8, 
		GT=9, LT=10, ID=11, WS=12;
	public static final int
		RULE_rulelist = 0, RULE_rule_ = 1, RULE_lhs = 2, RULE_rhs = 3, RULE_alternatives = 4, 
		RULE_alternative = 5, RULE_element = 6, RULE_optional_ = 7, RULE_zeroormore = 8, 
		RULE_oneormore = 9, RULE_text_ = 10, RULE_id_ = 11, RULE_ruleid = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"rulelist", "rule_", "lhs", "rhs", "alternatives", "alternative", "element", 
			"optional_", "zeroormore", "oneormore", "text_", "id_", "ruleid"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'::='", "')'", "'('", "'}'", "'{'", "']'", "'['", "'|'", "'>'", 
			"'<'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LEND", "REND", 
			"BAR", "GT", "LT", "ID", "WS"
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
	public String getGrammarFileName() { return "bnf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public bnfParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RulelistContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(bnfParser.EOF, 0); }
		public List<Rule_Context> rule_() {
			return getRuleContexts(Rule_Context.class);
		}
		public Rule_Context rule_(int i) {
			return getRuleContext(Rule_Context.class,i);
		}
		public RulelistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rulelist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterRulelist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitRulelist(this);
		}
	}

	public final RulelistContext rulelist() throws RecognitionException {
		RulelistContext _localctx = new RulelistContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_rulelist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LT) {
				{
				{
				setState(26);
				rule_();
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
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

	public static class Rule_Context extends ParserRuleContext {
		public LhsContext lhs() {
			return getRuleContext(LhsContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(bnfParser.ASSIGN, 0); }
		public RhsContext rhs() {
			return getRuleContext(RhsContext.class,0);
		}
		public Rule_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterRule_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitRule_(this);
		}
	}

	public final Rule_Context rule_() throws RecognitionException {
		Rule_Context _localctx = new Rule_Context(_ctx, getState());
		enterRule(_localctx, 2, RULE_rule_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			lhs();
			setState(35);
			match(ASSIGN);
			setState(36);
			rhs();
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

	public static class LhsContext extends ParserRuleContext {
		public Id_Context id_() {
			return getRuleContext(Id_Context.class,0);
		}
		public LhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterLhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitLhs(this);
		}
	}

	public final LhsContext lhs() throws RecognitionException {
		LhsContext _localctx = new LhsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_lhs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			id_();
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

	public static class RhsContext extends ParserRuleContext {
		public AlternativesContext alternatives() {
			return getRuleContext(AlternativesContext.class,0);
		}
		public RhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterRhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitRhs(this);
		}
	}

	public final RhsContext rhs() throws RecognitionException {
		RhsContext _localctx = new RhsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_rhs);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			alternatives();
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

	public static class AlternativesContext extends ParserRuleContext {
		public List<AlternativeContext> alternative() {
			return getRuleContexts(AlternativeContext.class);
		}
		public AlternativeContext alternative(int i) {
			return getRuleContext(AlternativeContext.class,i);
		}
		public List<TerminalNode> BAR() { return getTokens(bnfParser.BAR); }
		public TerminalNode BAR(int i) {
			return getToken(bnfParser.BAR, i);
		}
		public AlternativesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alternatives; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterAlternatives(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitAlternatives(this);
		}
	}

	public final AlternativesContext alternatives() throws RecognitionException {
		AlternativesContext _localctx = new AlternativesContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_alternatives);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			alternative();
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(43);
				match(BAR);
				setState(44);
				alternative();
				}
				}
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class AlternativeContext extends ParserRuleContext {
		public List<ElementContext> element() {
			return getRuleContexts(ElementContext.class);
		}
		public ElementContext element(int i) {
			return getRuleContext(ElementContext.class,i);
		}
		public AlternativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alternative; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterAlternative(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitAlternative(this);
		}
	}

	public final AlternativeContext alternative() throws RecognitionException {
		AlternativeContext _localctx = new AlternativeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_alternative);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(50);
					element();
					}
					} 
				}
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
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

	public static class ElementContext extends ParserRuleContext {
		public Optional_Context optional_() {
			return getRuleContext(Optional_Context.class,0);
		}
		public ZeroormoreContext zeroormore() {
			return getRuleContext(ZeroormoreContext.class,0);
		}
		public OneormoreContext oneormore() {
			return getRuleContext(OneormoreContext.class,0);
		}
		public Text_Context text_() {
			return getRuleContext(Text_Context.class,0);
		}
		public Id_Context id_() {
			return getRuleContext(Id_Context.class,0);
		}
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterElement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitElement(this);
		}
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_element);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case REND:
				enterOuterAlt(_localctx, 1);
				{
				setState(56);
				optional_();
				}
				break;
			case RBRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(57);
				zeroormore();
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 3);
				{
				setState(58);
				oneormore();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(59);
				text_();
				}
				break;
			case LT:
				enterOuterAlt(_localctx, 5);
				{
				setState(60);
				id_();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Optional_Context extends ParserRuleContext {
		public TerminalNode REND() { return getToken(bnfParser.REND, 0); }
		public AlternativesContext alternatives() {
			return getRuleContext(AlternativesContext.class,0);
		}
		public TerminalNode LEND() { return getToken(bnfParser.LEND, 0); }
		public Optional_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_optional_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterOptional_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitOptional_(this);
		}
	}

	public final Optional_Context optional_() throws RecognitionException {
		Optional_Context _localctx = new Optional_Context(_ctx, getState());
		enterRule(_localctx, 14, RULE_optional_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(REND);
			setState(64);
			alternatives();
			setState(65);
			match(LEND);
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

	public static class ZeroormoreContext extends ParserRuleContext {
		public TerminalNode RBRACE() { return getToken(bnfParser.RBRACE, 0); }
		public AlternativesContext alternatives() {
			return getRuleContext(AlternativesContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(bnfParser.LBRACE, 0); }
		public ZeroormoreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_zeroormore; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterZeroormore(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitZeroormore(this);
		}
	}

	public final ZeroormoreContext zeroormore() throws RecognitionException {
		ZeroormoreContext _localctx = new ZeroormoreContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_zeroormore);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(RBRACE);
			setState(68);
			alternatives();
			setState(69);
			match(LBRACE);
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

	public static class OneormoreContext extends ParserRuleContext {
		public TerminalNode RPAREN() { return getToken(bnfParser.RPAREN, 0); }
		public AlternativesContext alternatives() {
			return getRuleContext(AlternativesContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(bnfParser.LPAREN, 0); }
		public OneormoreContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_oneormore; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterOneormore(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitOneormore(this);
		}
	}

	public final OneormoreContext oneormore() throws RecognitionException {
		OneormoreContext _localctx = new OneormoreContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_oneormore);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(RPAREN);
			setState(72);
			alternatives();
			setState(73);
			match(LPAREN);
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

	public static class Text_Context extends ParserRuleContext {
		public TerminalNode ID() { return getToken(bnfParser.ID, 0); }
		public Text_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_text_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterText_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitText_(this);
		}
	}

	public final Text_Context text_() throws RecognitionException {
		Text_Context _localctx = new Text_Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_text_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
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

	public static class Id_Context extends ParserRuleContext {
		public TerminalNode LT() { return getToken(bnfParser.LT, 0); }
		public RuleidContext ruleid() {
			return getRuleContext(RuleidContext.class,0);
		}
		public TerminalNode GT() { return getToken(bnfParser.GT, 0); }
		public Id_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterId_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitId_(this);
		}
	}

	public final Id_Context id_() throws RecognitionException {
		Id_Context _localctx = new Id_Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_id_);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(LT);
			setState(78);
			ruleid();
			setState(79);
			match(GT);
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

	public static class RuleidContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(bnfParser.ID, 0); }
		public RuleidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ruleid; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).enterRuleid(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bnfListener ) ((bnfListener)listener).exitRuleid(this);
		}
	}

	public final RuleidContext ruleid() throws RecognitionException {
		RuleidContext _localctx = new RuleidContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_ruleid);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(ID);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16V\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6\63\13\6\3\7\7"+
		"\7\66\n\7\f\7\16\79\13\7\3\b\3\b\3\b\3\b\3\b\5\b@\n\b\3\t\3\t\3\t\3\t"+
		"\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16"+
		"\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2O\2\37\3\2\2\2\4$\3"+
		"\2\2\2\6(\3\2\2\2\b*\3\2\2\2\n,\3\2\2\2\f\67\3\2\2\2\16?\3\2\2\2\20A\3"+
		"\2\2\2\22E\3\2\2\2\24I\3\2\2\2\26M\3\2\2\2\30O\3\2\2\2\32S\3\2\2\2\34"+
		"\36\5\4\3\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2"+
		"\2\2!\37\3\2\2\2\"#\7\2\2\3#\3\3\2\2\2$%\5\6\4\2%&\7\3\2\2&\'\5\b\5\2"+
		"\'\5\3\2\2\2()\5\30\r\2)\7\3\2\2\2*+\5\n\6\2+\t\3\2\2\2,\61\5\f\7\2-."+
		"\7\n\2\2.\60\5\f\7\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2"+
		"\62\13\3\2\2\2\63\61\3\2\2\2\64\66\5\16\b\2\65\64\3\2\2\2\669\3\2\2\2"+
		"\67\65\3\2\2\2\678\3\2\2\28\r\3\2\2\29\67\3\2\2\2:@\5\20\t\2;@\5\22\n"+
		"\2<@\5\24\13\2=@\5\26\f\2>@\5\30\r\2?:\3\2\2\2?;\3\2\2\2?<\3\2\2\2?=\3"+
		"\2\2\2?>\3\2\2\2@\17\3\2\2\2AB\7\t\2\2BC\5\n\6\2CD\7\b\2\2D\21\3\2\2\2"+
		"EF\7\7\2\2FG\5\n\6\2GH\7\6\2\2H\23\3\2\2\2IJ\7\5\2\2JK\5\n\6\2KL\7\4\2"+
		"\2L\25\3\2\2\2MN\7\r\2\2N\27\3\2\2\2OP\7\f\2\2PQ\5\32\16\2QR\7\13\2\2"+
		"R\31\3\2\2\2ST\7\r\2\2T\33\3\2\2\2\6\37\61\67?";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}