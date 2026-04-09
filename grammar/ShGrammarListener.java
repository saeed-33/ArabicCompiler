// Generated from ShGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ShGrammarParser}.
 */
public interface ShGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ShGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ShGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ShGrammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ShGrammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void enterVarDecl(ShGrammarParser.VarDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#varDecl}.
	 * @param ctx the parse tree
	 */
	void exitVarDecl(ShGrammarParser.VarDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void enterExprStmt(ShGrammarParser.ExprStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#exprStmt}.
	 * @param ctx the parse tree
	 */
	void exitExprStmt(ShGrammarParser.ExprStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(ShGrammarParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(ShGrammarParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ShGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(ShGrammarParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ShGrammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(ShGrammarParser.ExprContext ctx);
}