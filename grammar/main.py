import sys
from antlr4 import *
from ShLexer import ShLexer

def main():
    try:
        input_stream = FileStream('program.arabic', encoding='utf-8')
    except FileNotFoundError:
        print("خطأ: لم يتم العثور على الملف program.arabic")
        sys.exit(1)

    lexer = ShLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("="*50)
    print(f"{'النص (Lexeme)':>15} | {'نوع الرمز (Token)':>15} | {'السطر'}")
    print("="*50)

    for token in token_stream.tokens:
        if token.type == Token.EOF:
            break
        
        token_name = lexer.symbolicNames[token.type]
        print(f"{token.text:>15} | {token_name:>15} | {token.line}")

if __name__ == '__main__':
    main()