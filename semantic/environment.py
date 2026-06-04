from semantic.symbols import Symbol

class SemanticError(Exception):
    """ استثناء مخصص لأخطاء التحليل الدلالي """ 
    pass

class Environment:
    def __init__(self, enclosing: 'Environment' = None):
        # القاموس الداخلي لتخزين الرموز في هذا النطاق فقط (Hash Table) [cite: 369]
        self._values = {}
        # مؤشر يشير إلى النطاق الأب الخارجي [cite: 371]
        self.enclosing = enclosing

    def define(self, name: str, symbol: Symbol):
        """ تعريف متغير جديد في النطاق الحالي ويمنع التكرار في نفس النطاق """ 
        if name in self._values:
            raise SemanticError(f"خطأ دلالي: المتغير '{name}' معرف مسبقاً في هذا النطاق.") 
        self._values[name] = symbol

    def resolve(self, name: str) -> Symbol:
        """ البحث عن متغير؛ تبدأ من النطاق الحالي وتصعد للأجداد إذا لزم الأمر """ 
        # 1. هل المتغير موجود في النطاق الحالي؟ [cite: 383]
        if name in self._values:
            return self._values[name]
        
        # 2. إذا لم أجده، هل هناك نطاق أب (خارجي) لأسأله؟ [cite: 387]
        if self.enclosing is not None:
            return self.enclosing.resolve(name)
        
        # 3. إذا وصلنا للقمة (النطاق العام) ولم نجده، إذن المتغير غير معرف! [cite: 390]
        raise SemanticError(f"خطأ دلالي: استخدام المتغير غير المعرف '{name}'.") 

    def print_stack(self, level=0):
        """ دالة مساعدة لطباعة محتوى الذاكرة للـ Debugging """ 
        print(f"{'  ' * level}Scope Level {level}: {list(self._values.keys())}") 
        if self.enclosing:
            self.enclosing.print_stack(level + 1) 