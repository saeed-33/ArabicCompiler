from platform import node

import llvmlite.ir as ir
import llvmlite.binding as llvm

from ast_tree.nodes import *
from ast_tree.visitor_interface import ASTVisitor

class IRGeneratorVisitor(ASTVisitor):
    def __init__(self):
        # 1. إنشاء الوحدة (Module): الحاوية الكبرى التي تمثل الملف بأكمله
        self.module = ir.Module(name="arabic_compiler_module")
        
        default_triple = llvm.get_default_triple()
        self.module.triple = default_triple
        # 1. Byte pointer type (i8*)
        self.byte_ptr_type = ir.IntType(8).as_pointer()

        # 2. Declare printf
        printf_type = ir.FunctionType(
            ir.IntType(32),
            [self.byte_ptr_type],
            var_arg=True
        )

        self.printf_func = ir.Function(
            self.module,
            printf_type,
            name="printf"
        )
        
        panic_type = ir.FunctionType(ir.VoidType(), [])
        self.panic_func = ir.Function(self.module, panic_type, name="panic_div_zero")

        # 3. Counter for global string constants
        self.string_counter = 0
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
       
        
    def emit_runtime_trap(self, is_danger_i1, panic_function):
        current_func = self.builder.function
        
        # 1. إنشاء كتلتين: واحدة للانهيار، وواحدة لاستمرار البرنامج (المنطقة الآمنة)
        panic_bb = current_func.append_basic_block("panic_block")
        continue_bb = current_func.append_basic_block("math_block")
        
        # 2. القفز المشروط: إذا كان هناك خطر، اقفز لكتلة الذعر، وإلا أكمل للمنطقة الآمنة
        self.builder.cbranch(is_danger_i1, panic_bb, continue_bb)
        
        # 3. برمجة كتلة الذعر (Panic Block)
        self.builder.position_at_end(panic_bb)
        # استدعاء دالة الطباعة وإنهاء البرنامج
        self.builder.call(panic_function, [])
        # تعليمة حاسمة تخبر المحسن أن البرنامج يتوقف هنا نهائيًا
        self.builder.unreachable()
        
        # 4. نقل القلم إلى المنطقة الآمنة ليستأنف الزائر عمله الطبيعي
        self.builder.position_at_end(continue_bb)
        
    def create_global_string(self, string_text: str):
        # 1. Add newline and null terminator
        string_text = string_text + '\n\0'

        # 2. Encode Arabic text as UTF-8 bytes
        encoded_bytes = bytearray(string_text.encode('utf-8'))

        # 3. Create array type [N x i8]
        array_type = ir.ArrayType(
            ir.IntType(8),
            len(encoded_bytes)
        )

        # 4. Create global constant
        global_name = f".str_{self.string_counter}"
        self.string_counter += 1

        global_str = ir.GlobalVariable(
            self.module,
            array_type,
            name=global_name
        )

        global_str.linkage = 'private'
        global_str.global_constant = True
        global_str.initializer = ir.Constant(
            array_type,
            encoded_bytes
        )

        return global_str

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
            # --- بداية زرع فخ الحماية ---
            # 1. إنشاء ثابت قيمته صفر للمقارنة
            zero_val = ir.Constant(ir.IntType(32), 0)
            
            # 2. فحص المقام: هل يساوي صفرًا؟ (يرجع i1)
            is_zero = self.builder.icmp_signed('==', right_val, zero_val, name="is_zero_trap")
            
            # 3. استدعاء الدالة المساعدة لزرع كتل الفخ وإيقاف البرنامج إن لزم الأمر
            self.emit_runtime_trap(is_zero, self.panic_func)
            # --- نهاية الفخ (القلم الآن موجود بأمان داخل كتلة math_block) ---
            
            # إجراء عملية القسمة بأمان تام
            return self.builder.sdiv(left_val, right_val, name="divtmp")
        elif node.op == '<':
            return self.builder.icmp_signed('<',left_val,right_val, name="Lttemp")
        elif node.op == '>':
            return self.builder.icmp_signed('>',left_val,right_val, name="Gttemp")
        elif node.op == '==':
            return self.builder.icmp_signed('==',left_val,right_val, name="Eqtemp")
        elif node.op == '!=':
            return self.builder.icmp_signed('!=',left_val,right_val, name="Neqtemp")
        
        else:
            raise NotImplementedError(f"العملية الرياضية '{node.op}' غير مدعومة حالياً.")

    # ---------------------------------------------------------
    # باقي الدوال ستظل فارغة للأيام القادمة
    # ---------------------------------------------------------
    def visit_PrintNode(self, node:PrintNode):
        # 1. Create global string constant
        zero = ir.Constant(ir.IntType(32), 0)
        if  isinstance(node.expr, StringNode):
            global_str = self.create_global_string(node.expr.value)
                # 2. Convert array to pointer using GEP
           

            str_ptr = self.builder.gep(
                global_str,
                [zero, zero],
                inbounds=True,
                name="str_ptr"
            )
                # 3. Call printf
            self.builder.call(
                self.printf_func,
                [str_ptr],
                name="print_call"
            )
        else:
            global_str = self.create_global_string("%d")
            str_ptr = self.builder.gep(
                global_str,
                [zero, zero],
                inbounds=True,
                name="str_ptr"
            )
                # 3. Call printf
            self.builder.call(
                self.printf_func,
                [str_ptr,self.visit(node.expr)],
                name="print_call"
            )
       

        
        
    
    def visit_IfNode(self, node): 
        cond_val = self.visit(node.condition)
        current_function = self.builder.function
        then_bb = current_function.append_basic_block("then")
        merge_bb = current_function.append_basic_block("ifcont")
        if node.else_block:
            else_bb = current_function.append_basic_block("else")
            self.builder.cbranch(cond_val, then_bb, else_bb)
        else:
            self.builder.cbranch(cond_val,then_bb,merge_bb)
        self.builder.position_at_end(then_bb)
        self.visit(node.then_block)
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)
        if node.else_block:
            self.builder.position_at_end(else_bb)
            self.visit(node.else_block)
            if not self.builder.block.is_terminated:
                self.builder.branch(merge_bb)
        
        self.builder.position_at_end(merge_bb)
        
    
    
    
    def visit_WhileNode(self, node): 
        current_func = self.builder.function

    # 1. Create the three blocks
        cond_bb = current_func.append_basic_block("while_cond")
        body_bb = current_func.append_basic_block("while_body")
        end_bb = current_func.append_basic_block("while_end")

    # 2. Jump to loop condition
        self.builder.branch(cond_bb)

    # 3. Generate condition block
        self.builder.position_at_end(cond_bb)

        cond_val = self.visit(node.condition)
        if cond_val is None:
            raise Exception("خطأ هندسي: تعذر تقييم شرط الحلقة.")

        # Conditional branch
        self.builder.cbranch(cond_val, body_bb, end_bb)

        # 4. Generate body block
        self.builder.position_at_end(body_bb)

    # Push current loop information
        self.loop_stack.append((cond_bb, end_bb))

    # Visit loop body
        self.visit(node.body)

    # Pop loop information
        self.loop_stack.pop()

    # 5. Back-edge to condition
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_bb)

    # 6. Continue after loop
        self.builder.position_at_end(end_bb)
        
        
    def visit_BlockNode(self, node:BlockNode): 
        for stmt in node.statements:
            self.visit(stmt)
            
            
    def visit_ContinueNode(self, node:ContinueNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'تجاوز' خارج حلقة تكرار")

    # Get condition block of current loop
        cond_bb, _ = self.loop_stack[-1]
        self.builder.branch(cond_bb)
        
    def visit_BreakNode(self, node:BreakNode):
        if not self.loop_stack:
            raise Exception("خطأ نحوي: تم استخدام أمر 'اكسر' خارج حلقة تكرار")
         # Get end block of current loop
        _, end_bb = self.loop_stack[-1]
        self.builder.branch(end_bb)