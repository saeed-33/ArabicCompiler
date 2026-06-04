from ast_tree.nodes import *
from semantic.environment import Environment, SemanticError
from semantic.symbols import VariableSymbol
from semantic.types_system import *

class SemanticAnalyzerVisitor:
    def __init__(self):
        # تهيئة البيئة العامة
        self.current_env = Environment()
        # قائمة لتجميع الأخطاء بدلاً من إيقاف المترجم
        self.errors = []

    def log_error(self, line: int, column: int, message: str):
        self.errors.append(f"(خطأ داللي) سطر {line}: {message}")

    # 1. زيارة البرنامج
    def visit_ProgramNode(self, node: ProgramNode):
        for stmt in node.statements:
            if stmt is not None:  # التحقق من أن العقدة ليست فارغة
                stmt.accept(self)

    # 2. زيارة الكتل البرمجية (الأقواس المعقوفة)
    def visit_BlockNode(self, node: BlockNode):
        # الدخول في نطاق جديد (Scope)
        previous_env = self.current_env
        self.current_env = Environment(enclosing=previous_env)
        
        for stmt in node.statements:
            if stmt is not None:  # التحقق من أن العقدة ليست فارغة
                stmt.accept(self)
        
        # الخروج من النطاق وتدمير المتغيرات المحلية
        self.current_env = previous_env

    # زيارة جملة الإسناد (مثل: س = س + ٥)
    def visit_AssignNode(self, node: AssignNode):
        # 1. تقييم الطرف الأيمن (القيمة المسندة)
        value_type = node.expr.accept(self)
        
        # 2. تحديد اسم المتغير المستهدف بالاعتماد على خصائص العقدة
        var_name = node.variable_name
        
        # 3. التحقق من وجود المتغير في البيئة (جدول الرموز)
        try:
            sym = self.current_env.resolve(var_name)
            declared_type = sym.type
            
            # 4. التحقق من توافق نوع القيمة المسندة مع النوع المعرّف للمتغير
            if value_type != ERROR_TYPE and value_type != declared_type:
                self.log_error(
                    node.line, 
                    node.column, 
                    f"لا يمكن إسناد قيمة من نوع '{value_type}' إلى متغير من نوع '{declared_type}'."
                )
                return ERROR_TYPE
                
            return declared_type
            
        except SemanticError as e:
            self.log_error(node.line, node.column, f"محاولة إسناد قيمة لمتغير غير معرّف '{var_name}'.")
            return ERROR_TYPE
    
    # 3. زيارة إعلان المتغير
    def visit_VarDeclNode(self, node: VarDeclNode):
        # تقييم القيمة الابتدائية أولاً
        value_type = node.expr.accept(self)

        # تحويل الاسم النصي للنوع إلى كائن Type (تبسيط للمعمل)
        declared_type = INT_TYPE if node.variable_type == 'صحيح' else STRING_TYPE

        # التحقق من توافق الأنواع
        if value_type != ERROR_TYPE and value_type != declared_type:
            self.log_error(
                node.line, 
                node.column, 
                f"لا يمكن إسناد قيمة من نوع '{value_type}' إلى متغير من نوع '{declared_type}'."
            )

        # حفظ المتغير في البيئة
        try:
            sym = VariableSymbol(node.variable_name, declared_type)
            self.current_env.define(node.variable_name, sym)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    # 4. زيارة الأرقام (الأوراق)
    def visit_NumberNode(self, node: NumberNode):
        # نرجع النوع صحيح دائماً في هذا التبسيط
        return INT_TYPE

    # 5. زيارة استخدام المتغير
    def visit_IdNode(self, node: IdNode):
        try:
            sym = self.current_env.resolve(node.name)
            return sym.type  # إرجاع النوع الأصلي للمتغير
        except SemanticError as e:
            self.log_error(node.line, node.column, f"استخدام لمتغير غير معرّف '{node.name}'.")
            return ERROR_TYPE  # تسميم العقدة لمنع أخطاء إضافية

    # 6. زيارة العمليات الثنائية (الرياضيات)
    def visit_BinOpNode(self, node: BinOpNode):
        left_type = node.left.accept(self)
        right_type = node.right.accept(self)

        # التقييم القصير للأخطاء (Poisoning)
        if left_type == ERROR_TYPE or right_type == ERROR_TYPE:
            return ERROR_TYPE

        # التحقق من قوانين الرياضيات
        if node.op in ['+', '-', '*', '/']:
            if left_type == INT_TYPE and right_type == INT_TYPE:
                return INT_TYPE
            else:
                self.log_error(
                    node.line, 
                    node.column, 
                    f"العملية '{node.op}' غير مسموحة بين '{left_type}' و '{right_type}'."
                )
                return ERROR_TYPE
            
    def visit_PrintNode(self, node : PrintNode):
        
        # تقييم التعبير الممرر لجملة الطباعة
        node.expr.accept(self)
        

        return ERROR_TYPE