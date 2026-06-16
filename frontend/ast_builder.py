from frontend.ShGrammarVisitor import ShGrammarVisitor
from frontend.ShGrammarParser import ShGrammarParser
from ast_tree.nodes import *

class ASTBuilderVisitor(ShGrammarVisitor):
    
    # دالة مساعدة لنسخ البيانات الوصفية (رقم السطر والعمود)
    def set_metadata(self, node: ASTNode, ctx):
        node.line = ctx.start.line
        node.column = ctx.start.column
        return node

    def visitProgram(self, ctx: ShGrammarParser.ProgramContext):
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        node = ProgramNode(statements=statements)
        return self.set_metadata(node, ctx)

    def visitStatement(self, ctx: ShGrammarParser.StatementContext):
        # توجيه الزيارة حسب نوع الجملة
        if ctx.varDecl(): return self.visit(ctx.varDecl())
        elif ctx.ifStmt(): return self.visit(ctx.ifStmt())
        elif ctx.whileStmt(): return self.visit(ctx.whileStmt())
        elif ctx.assignStmt(): return self.visit(ctx.assignStmt())
        # إذا كان لديك جملة طباعة بالملف الأساسي يمكنك إلغاء تعليق السطر التالي:
        elif ctx.printStmt(): return self.visit(ctx.printStmt())
        elif ctx.breakStmt(): return self.visit(ctx.breakStmt())
        elif ctx.continueStmt(): return self.visit(ctx.continueStmt())

    def visitVarDecl(self, ctx: ShGrammarParser.VarDeclContext):
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()
        value_node = self.visit(ctx.expr())
        
        node = VarDeclNode(variable_name=name, variable_type=var_type, expr=value_node)
        return self.set_metadata(node, ctx)

    def visitIfStmt(self, ctx: ShGrammarParser.IfStmtContext):
        condition = self.visit(ctx.expr())
        then_block = self.visit(ctx.block(0))
        else_block = None
        
        if ctx.block(1):
            else_block = self.visit(ctx.block(1))
            
        node = IfNode(condition=condition, then_block=then_block, else_block=else_block)
        return self.set_metadata(node, ctx)

    def visitWhileStmt(self, ctx: ShGrammarParser.WhileStmtContext):
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.block())
        node = WhileNode(condition=condition, body=body)
        return self.set_metadata(node, ctx)

    def visitBlock(self, ctx: ShGrammarParser.BlockContext):
        statements = [self.visit(stmt) for stmt in ctx.statement()]
        node = BlockNode(statements=statements)
        return self.set_metadata(node, ctx)
    
    def visitAssignStmt(self, ctx: ShGrammarParser.AssignStmtContext):
        name = ctx.ID().getText()
        value_node = self.visit(ctx.expr())
        
        node = AssignNode(variable_name=name, expr=value_node)
        return self.set_metadata(node, ctx)
    
    def visitExpr(self, ctx: ShGrammarParser.ExprContext):
        # حالة 1: العمليات الثنائية (مثل: س + 5)
        if ctx.getChildCount() == 3 and len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expr(1))
            
            node = BinOpNode(left=left, op=op, right=right)
            return self.set_metadata(node, ctx)
            
        # حالة 2: القيم الرقمية المباشرة (Literal Numbers)
        elif ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
            node = NumberNode(value=value)
            return self.set_metadata(node, ctx)
            
        # حالة 3: استدعاء متغير داخل التعبير (مثل استخدام 'س' داخل معادلة)
        elif ctx.ID():
            name = ctx.ID().getText()
            node = IdNode(name=name)  # تم تعديلها هنا إلى IdNode الصحيحة والمكتملة
            return self.set_metadata(node, ctx)
            
        # حالة 4: التعامل مع الأقواس لضمان أولوية العمليات ( تعبير )
        elif ctx.expr(0):
            return self.visit(ctx.expr(0))
        
    def visitPrintStmt(self, ctx: ShGrammarParser.PrintStmtContext):
        value_node = self.visit(ctx.expr())
        return PrintNode (expr=value_node)
    def visitBreakStmt(self, ctx:ShGrammarParser.BreakStmtContext):
        return BreakNode(line=ctx.start.line, column=ctx.start.column)
    def visitContinueStmt(self, ctx:ShGrammarParser.ContinueStmtContext):
        return ContinueNode(line=ctx.start.line, column=ctx.start.column)