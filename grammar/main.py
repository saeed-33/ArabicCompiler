import sys
from antlr4 import *
from ShGrammarLexer import ShGrammarLexer
from ShGrammarParser import ShGrammarParser
from custom_visitor import CustomASTVisitor

def main():
    # 1. قراءة الملف المصدري
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print("program.arabic خطأ : لم يتم العثور على الملف")
        sys.exit(1)

    # 2. التحليل المعجمي (Lexer)
    lexer = ShGrammarLexer (input_stream)
    token_stream = CommonTokenStream (lexer)

    # 3. التحليل النحوي (Parser)
    parser = ShGrammarParser (token_stream)
    # البدء من القاعدة الجذرية program للحصول على شجرة الإعراب
    parse_tree = parser.program()

    # 4. العبور على الشجرة باستخدام الزائر لبناء الـ AST
    visitor = CustomASTVisitor()
    ast = visitor.visit(parse_tree)

    # 50. طباعة هيكل الـ AST النظيف
    print("="*50)
    print(": الناتجة (AST) شجرة القواعد المجردة")
    # توفر dataclasses ميزة (repr) جاهزة وجميلة للكائنات في بايثون
    print("="*50)
    import pprint
    print (pprint.pformat(ast))

if __name__ == '__main__':
    main()