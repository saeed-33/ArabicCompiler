import sys
import pprint
# import pprint
from antlr4 import *
from frontend.ShGrammarLexer import ShGrammarLexer
from frontend.ShGrammarParser import ShGrammarParser
from frontend.ast_builder import ASTBuilderVisitor

def main(): 
    # 1 قراءة الملف 
    try: 
        input_stream = FileStream('program.arabic', encoding='utf-8') 
    except FileNotFoundError: 
        print("خطأ: الملف غير موجود") 
        sys.exit(1) 
        
    # 2 بناء شجرة ANTLR 
    lexer = ShGrammarLexer(input_stream) 
    token_stream = CommonTokenStream(lexer) 
    parser = ShGrammarParser(token_stream) 
    parse_tree = parser.program() 
    
    # 3 العبور على الشجرة وبناء الـ AST الخاصة بنا 
    builder = ASTBuilderVisitor() 
    ast = builder.visit(parse_tree) 
    
    # 4 الطباعة للتحقق من أرقام الأسطر 
    print("="*50) 
    print("شجرة ال AST النهائية (مع أرقام الأسطر) :") 
    print("="*50) 
    print(pprint.pformat(ast)) 

if __name__ == '__main__': 
    main()