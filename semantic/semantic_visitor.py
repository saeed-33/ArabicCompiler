from ast_tree.visitor_interface import ASTVisitor
from semantic.environment import Environment, SemanticError
from semantic.symbols import VariableSymbol

class SemanticVisitor(ASTVisitor):
    def __init__(self):
        # تهيئة البيئة العامة (Global Scope) كأول نطاق تبدأ منه العملية
        self.current_env = Environment()
        # قائمة ديناميكية لتجميع الأخطاء الدلالية المكتشفة أثناء عبور الشجرة
        self.errors = []

    def log_error(self, line: int, column: int, message: str):
        """ دالة مساعدة لصياغة الأخطاء بتنسيق هندسي موحد وسهل القراءة """
        self.errors.append(f"خطأ دلالي (سطر {line}، عمود {column}): {message}")

    def visit_ProgramNode(self, node):
        """ نقطة الانطلاق: عبور جميع الجمل الأساسية في البرنامج """
        for stmt in node.statements:
            if stmt is not None:  # التحصين: تخطي أي عقدة فارغة أو غير مبنية
                stmt.accept(self)

    def visit_BlockNode(self, node):
        """ إدارة النطاقات المعجمية للكتل البرمجية """
        # 1. الاحتفاظ بمؤشر البيئة الحالية (النطاق الأب الخارجي)
        previous_env = self.current_env
        
        # 2. الغوص للأسفل عبر إنشاء بيئة جديدة وتمرير البيئة السابقة كأب لها
        self.current_env = Environment(enclosing=previous_env)
        
        # 3. زيارة وتحليل جميع الجمل البرمجية الواقعة داخل هذا النطاق الجديد
        for stmt in node.statements:
            if stmt is not None:  # التحصين: حماية الكتل البرمجية أيضاً
                stmt.accept(self)
            
        # 4. الصعود للأعلى واستعادة البيئة السابقة
        self.current_env = previous_env

    def visit_VarDeclNode(self, node):
        """ تسجيل المتغيرات وفحص التكرار """
        # أولاً: تقييم التعبير البرمجي المصاحب للإعلان إن وجد
        if node.expr:
            node.expr.accept(self)
            
        # ثانياً: إنشاء كائن الرمز باستخدام المسميات المطابقة لعقدتك (variable_name و variable_type)
        symbol = VariableSymbol(name=node.variable_name, sym_type=node.variable_type)
        
        # ثالثاً: محاولة تسجيل المتغير في النطاق الحالي واصطياد أخطاء التكرار
        try:
            self.current_env.define(node.variable_name, symbol)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    def visit_AssignNode(self, node):
        """ التحقق من صحة عملية التعيين وتحديث قيم المتغيرات """
        # 1. تقييم الطرف الأيمن من المعادلة
        if node.expr:
            node.expr.accept(self)
            
        # 2. التأكد من أن المتغير المراد تعديله موجود ومُعلن عنه باستخدام (variable_name)
        try:
            self.current_env.resolve(node.variable_name)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    def visit_IdNode(self, node):
        """ التحقق من وجود المتغير في الذاكرة عند استدعاء اسمه """
        try:
            self.current_env.resolve(node.name)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    def visit_PrintNode(self, node):
        if node.expr:
            node.expr.accept(self)

    def visit_IfNode(self, node):
        if node.condition:
            node.condition.accept(self)
        if node.then_block:
            node.then_block.accept(self)
        if node.else_block:
            node.else_block.accept(self)

    def visit_WhileNode(self, node):
        if node.condition:
            node.condition.accept(self)
        if node.body:
            node.body.accept(self)

    def visit_BinOpNode(self, node):
        if node.left:
            node.left.accept(self)
        if node.right:
            node.right.accept(self)

    def visit_NumberNode(self, node):
        # الأرقام الثابتة لا تحتاج لتحليل النطاقات
        pass