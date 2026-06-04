# الفئة الأساسية لأي نوع بيانات
class Type:
    def __eq__(self, other):
        # نوعان متطابقان إذا كانا من نفس الفئة (Nominal تطابق اسمي)
        return isinstance(other, self.__class__)

class IntType(Type):
    def __str__(self): return "صحيح"

class FloatType(Type):
    def __str__(self): return "عشري"

class StringType(Type):
    def __str__(self): return "نص"

class BoolType(Type):
    def __str__(self): return "منطقي"

class ErrorType(Type):
    """النوع المسموم: يُستخدم عند وجود خطأ لمنع تكرار رسائل الخطأ"""
    def __str__(self): return "داللي_خطأ"

# ثوابت عامة لتوفير الذاكرة، سنستخدمها في كل المترجم (Singletons)
INT_TYPE = IntType()
FLOAT_TYPE = FloatType()
STRING_TYPE = StringType()
BOOL_TYPE = BoolType()
ERROR_TYPE = ErrorType()