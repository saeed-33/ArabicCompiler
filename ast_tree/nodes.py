from dataclasses import dataclass
from typing import List, Optional
from abc import ABC, abstractmethod

# --- Base AST Node ---

@dataclass
class ASTNode(ABC):
    line: int = 0
    column: int = 0
    
    @abstractmethod
    def accept(self, visitor): 
        pass

@dataclass(kw_only=True)
class ProgramNode(ASTNode):
    statements: List[ASTNode]
    
    def accept(self, visitor):
        return visitor.visit_ProgramNode(self)

# --- Semantic AST Nodes --

@dataclass(kw_only=True)
class BinOpNode(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_BinOpNode(self)
        
@dataclass(kw_only=True)
class BlockNode(ASTNode):
    statements: List[ASTNode]
    
    def accept(self, visitor):
        return visitor.visit_BlockNode(self)

@dataclass(kw_only=True)
class VarDeclNode(ASTNode):
    variable_name: str
    variable_type: str
    expr: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_VarDeclNode(self)

@dataclass(kw_only=True)
class AssignNode(ASTNode):
    variable_name: str
    expr: ASTNode
    
    def accept(self, visitor):
        return visitor.visit_AssignNode(self)

@dataclass(kw_only=True)
class PrintNode(ASTNode):
    text: str
    
    def accept(self, visitor):
        return visitor.visit_PrintNode(self)

@dataclass(kw_only=True)
class IfNode(ASTNode):
    condition: ASTNode
    then_block: BlockNode
    else_block: Optional[BlockNode] = None
    
    def accept(self, visitor):
        return visitor.visit_IfNode(self)

@dataclass(kw_only=True)
class WhileNode(ASTNode):
    condition: ASTNode
    body: BlockNode
    
    def accept(self, visitor):
        return visitor.visit_WhileNode(self)
        
@dataclass(kw_only=True)
class NumberNode(ASTNode):
    value: float
    
    def accept(self, visitor):
        return visitor.visit_NumberNode(self)
       
@dataclass(kw_only=True)
class StringNode(ASTNode):
    value: str
    
    def accept(self, visitor):
        return visitor.visit_NumberNode(self)
    

@dataclass(kw_only=True)
class IdNode(ASTNode):
    name: str
    
    def accept(self, visitor):
        return visitor.visit_IdNode(self)


@dataclass(kw_only=True)
class BreakNode(ASTNode):
    def accept(self, visitor):
        return visitor.visit_BreakNode(self)

@dataclass(kw_only=True)
class ContinueNode(ASTNode):
    def accept(self, visitor):
        return visitor.visit_ContinueNode(self)