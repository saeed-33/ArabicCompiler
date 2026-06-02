from dataclasses import dataclass
from typing import List, Optional

# الفئة الأم التي ترث منها كل العقد
class ASTNode:
    pass

# عقدة تمثل الرقم الثابت
@dataclass
class NumberNode (ASTNode):
    value: float

# عقدة تمثل اسم المتغير عند استخدامه في معادلة
@dataclass
class IdNode (ASTNode):
    name: str

# عقدة تمثل عملية حسابية ثنائية (جمع)، طرح، ضرب قسمة)
@dataclass
class BinOpNode (ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

# عقدة تمثل إعلان متغير جديد
@dataclass
class VarDeclNode (ASTNode):
    name: str
    var_type: str
    value: ASTNode

# العقدة الجذرية التي تمثل البرنامج كاملاً تحتوي على قائمة من الجمل)
@dataclass
class ProgramNode (ASTNode):
    statements: List [ASTNode]


# الفئات السابقة (NumberNode, IdNode, BinOpNode, VarDeclNode, ProgramNode) تبقى كما هي

@dataclass
class AssignNode (ASTNode):
    name: str
    value: ASTNode

@dataclass
class PrintNode (ASTNode):
    value: ASTNode

@dataclass
class BlockNode (ASTNode):
    statements: List [ASTNode]

@dataclass
class IfNode (ASTNode):
    condition: ASTNode
    then_block: BlockNode
    else_block: Optional [BlockNode]  # قد تكون None إذا لم يكتب المبرمج "وإلا"

@dataclass
class WhileNode (ASTNode):
    condition: ASTNode
    body: BlockNode