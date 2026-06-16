import sys
from antlr4 import *
import llvmlite.binding as llvm
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor
from backend.ir_generator import IRGeneratorVisitor


import llvmlite.binding as llvm

def initialize_llvm():
    """Initialize LLVM with explicit target registration"""
    try:
        # These are still needed for target registration
        llvm.initialize_all_targets()
        llvm.initialize_all_asmprinters()
        
        # Verify target is available
        target = llvm.Target.from_default_triple()
        print(f"✅ LLVM initialized successfully with target: {target.name}")
        return True
    except Exception as e:
        print(f"❌ LLVM initialization failed: {e}")
        return False

def optimize_ir(raw_llvm_ir):
    """Optimize LLVM IR at O2 level using the new pass manager"""
    
    # 1. Parse and verify IR
    mod = llvm.parse_assembly(raw_llvm_ir)
    mod.verify()
    
    # 2. Create pipeline tuning options
    pto = llvm.create_pipeline_tuning_options(speed_level=2)  # O2
    
    # 3. Create target machine
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    print("target machine created for optimization:", target_machine.triple)
    # 4. Create PassBuilder and get ModulePassManager
    pass_builder = llvm.create_pass_builder(target_machine, pto)
    pm = pass_builder.getModulePassManager()
    
    # 5. Run optimizations
    pm.run(mod, pass_builder)
    
    # 6. Return optimized IR
    return str(mod)

def main():
    print("1. جاري قراءة الكود وبناء شجرة AST...")
    input_stream = FileStream('program.arabic', encoding='utf-8')
    lexer = ShGrammarLexer(input_stream)
    parser = ShGrammarParser(CommonTokenStream(lexer))
    parse_tree = parser.program()
    
    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)

    print("2. جاري توليد كود LLVM IR الخام...")
    ir_generator = IRGeneratorVisitor()
    raw_llvm_ir = ir_generator.generate(ast)

    # Save raw IR
    with open("output_raw.ll", "w", encoding="utf-8") as f:
        f.write(raw_llvm_ir)

    print("3. جاري تشغيل مدير تمريرات التحسين (Pass Manager)...")
    initialize_llvm()

    try:
        optimized_ir = optimize_ir(raw_llvm_ir)

        # Save optimized IR
        with open("output_opt.ll", "w", encoding="utf-8") as f:
            f.write(optimized_ir)

        print(
            "✅ تم تحسين الكود بنجاح! قارن بين output_raw.ll و output_opt.ll"
        )

    except Exception as e:
        print(f"❌ حدث خطأ أثناء التحسين: {e}")

if __name__ == '__main__':
    main()