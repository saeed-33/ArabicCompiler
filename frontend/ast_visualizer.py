# frontend/ast_visualizer.py
import graphviz 
from ast_tree.visitor_interface import ASTVisitor

class ASTVisualizerVisitor(ASTVisitor):
    def __init__(self):
        # إنشاء كائن الرسم البياني الموجه (Directed Graph)
        self.dot = graphviz.Digraph(comment='Arabic Compiler AST', format='png')
        # تصميم شكل العقد (صناديق زرقاء بحواف دائرية)
        self.dot.attr('node', shape='box', style='rounded, filled', 
                      fillcolor='lightblue', fontname='Arial')

    def render(self, output_filename='ast_output'):
        # حفظ الصورة وعرضها تلقائياً للمستخدم
        self.dot.render(output_filename, view=True)

    def add_node_and_edge(self, parent_node, child_node, edge_label=""):
        if child_node is not None:
            child_node.accept(self)  # استدعاء الزائر للابن ليرسم نفسه
            # رسم سهم يربط بين الأب والابن باستخدام المعرف الفريد id() لكل كائن
            self.dot.edge(str(id(parent_node)), str(id(child_node)), label=edge_label)

    # --- تطبيق دوال الزيارة لكل عقدة بناءً على معماريتك المحددة ---
    
    def visit_ProgramNode(self, node):
        self.dot.node(str(id(node)), "Program")
        for stmt in node.statements:
            if stmt is not None:
                self.add_node_and_edge(node, stmt)

    def visit_VarDeclNode(self, node):
        label = f"VarDecl\n{node.variable_name} : {node.variable_type}"
        self.dot.node(str(id(node)), label, fillcolor='lightgreen')
        self.add_node_and_edge(node, node.expr, "expr")

    def visit_AssignNode(self, node):
        label = f"Assign\n{node.variable_name}"
        self.dot.node(str(id(node)), label, fillcolor='lightgreen')
        self.add_node_and_edge(node, node.expr, "expr")

    def visit_BinOpNode(self, node):
        self.dot.node(str(id(node)), f"BinOp\n'{node.op}'", fillcolor='lightyellow')
        self.add_node_and_edge(node, node.left, "left")
        self.add_node_and_edge(node, node.right, "right")

    def visit_NumberNode(self, node):
        self.dot.node(str(id(node)), f"Number\n{node.value}", fillcolor='white')

    def visit_IdNode(self, node):
        self.dot.node(str(id(node)), f"ID\n{node.name}", fillcolor='white')

    def visit_IfNode(self, node):
        self.dot.node(str(id(node)), "If", fillcolor='orange')
        self.add_node_and_edge(node, node.condition, "condition")
        self.add_node_and_edge(node, node.then_block, "then")
        if node.else_block:
            self.add_node_and_edge(node, node.else_block, "else")

    def visit_WhileNode(self, node):
        self.dot.node(str(id(node)), "While", fillcolor='orange')
        self.add_node_and_edge(node, node.condition, "condition")
        self.add_node_and_edge(node, node.body, "body")

    def visit_BlockNode(self, node):
        self.dot.node(str(id(node)), "Block")
        for stmt in node.statements:
            if stmt is not None:
                self.add_node_and_edge(node, stmt)

    def visit_PrintNode(self, node):
        self.dot.node(str(id(node)), "Print", fillcolor='pink')
        self.add_node_and_edge(node, node.value, "value")