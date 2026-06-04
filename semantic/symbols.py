from dataclasses import dataclass
from typing import Any

# الفئة الأساسية لأي كيان يتم تعريفه في الكود
class Symbol:
    def __init__(self, name: str, sym_type: Any = None):
        self.name = name
        self.type = sym_type # نوع البيانات (صحيح، نص، عشري، إلخ) [cite: 338]

    def __repr__(self):
        return f"<{self.__class__.__name__} name='{self.name}' type='{self.type}'>"

# فئة متخصصة للمتغيرات العادية [cite: 344]
class VariableSymbol(Symbol):
    def __init__(self, name: str, sym_type: Any = None):
        super().__init__(name, sym_type)

# فئة متخصصة للدوال (سنحتاجها في المراحل المتقدمة) [cite: 350]
class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: Any = None, arity: int = 0):
        super().__init__(name, return_type)
        self.arity = arity # عدد المعاملات التي تقبلها الدالة [cite: 355]