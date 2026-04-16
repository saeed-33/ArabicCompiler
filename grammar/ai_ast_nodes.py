from dataclasses import dataclass
from typing import List, Optional
from abc import ABC, abstractmethod

from custom_visitor import CustomASTVisitor

# --- Base AST Node ---

@dataclass
class ASTNode(ABC):
    line: int = 0
    column: int = 0
    
    @abstractmethod
    def accept(self, visitor: 'CustomASTVisitor'): 
        pass

# --- Semantic AST Nodes --
@dataclass(kw_only=True)
class BinOpNode (ASTNode):
    left: ASTNode
    op: str
    right: ASTNode
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_BinOpNode(self)
    
@dataclass(kw_only=True)
class BlockNode(ASTNode):
    statements: List[ASTNode]
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_BlockNode(self)

@dataclass(kw_only=True)
class VarDeclNode(ASTNode):
    variable_name: str
    variable_type: str
    expr: ASTNode
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_VarDeclNode(self)

@dataclass(kw_only=True)
class AssignNode(ASTNode):
    variable_name: str
    expr: ASTNode
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_AssignNode(self)

@dataclass(kw_only=True)
class PrintNode(ASTNode):
    expr: ASTNode
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_PrintNode(self)

@dataclass(kw_only=True)
class IfNode(ASTNode):
    condition: ASTNode
    then_block: BlockNode
    else_block: Optional[BlockNode] = None
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_IfNode(self)

@dataclass(kw_only=True)
class WhileNode(ASTNode):
    condition: ASTNode
    body: BlockNode
    
    def accept(self, visitor: 'CustomASTVisitor'):
        return visitor.visit_WhileNode(self)