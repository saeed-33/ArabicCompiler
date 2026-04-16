from ai_ast_nodes import *

# سنقوم بمحاكاة بناء عقدة شرطية برمجيا للتأكد من صحة الفئات
dummy_condition = BinOpNode(left=None, op=">", right=None)
dummy_then = BlockNode(statements=[])

# تجربة إنشاء عقدة "إذا" بدون "وإلا"
if_node = IfNode (condition=dummy_condition, then_block=dummy_then, else_block=None)

print("تم إنشاء عقدة الذكاء الصناعي بنجاح")
print(if_node)