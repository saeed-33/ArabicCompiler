// Generated from ShGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ShGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ShGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(ShGrammarParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(ShGrammarParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(ShGrammarParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#varDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarDecl(ShGrammarParser.VarDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#assignStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignStmt(ShGrammarParser.AssignStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#printStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrintStmt(ShGrammarParser.PrintStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#ifStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStmt(ShGrammarParser.IfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#whileStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileStmt(ShGrammarParser.WhileStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#exprStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprStmt(ShGrammarParser.ExprStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(ShGrammarParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link ShGrammarParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(ShGrammarParser.ExprContext ctx);
}