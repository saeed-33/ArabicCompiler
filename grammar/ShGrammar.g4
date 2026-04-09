grammar ShGrammar;

program : statement* EOF ;
statement
    : varDecl
    | exprStmt
    ;
varDecl : VAR ID COLON type ASSIGN expr SEMI ;
exprStmt : expr SEMI ;
type : INT_T | FLOAT_T ;

expr
: LPAREN expr RPAREN            
| expr (MUL | DIV) expr         
| expr (PLUS | MINUS) expr    
| expr (GT | LT) expr
| TRUE
| FALSE
| NUMBER                      
| ID                           
;


VAR :'متغير';
IF :'لو' | 'إذا' | 'اذا';
ELSE :'والا' | 'وإلا';
WHILE :'بينما';
PRINT :'اكتب';
TRUE :'صح';
FALSE :'غلط';
INT_T :'صحيح';
FLOAT_T :'عشري';

ASSIGN :'=';
PLUS :'+';
MINUS :'-';
MUL :'*';
DIV :'/';
GT :'>';
LT :'<';
LPAREN :'(';
RPAREN :')';
LBRACE :'{';
RBRACE :'}';
COLON :':';
SEMI :'؛';

fragment DIGIT : [0-9] | [\u0660-\u0669] ;
NUMBER  : DIGIT+ ('.' DIGIT+)? ;
ID      : [\u0621-\u064A] [\u0621-\u064A\u0660-\u06690-9_]* ;
WS      : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;