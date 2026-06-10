from platform import node

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

        self.loop_stack = []
        # 1. تعريف نوع مؤشر البايتات للنصوص (i8) #
        self.byte_ptr_type = ir.IntType(8).as_pointer()
        
        # 2. إعلان توقيع دالة printf الخارجية: تقبل مؤشر نص وعدد متغير من المعاملات var_arg=True( #
        printf_type = ir.FunctionType (ir.IntType (32), [self.byte_ptr_type], var_arg=True)
        self.printf_func = ir.Function(self.module, printf_type, name="printf")
        
        # 3. عداد لتسمية الثوابت النصية العالمية بشكل فريد #
        self.string_counter = 0

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
    
    def visit_IfNode (self, node):
        cond_val = self.visit(node.condition)
        if cond_val is None:
        # 10 # التقييم العميق حساب قيمة الشرط (11) يجب أن ينتج قيمة منطقية)
            raise Exception (". خطأ هندسي تعذر حساب قيمة الشرط لجملة (إذا)")
    # 20 # الحصول على الدالة الحالية التي تكتب بداخلها
        current_func = self.builder.function
    # 3 # حجز الكتل الأساسية في الذاكرة (Basic Blocks)
        then_bb = current_func.append_basic_block("then")
        merge_bb = current_func.append_basic_block("merge")
    # التحقق مما إذا كان هناك مسار (وإلا) #
        if node.else_block:
            else_bb = current_func.append_basic_block("else")
        # وإلا اذهب لـ else قفزة مشروطة : إذا صح اذهب لـ then #
            self.builder.cbranch(cond_val, then_bb, else_bb) 
        else: 
        # مباشرة merge وإلا تخطى واذهب لـ then قفزة مشروطة : إذا صح اذهب لـ # 
            self.builder.cbranch (cond_val, then_bb, merge_bb) 
    # (then) نقل القلم وبناء كتلة التحقق .4 # 
        self.builder.position_at_end(then_bb) 
        self.visit(node.then_block) # زيارة محتوى جملة إذا 
    # برمجة دفاعية: لا نقفز للالتحام إلا إذا كانت الستلة غير مختومة مسبقاً بقانون المنهي # 
        if not self.builder.block.is_terminated: 
            self.builder.branch (merge_bb) 
    # إن وجدت (else) نقل القلم وبناء كتلة النفي 5 # 
        if node.else_block: 
            self.builder.position_at_end(else_bb) 
            self.visit(node.else_block) 
        # برمجة دفاعية للمسار الثاني # 
            if not self.builder.block.is_terminated: 
                self.builder.branch (merge_bb) 
    # استئناف البرنامج: وضع القلم في كتلة الالتحام ليكتب الكود القادم فيها 60 # 
        self.builder.position_at_end (merge_bb)
    def visit_WhileNode (self, node:WhileNode):
        current_func = self.builder.function
    # 1. حجز الكتل الثلاث في الذاكرة #
        cond_bb = current_func.append_basic_block("while_cond")
        body_bb = current_func.append_basic_block("while_body")
        end_bb = current_func.append_basic_block("while_end")
    # 2. القفز من الكتلة الحالية للدخول إلى رأس الحلقة #
        self.builder.branch (cond_bb)
    # 3. برمجة كتلة الشرط #
        self.builder.position_at_end (cond_bb)
        cond_val = self.visit(node.condition)
        if cond_val is None:
            raise Exception (". خطأ هندسي تعذر تقييم شرط الحلقة" )
    # قفزة مشروطة: إذا صح استمر للمحتوى، وإلا اخرج للنهاية #
        self.builder.cbranch (cond_val, body_bb, end_bb)
    # 4. برمجة كتلة المحتوى (مع إدارة المكدس) #
        self.builder.position_at_end (body_bb)
    # دفع معلومات الحلقة الحالية للمكدس قبل زيارة المحتوى #
        self.loop_stack.append((cond_bb, end_bb))
        self.visit(node.body) # زيارة كل الأوامر داخل الحلقة
    # سحب معلومات الحلقة بعد الانتهاء #
        self.loop_stack.pop()
    # 5. العودة لتقييم الشرط مجدداً : (Back-Edge) الحافة الخلفية #
        if not self.builder.block.is_terminated:
           self.builder.branch (cond_bb)
    # 6. استئناف البرنامج خارج الحلقة #
        self.builder.position_at_end (end_bb)
    def visit_BlockNode(self, node): pass
    def visit_BreakNode (self, node):
        if not self.loop_stack:
            raise Exception (". خطأ نحوي تم استخدام أمر اكسر خارج حلقة تكرار")
    # استخراج كتلة النهاية للحلقة الأعمق والنشطة حالياً #
        _, end_bb = self.loop_stack[-1]
        self.builder.branch (end_bb)

    def visit_ContinueNode (self, node):
        if not self.loop_stack:
            raise Exception (". خطأ نحوي تم استخدام أمر تجاوز خارج حلقة تكرار")
    # استخراج كتلة الشرط للحلقة الأعمق والنشطة حالياً #
        cond_bb, _ = self.loop_stack[-1]
        self.builder.branch (cond_bb)
    def create_global_string (self, string_text: str):
    # 1. إضافة سطر جديد وإنهاء النص بالصفر (C-style string) #
        string_text = string_text + '\n\0'
    # 2. تحويل النص العربي إلى بايتات مشفرة بـ UTF-8 #
        encoded_bytes = bytearray (string_text.encode('utf-8'))
    # 3. تحديد نوع المصفوفة [i8 x عدد البايثات] #
        array_type = ir.ArrayType (ir.IntType (8), len (encoded_bytes))
    # 4. إنشاء الثابت في النطاق العالمي (Global Variable) #
        global_name = f".str_{self.string_counter}"
        self.string_counter += 1
        global_str = ir.GlobalVariable (self.module, array_type, name=global_name)
        global_str.linkage = 'private'
        global_str.global_constant = True
        global_str.initializer = ir.Constant (array_type, encoded_bytes)
        return global_str
    def visit_PrintStringNode (self, node):
    # 1. إنشاء النص كـ ثابت عالمي في الذاكرة #
        global_str = self.create_global_string (node.text)
    # 2. استخدام تعليمة GEP (GetElementPtr) للوصول للعنصر رقم 0 في المصفوفة #
    # نمرر صفرين: الأول للدخول داخل المؤشر، والثاني لاختيار الحرف الأول #
        zero = ir.Constant(ir.IntType (32), 0)
        str_ptr = self.builder.gep(global_str, [zero, zero], inbounds=True, name="str_ptr")
    # 3. استدعاء دالة printf وتمرير المؤشر إليها #
        self.builder.call(self.printf_func, [str_ptr], name="print_call")
    def visit_StringNode(self, node):
    # إزالة علامات التنصيص الزائدة من أطراف النص إن وجدت
        clean_text = node.value.strip('"')
    # استدعاء الدالة المساعدة لإنشاء النص كـ ثابت عالمي في الذاكرة
        return self.create_global_string(clean_text)