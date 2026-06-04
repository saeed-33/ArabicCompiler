import sys
from antlr4 import *
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor
from backend.ir_generator import IRGeneratorVisitor

def main():
    print("1. جاري قراءة الكود وبناء شجرة AST...")
    input_stream = FileStream('program.arabic', encoding='utf-8')
    lexer = ShGrammarLexer(input_stream)
    parser = ShGrammarParser(CommonTokenStream(lexer))
    parse_tree = parser.program()
    
    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)
    
    print("2. جاري توليد كود LLVM IR...")
    ir_generator = IRGeneratorVisitor()
    
    # تجاوز التحليل الداللي مؤقتاً لتسريع التجربة
    llvm_ir_code = ir_generator.generate(ast)
    
    # حفظ الكود في ملف نصي
    output_file = "output.ll"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(llvm_ir_code)
        
    print(f"\n✅ تم توليد الكود بنجاح! تم الحفظ في ملف: {output_file}")

if __name__ == '__main__':
    main()