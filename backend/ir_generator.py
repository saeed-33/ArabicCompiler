import llvmlite.ir as ir
from ast_tree.nodes import *
from ast_tree.visitor_interface import ASTVisitor

class IRGeneratorVisitor(ASTVisitor):
    def __init__(self):
        # 1. إنشاء الوحدة (Module): الحاوية الكبرى التي تمثل الملف بأكمله
        self.module = ir.Module(name="arabic_compiler_module")
        
        # 2. إعداد دالة نقطة الإدخال (Main Function)
        func_type = ir.FunctionType(ir.IntType(32), [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        
        # 3. إنشاء الكتلة الأساسية (Basic Block) داخل الدالة
        entry_block = self.main_func.append_basic_block(name="entry")
        
        # 4. إعداد قلم الكتابة (IRBuilder)
        self.builder = ir.IRBuilder(entry_block)
        
        # 5. قاموس جديد لربط اسم المتغير بمؤشره في الذاكرة (Pointer)
        self.symbol_table = {}

    def finish_generation(self):
        """تضيف أمر الإرجاع (ret) بقيمة 0 لإعلام نظام التشغيل بنجاح التنفيذ."""
        self.builder.ret(ir.Constant(ir.IntType(32), 0))
        return str(self.module)

    def generate(self, node):
        """دالة مساعدة لزيارة الشجرة بالكامل وإنهاء عملية توليد الكود."""
        self.visit(node)
        return self.finish_generation()

    def visit(self, node: ASTNode):
        """دالة عامة للمرور على أي عقدة واستدعاء الزائر المناسب لها."""
        if node:
            return node.accept(self)

    # 1. زيارة البرنامج (جذر الشجرة)
    def visit_ProgramNode(self, node: ProgramNode):
        for stmt in node.statements:
            self.visit(stmt)

    # 2. ترجمة إعلان المتغير (حجز الذاكرة والتخزين الابتدائي)
    def visit_VarDeclNode(self, node: VarDeclNode):
        # تحديد نوع البيانات في LLVM (صحيح 32-بت للتبسيط)
        var_type = ir.IntType(32)
        
        # حجز مساحة في مكدس الذاكرة (Stack) باستخدام alloca (يرجع مؤشراً)
        ptr = self.builder.alloca(var_type, name=node.variable_name)
        
        # تسجيل هذا المؤشر في جدول الرموز للوصول إليه لاحقاً
        self.symbol_table[node.variable_name] = ptr
        
        # حساب القيمة الابتدائية بزيارة الابن وتخزينها بالذاكرة
        if node.expr:
            init_val = self.visit(node.expr)
            self.builder.store(init_val, ptr)

    # 3. استدعاء المتغيرات وقراءتها (تحميل القيمة من الذاكرة)
    def visit_IdNode(self, node: IdNode):
        # البحث عن عنوان المتغير في الذاكرة
        ptr = self.symbol_table.get(node.name)
        if ptr is None:
            raise Exception(f"خطأ هندسي: المتغير '{node.name}' غير موجود في الذاكرة.")
        
        # تحميل القيمة من الذاكرة إلى مسجل وهمي جديد متبوعاً بـ _val
        return self.builder.load(ptr, name=node.name + "_val")

    # 4. تحديث قيم المتغيرات (تخزين القيمة الجديدة)
    def visit_AssignNode(self, node: AssignNode):
        # حساب القيمة الجديدة في الجانب الأيمن
        value_val = self.visit(node.expr)
        
        # إحضار مؤشر الذاكرة القديم للمتغير من الجانب الأيسر
        ptr = self.symbol_table.get(node.variable_name)
        if ptr is None:
            raise Exception(f"خطأ هندسي: محاولة إسناد لمتغير غير مسجل '{node.name}'.")
        
        # تخزين القيمة الجديدة في نفس العنوان
        self.builder.store(value_val, ptr)

    # 5. ترجمة الأرقام الثابتة
    def visit_NumberNode(self, node: NumberNode):
        int_type = ir.IntType(32)
        return ir.Constant(int_type, int(node.value))

    # 6. ترجمة العمليات الثنائية
    def visit_BinOpNode(self, node: BinOpNode):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        
        if left_val is None or right_val is None:
            raise Exception("خطأ أثناء توليد الكود: أحد أطراف العملية الحسابية مفقود.")

        if node.op == '+':
            return self.builder.add(left_val, right_val, name="addtmp")
        elif node.op == '-':
            return self.builder.sub(left_val, right_val, name="subtmp")
        elif node.op == '*':
            return self.builder.mul(left_val, right_val, name="multmp")
        elif node.op == '/':
            return self.builder.sdiv(left_val, right_val, name="divtmp")
        elif node.op == '<':
            return self.builder.icmp_signed('<',left_val,right_val, name="Lttemp")
        elif node.op == '>':
            return self.builder.icmp_signed('>',left_val,right_val, name="Gttemp")
        else:
            raise NotImplementedError(f"العملية الرياضية '{node.op}' غير مدعومة حالياً.")

    # ---------------------------------------------------------
    # باقي الدوال ستظل فارغة للأيام القادمة
    # ---------------------------------------------------------
    def visit_PrintNode(self, node:IfNode): pass
    
    def visit_IfNode(self, node): 
        cond_val = self.visit(node.condition)
        current_function = self.builder.function
        then_bb = current_function.append_basic_block("then")
        merge_bb = current_function.append_basic_block("ifcont")
        self.builder.cbranch(cond_val,then_bb,merge_bb)
        self.builder.position_at_end(then_bb)
        self.visit(node.then_block)
        self.builder.branch(merge_bb)
        
        self.builder.position_at_end(merge_bb)
        return None
    def visit_WhileNode(self, node): pass
    def visit_BlockNode(self, node): pass