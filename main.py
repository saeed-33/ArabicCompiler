import sys
from antlr4 import *
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor
from semantic.semantic_visitor import SemanticVisitor

def main():
    # 1. قراءة الملف وبناء شجرة التحليل الإعرابي بواسطة ANTLR
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print("خطأ: الملف 'program.arabic' غير موجود.")
        sys.exit(1)

    lexer = ShGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShGrammarParser(token_stream)
    parse_tree = parser.program()

    # 2. بناء شجرة الـ AST المخصصة
    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)
    
    print("==================================================")
    print("--- جاري التحليل الدلالي (فحص النطاقات والمتغيرات) ---")
    print("==================================================")

    # 3. تمرير الزائر الدلالي على الشجرة لفحص النطاقات والرموز
    semantic_visitor = SemanticVisitor()
    ast.accept(semantic_visitor)

    # 4. طباعة تقرير الأخطاء الهندسي الموحد
    if semantic_visitor.errors:
        print("\n❌ تم العثور على أخطاء دلالية:")
        for err in semantic_visitor.errors:
            print(f"   {err}")
    else:
        print("\n✅ الكود سليم دلالياً! جميع المتغيرات والنطاقات صحيحة.")

if __name__ == "__main__":
    main()