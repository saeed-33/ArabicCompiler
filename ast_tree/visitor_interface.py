# ast/visitor_interface.py
from abc import ABC, abstractmethod

class ASTVisitor(ABC):
    """
    الواجهة البرمجية الأساسية لأي زائر سيعبر شجرة الـ AST.
    """
    @abstractmethod
    def visit_ProgramNode(self, node): pass

    @abstractmethod
    def visit_VarDeclNode(self, node): pass

    @abstractmethod
    def visit_AssignNode(self, node): pass

    @abstractmethod
    def visit_IfNode(self, node): pass

    @abstractmethod
    def visit_WhileNode(self, node): pass

    @abstractmethod
    def visit_BlockNode(self, node): pass

    @abstractmethod
    def visit_BinOpNode(self, node): pass

    @abstractmethod
    def visit_NumberNode(self, node): pass

    @abstractmethod
    def visit_IdNode(self, node): pass

    @abstractmethod
    def visit_PrintNode(self, node): pass

    @abstractmethod
    def visit_StringNode(self, node): pass