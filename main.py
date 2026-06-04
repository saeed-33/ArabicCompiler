import sys
from antlr4 import *
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor
from semantic.semantic_analyzer import SemanticAnalyzerVisitor
from semantic.semantic_visitor import SemanticVisitor

def main():
    # 1. قراءة وبناء الشجرة (Front-End)
    input_stream = FileStream('program.arabic', encoding='utf-8')
    lexer = ShGrammarLexer(input_stream)
    parser = ShGrammarParser(CommonTokenStream(lexer))
    parse_tree = parser.program()
   
    # 2. تحويل شجرة ANTLR إلى AST مخصصة
    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)
    print("--- جاري التحليل الداللي (Type Checking) ---")

    # 3. التحليل الداللي (التحقق من الأنواع والنطاقات)
    analyzer = SemanticAnalyzerVisitor()
    ast.accept(analyzer) # إرسال الزائر للشجرة
   
    # 4. طباعة تقرير الأخطاء
    if len(analyzer.errors) > 0:
        print("\nتم العثور على الأخطاء التالية:")
        for err in analyzer.errors:
            print(" ❌ " + err)
        
        print("\nفشلت عملية الترجمة. الرجاء إصلاح الأخطاء أعلاه.")
    else:
        print("✅ الكود سليم دلالياً ونحوياً 100%. جاهز لتوليد كود الآلة (IR)!")

if __name__ == '__main__':
    main()