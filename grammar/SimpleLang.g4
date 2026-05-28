grammar SimpleLang;

// =============================================================================
// Sintaxe corrigida (sem ambiguidade; OPENG restrito a valueAtom)
// =============================================================================

program
    : BEGIN PROGRAM DPONTOS block END PROGRAM EOF
    ;

block
    : blockItem*
    ;

blockItem
    : decl
    | stmt
    ;

decl
    : INTEGER ID ATRIB expr PVIG       # IntDecl
    | BOOLEAN ID ATRIB expr PVIG       # BoolDecl
    | VAR ID ATRIB expr PVIG           # VarDecl
    ;

stmt
    : ID ATRIB expr PVIG               # AssignStmt
    | WRITE expr PVIG                  # WriteStmt
    | READ ID PVIG                     # ReadStmt
    | whileStmt                        # WhileStmtNode
    ;

whileStmt
    : WHILE ABPAR expr FPAR DO DPONTOS block END WHILE
    ;

expr
    : logicOrExpr
    ;

logicOrExpr
    : logicAndExpr (OR logicAndExpr)*
    ;

logicAndExpr
    : relExpr (AND relExpr)*
    ;

relExpr
    : addExpr ((LT | LE | GT | GE | EQ | NE) addExpr)?
    ;

addExpr
    : mulExpr ((PLUS | MINUS) mulExpr)*
    ;

mulExpr
    : unaryExpr ((MULT | DIV) unaryExpr)*
    ;

unaryExpr
    : OPNEG unaryExpr                  # UnaryNeg
    | valueAtom                        # ValueAtomExpr
    ;

valueAtom
    : ID                               # IdAtom
    | CTE                              # CteAtom
    | TRUE                             # TrueAtom
    | FALSE                            # FalseAtom
    | CADEIA                           # StringAtom
    | ABPAR expr FPAR                  # ParenAtom
    ;

// =============================================================================
// Léxico
// =============================================================================

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

fragment LETTER : [a-zA-Z];
fragment DIGIT  : [0-9];

PROGRAM : P R O G R A M ;
INTEGER : I N T E G E R ;
BOOLEAN : B O O L E A N ;
BEGIN   : B E G I N ;
END     : E N D ;
WHILE   : W H I L E ;
DO      : D O ;
READ    : R E A D ;
VAR     : V A R ;
FALSE   : F A L S E ;
TRUE    : T R U E ;
WRITE   : W R I T E ;
OR      : O R ;
AND     : A N D ;

PLUS  : '+';
MINUS : '-';
MULT  : '*';
DIV   : '/';
LT    : '<';
LE    : '<=';
GT    : '>';
GE    : '>=';
EQ    : '==';
NE    : '<>';
OPNEG : '~';

PVIG    : ';';
PONTO   : '.';
DPONTOS : ':';
VIG     : ',';
ABPAR   : '(';
FPAR    : ')';
ATRIB   : ':=';

ID : LETTER (LETTER | DIGIT)* ;

CTE : SIGN? DIGIT+ ;

fragment SIGN : '+' | '-';

CADEIA : '"' (~["\r\n])* '"' ;

LINE_COMMENT : '//' ~[\r\n]* -> skip ;
WS           : [ \t\r\n]+ -> skip ;
ERR_CHAR     : . ;
