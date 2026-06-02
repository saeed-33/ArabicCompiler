# main.py
import sys
import pprint
from antlr4 import *
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor
from frontend.ast_visualizer import ASTVisualizerVisitor  # استيراد الزائر البصري المعدل

def main():
    # 1. قراءة ملف الكود العربي
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print("خطأ: الملف غير موجود")
        sys.exit(1)

    # 2. بناء شجرة التحليل النحوي عبر ANTLR
    lexer = ShGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ShGrammarParser(token_stream)
    parse_tree = parser.program()

    # 3. العبور وبناء شجرة الـ AST المخصصة لنا
    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)
    
    print("==================================================")
    print("تم بناء الـ AST بنجاح! جاري توليد المخطط الهندسي البصري...")
    print("==================================================")

    # 4. تشغيل زائر الرسم البصري وتوليد الصورة
    visualizer = ASTVisualizerVisitor()
    ast.accept(visualizer)  # نقطة الانطلاق لتمرير الزائر عبر الشجرة
    visualizer.render('my_arabic_ast')  # سيقوم بحفظ وعرض ملف my_arabic_ast.png تلقائياً
    
    print("اكتمل العمل! تفقد المخطط البصري المفتوح أمامك.")

if __name__ == '__main__':
    main()