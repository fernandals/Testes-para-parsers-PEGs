// Generated from bnf.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link bnfParser}.
 */
public interface bnfListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link bnfParser#rulelist}.
	 * @param ctx the parse tree
	 */
	void enterRulelist(bnfParser.RulelistContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#rulelist}.
	 * @param ctx the parse tree
	 */
	void exitRulelist(bnfParser.RulelistContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#rule_}.
	 * @param ctx the parse tree
	 */
	void enterRule_(bnfParser.Rule_Context ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#rule_}.
	 * @param ctx the parse tree
	 */
	void exitRule_(bnfParser.Rule_Context ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(bnfParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(bnfParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#rhs}.
	 * @param ctx the parse tree
	 */
	void enterRhs(bnfParser.RhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#rhs}.
	 * @param ctx the parse tree
	 */
	void exitRhs(bnfParser.RhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#alternatives}.
	 * @param ctx the parse tree
	 */
	void enterAlternatives(bnfParser.AlternativesContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#alternatives}.
	 * @param ctx the parse tree
	 */
	void exitAlternatives(bnfParser.AlternativesContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#alternative}.
	 * @param ctx the parse tree
	 */
	void enterAlternative(bnfParser.AlternativeContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#alternative}.
	 * @param ctx the parse tree
	 */
	void exitAlternative(bnfParser.AlternativeContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#element}.
	 * @param ctx the parse tree
	 */
	void enterElement(bnfParser.ElementContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#element}.
	 * @param ctx the parse tree
	 */
	void exitElement(bnfParser.ElementContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#optional_}.
	 * @param ctx the parse tree
	 */
	void enterOptional_(bnfParser.Optional_Context ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#optional_}.
	 * @param ctx the parse tree
	 */
	void exitOptional_(bnfParser.Optional_Context ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#zeroormore}.
	 * @param ctx the parse tree
	 */
	void enterZeroormore(bnfParser.ZeroormoreContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#zeroormore}.
	 * @param ctx the parse tree
	 */
	void exitZeroormore(bnfParser.ZeroormoreContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#oneormore}.
	 * @param ctx the parse tree
	 */
	void enterOneormore(bnfParser.OneormoreContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#oneormore}.
	 * @param ctx the parse tree
	 */
	void exitOneormore(bnfParser.OneormoreContext ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#text_}.
	 * @param ctx the parse tree
	 */
	void enterText_(bnfParser.Text_Context ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#text_}.
	 * @param ctx the parse tree
	 */
	void exitText_(bnfParser.Text_Context ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#id_}.
	 * @param ctx the parse tree
	 */
	void enterId_(bnfParser.Id_Context ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#id_}.
	 * @param ctx the parse tree
	 */
	void exitId_(bnfParser.Id_Context ctx);
	/**
	 * Enter a parse tree produced by {@link bnfParser#ruleid}.
	 * @param ctx the parse tree
	 */
	void enterRuleid(bnfParser.RuleidContext ctx);
	/**
	 * Exit a parse tree produced by {@link bnfParser#ruleid}.
	 * @param ctx the parse tree
	 */
	void exitRuleid(bnfParser.RuleidContext ctx);
}