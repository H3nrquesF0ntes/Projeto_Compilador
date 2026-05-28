# Generated from C:/Users/h3nri/Documents/Compiladores/grammar/SimpleLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,5,1,38,8,1,10,1,12,1,41,9,1,
        1,2,1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,97,8,7,10,7,12,7,100,9,7,1,8,1,
        8,1,8,5,8,105,8,8,10,8,12,8,108,9,8,1,9,1,9,1,9,3,9,113,8,9,1,10,
        1,10,1,10,5,10,118,8,10,10,10,12,10,121,9,10,1,11,1,11,1,11,5,11,
        126,8,11,10,11,12,11,129,9,11,1,12,1,12,1,12,3,12,134,8,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,145,8,13,1,13,0,0,14,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,3,1,0,19,24,1,0,15,16,1,0,
        17,18,150,0,28,1,0,0,0,2,39,1,0,0,0,4,44,1,0,0,0,6,64,1,0,0,0,8,
        79,1,0,0,0,10,81,1,0,0,0,12,91,1,0,0,0,14,93,1,0,0,0,16,101,1,0,
        0,0,18,109,1,0,0,0,20,114,1,0,0,0,22,122,1,0,0,0,24,133,1,0,0,0,
        26,144,1,0,0,0,28,29,5,4,0,0,29,30,5,1,0,0,30,31,5,28,0,0,31,32,
        3,2,1,0,32,33,5,5,0,0,33,34,5,1,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,
        38,3,4,2,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,
        0,40,3,1,0,0,0,41,39,1,0,0,0,42,45,3,6,3,0,43,45,3,8,4,0,44,42,1,
        0,0,0,44,43,1,0,0,0,45,5,1,0,0,0,46,47,5,2,0,0,47,48,5,33,0,0,48,
        49,5,32,0,0,49,50,3,12,6,0,50,51,5,26,0,0,51,65,1,0,0,0,52,53,5,
        3,0,0,53,54,5,33,0,0,54,55,5,32,0,0,55,56,3,12,6,0,56,57,5,26,0,
        0,57,65,1,0,0,0,58,59,5,9,0,0,59,60,5,33,0,0,60,61,5,32,0,0,61,62,
        3,12,6,0,62,63,5,26,0,0,63,65,1,0,0,0,64,46,1,0,0,0,64,52,1,0,0,
        0,64,58,1,0,0,0,65,7,1,0,0,0,66,67,5,33,0,0,67,68,5,32,0,0,68,69,
        3,12,6,0,69,70,5,26,0,0,70,80,1,0,0,0,71,72,5,12,0,0,72,73,3,12,
        6,0,73,74,5,26,0,0,74,80,1,0,0,0,75,76,5,8,0,0,76,77,5,33,0,0,77,
        80,5,26,0,0,78,80,3,10,5,0,79,66,1,0,0,0,79,71,1,0,0,0,79,75,1,0,
        0,0,79,78,1,0,0,0,80,9,1,0,0,0,81,82,5,6,0,0,82,83,5,30,0,0,83,84,
        3,12,6,0,84,85,5,31,0,0,85,86,5,7,0,0,86,87,5,28,0,0,87,88,3,2,1,
        0,88,89,5,5,0,0,89,90,5,6,0,0,90,11,1,0,0,0,91,92,3,14,7,0,92,13,
        1,0,0,0,93,98,3,16,8,0,94,95,5,13,0,0,95,97,3,16,8,0,96,94,1,0,0,
        0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,15,1,0,0,0,100,98,
        1,0,0,0,101,106,3,18,9,0,102,103,5,14,0,0,103,105,3,18,9,0,104,102,
        1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,17,1,
        0,0,0,108,106,1,0,0,0,109,112,3,20,10,0,110,111,7,0,0,0,111,113,
        3,20,10,0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,119,
        3,22,11,0,115,116,7,1,0,0,116,118,3,22,11,0,117,115,1,0,0,0,118,
        121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,21,1,0,0,0,121,119,
        1,0,0,0,122,127,3,24,12,0,123,124,7,2,0,0,124,126,3,24,12,0,125,
        123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,
        23,1,0,0,0,129,127,1,0,0,0,130,131,5,25,0,0,131,134,3,24,12,0,132,
        134,3,26,13,0,133,130,1,0,0,0,133,132,1,0,0,0,134,25,1,0,0,0,135,
        145,5,33,0,0,136,145,5,34,0,0,137,145,5,11,0,0,138,145,5,10,0,0,
        139,145,5,35,0,0,140,141,5,30,0,0,141,142,3,12,6,0,142,143,5,31,
        0,0,143,145,1,0,0,0,144,135,1,0,0,0,144,136,1,0,0,0,144,137,1,0,
        0,0,144,138,1,0,0,0,144,139,1,0,0,0,144,140,1,0,0,0,145,27,1,0,0,
        0,11,39,44,64,79,98,106,112,119,127,133,144
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'<='", "'>'", "'>='", "'=='", 
                     "'<>'", "'~'", "';'", "'.'", "':'", "','", "'('", "')'", 
                     "':='" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "INTEGER", "BOOLEAN", "BEGIN", 
                      "END", "WHILE", "DO", "READ", "VAR", "FALSE", "TRUE", 
                      "WRITE", "OR", "AND", "PLUS", "MINUS", "MULT", "DIV", 
                      "LT", "LE", "GT", "GE", "EQ", "NE", "OPNEG", "PVIG", 
                      "PONTO", "DPONTOS", "VIG", "ABPAR", "FPAR", "ATRIB", 
                      "ID", "CTE", "CADEIA", "LINE_COMMENT", "WS", "ERR_CHAR" ]

    RULE_program = 0
    RULE_block = 1
    RULE_blockItem = 2
    RULE_decl = 3
    RULE_stmt = 4
    RULE_whileStmt = 5
    RULE_expr = 6
    RULE_logicOrExpr = 7
    RULE_logicAndExpr = 8
    RULE_relExpr = 9
    RULE_addExpr = 10
    RULE_mulExpr = 11
    RULE_unaryExpr = 12
    RULE_valueAtom = 13

    ruleNames =  [ "program", "block", "blockItem", "decl", "stmt", "whileStmt", 
                   "expr", "logicOrExpr", "logicAndExpr", "relExpr", "addExpr", 
                   "mulExpr", "unaryExpr", "valueAtom" ]

    EOF = Token.EOF
    PROGRAM=1
    INTEGER=2
    BOOLEAN=3
    BEGIN=4
    END=5
    WHILE=6
    DO=7
    READ=8
    VAR=9
    FALSE=10
    TRUE=11
    WRITE=12
    OR=13
    AND=14
    PLUS=15
    MINUS=16
    MULT=17
    DIV=18
    LT=19
    LE=20
    GT=21
    GE=22
    EQ=23
    NE=24
    OPNEG=25
    PVIG=26
    PONTO=27
    DPONTOS=28
    VIG=29
    ABPAR=30
    FPAR=31
    ATRIB=32
    ID=33
    CTE=34
    CADEIA=35
    LINE_COMMENT=36
    WS=37
    ERR_CHAR=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(SimpleLangParser.BEGIN, 0)

        def PROGRAM(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.PROGRAM)
            else:
                return self.getToken(SimpleLangParser.PROGRAM, i)

        def DPONTOS(self):
            return self.getToken(SimpleLangParser.DPONTOS, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def END(self):
            return self.getToken(SimpleLangParser.END, 0)

        def EOF(self):
            return self.getToken(SimpleLangParser.EOF, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(SimpleLangParser.BEGIN)
            self.state = 29
            self.match(SimpleLangParser.PROGRAM)
            self.state = 30
            self.match(SimpleLangParser.DPONTOS)
            self.state = 31
            self.block()
            self.state = 32
            self.match(SimpleLangParser.END)
            self.state = 33
            self.match(SimpleLangParser.PROGRAM)
            self.state = 34
            self.match(SimpleLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.BlockItemContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.BlockItemContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SimpleLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589939532) != 0):
                self.state = 36
                self.blockItem()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(SimpleLangParser.DeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(SimpleLangParser.StmtContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_blockItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockItem" ):
                return visitor.visitBlockItem(self)
            else:
                return visitor.visitChildren(self)




    def blockItem(self):

        localctx = SimpleLangParser.BlockItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockItem)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.decl()
                pass
            elif token in [6, 8, 12, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarDeclContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(SimpleLangParser.VAR, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)


    class IntDeclContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(SimpleLangParser.INTEGER, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntDecl" ):
                return visitor.visitIntDecl(self)
            else:
                return visitor.visitChildren(self)


    class BoolDeclContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.DeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SimpleLangParser.BOOLEAN, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolDecl" ):
                return visitor.visitBoolDecl(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = SimpleLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = SimpleLangParser.IntDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(SimpleLangParser.INTEGER)
                self.state = 47
                self.match(SimpleLangParser.ID)
                self.state = 48
                self.match(SimpleLangParser.ATRIB)
                self.state = 49
                self.expr()
                self.state = 50
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [3]:
                localctx = SimpleLangParser.BoolDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(SimpleLangParser.BOOLEAN)
                self.state = 53
                self.match(SimpleLangParser.ID)
                self.state = 54
                self.match(SimpleLangParser.ATRIB)
                self.state = 55
                self.expr()
                self.state = 56
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [9]:
                localctx = SimpleLangParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.match(SimpleLangParser.VAR)
                self.state = 59
                self.match(SimpleLangParser.ID)
                self.state = 60
                self.match(SimpleLangParser.ATRIB)
                self.state = 61
                self.expr()
                self.state = 62
                self.match(SimpleLangParser.PVIG)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)


    class WriteStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(SimpleLangParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReadStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(SimpleLangParser.READ, 0)
        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStmt" ):
                return visitor.visitReadStmt(self)
            else:
                return visitor.visitChildren(self)


    class WhileStmtNodeContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStmt(self):
            return self.getTypedRuleContext(SimpleLangParser.WhileStmtContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmtNode" ):
                return visitor.visitWhileStmtNode(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = SimpleLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = SimpleLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(SimpleLangParser.ID)
                self.state = 67
                self.match(SimpleLangParser.ATRIB)
                self.state = 68
                self.expr()
                self.state = 69
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [12]:
                localctx = SimpleLangParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(SimpleLangParser.WRITE)
                self.state = 72
                self.expr()
                self.state = 73
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [8]:
                localctx = SimpleLangParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(SimpleLangParser.READ)
                self.state = 76
                self.match(SimpleLangParser.ID)
                self.state = 77
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [6]:
                localctx = SimpleLangParser.WhileStmtNodeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.WHILE)
            else:
                return self.getToken(SimpleLangParser.WHILE, i)

        def ABPAR(self):
            return self.getToken(SimpleLangParser.ABPAR, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def FPAR(self):
            return self.getToken(SimpleLangParser.FPAR, 0)

        def DO(self):
            return self.getToken(SimpleLangParser.DO, 0)

        def DPONTOS(self):
            return self.getToken(SimpleLangParser.DPONTOS, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleLangParser.BlockContext,0)


        def END(self):
            return self.getToken(SimpleLangParser.END, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_whileStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = SimpleLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SimpleLangParser.WHILE)
            self.state = 82
            self.match(SimpleLangParser.ABPAR)
            self.state = 83
            self.expr()
            self.state = 84
            self.match(SimpleLangParser.FPAR)
            self.state = 85
            self.match(SimpleLangParser.DO)
            self.state = 86
            self.match(SimpleLangParser.DPONTOS)
            self.state = 87
            self.block()
            self.state = 88
            self.match(SimpleLangParser.END)
            self.state = 89
            self.match(SimpleLangParser.WHILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOrExpr(self):
            return self.getTypedRuleContext(SimpleLangParser.LogicOrExprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SimpleLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.logicOrExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.LogicAndExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.LogicAndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.OR)
            else:
                return self.getToken(SimpleLangParser.OR, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_logicOrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOrExpr" ):
                return visitor.visitLogicOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicOrExpr(self):

        localctx = SimpleLangParser.LogicOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_logicOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.logicAndExpr()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 94
                self.match(SimpleLangParser.OR)
                self.state = 95
                self.logicAndExpr()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.RelExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.RelExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.AND)
            else:
                return self.getToken(SimpleLangParser.AND, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_logicAndExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAndExpr" ):
                return visitor.visitLogicAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def logicAndExpr(self):

        localctx = SimpleLangParser.LogicAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_logicAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.relExpr()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 102
                self.match(SimpleLangParser.AND)
                self.state = 103
                self.relExpr()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.AddExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.AddExprContext,i)


        def LT(self):
            return self.getToken(SimpleLangParser.LT, 0)

        def LE(self):
            return self.getToken(SimpleLangParser.LE, 0)

        def GT(self):
            return self.getToken(SimpleLangParser.GT, 0)

        def GE(self):
            return self.getToken(SimpleLangParser.GE, 0)

        def EQ(self):
            return self.getToken(SimpleLangParser.EQ, 0)

        def NE(self):
            return self.getToken(SimpleLangParser.NE, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_relExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)




    def relExpr(self):

        localctx = SimpleLangParser.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_relExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.addExpr()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                self.state = 110
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.addExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.MulExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.MulExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.PLUS)
            else:
                return self.getToken(SimpleLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.MINUS)
            else:
                return self.getToken(SimpleLangParser.MINUS, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_addExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)




    def addExpr(self):

        localctx = SimpleLangParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.mulExpr()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 115
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 116
                self.mulExpr()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.UnaryExprContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.MULT)
            else:
                return self.getToken(SimpleLangParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.DIV)
            else:
                return self.getToken(SimpleLangParser.DIV, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_mulExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)




    def mulExpr(self):

        localctx = SimpleLangParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.unaryExpr()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 123
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 124
                self.unaryExpr()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_unaryExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnaryNegContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPNEG(self):
            return self.getToken(SimpleLangParser.OPNEG, 0)
        def unaryExpr(self):
            return self.getTypedRuleContext(SimpleLangParser.UnaryExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryNeg" ):
                return visitor.visitUnaryNeg(self)
            else:
                return visitor.visitChildren(self)


    class ValueAtomExprContext(UnaryExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.UnaryExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def valueAtom(self):
            return self.getTypedRuleContext(SimpleLangParser.ValueAtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueAtomExpr" ):
                return visitor.visitValueAtomExpr(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpr(self):

        localctx = SimpleLangParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unaryExpr)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = SimpleLangParser.UnaryNegContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.match(SimpleLangParser.OPNEG)
                self.state = 131
                self.unaryExpr()
                pass
            elif token in [10, 11, 30, 33, 34, 35]:
                localctx = SimpleLangParser.ValueAtomExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.valueAtom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_valueAtom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TrueAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(SimpleLangParser.TRUE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueAtom" ):
                return visitor.visitTrueAtom(self)
            else:
                return visitor.visitChildren(self)


    class FalseAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(SimpleLangParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFalseAtom" ):
                return visitor.visitFalseAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CADEIA(self):
            return self.getToken(SimpleLangParser.CADEIA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringAtom" ):
                return visitor.visitStringAtom(self)
            else:
                return visitor.visitChildren(self)


    class CteAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CTE(self):
            return self.getToken(SimpleLangParser.CTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCteAtom" ):
                return visitor.visitCteAtom(self)
            else:
                return visitor.visitChildren(self)


    class ParenAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABPAR(self):
            return self.getToken(SimpleLangParser.ABPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)

        def FPAR(self):
            return self.getToken(SimpleLangParser.FPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenAtom" ):
                return visitor.visitParenAtom(self)
            else:
                return visitor.visitChildren(self)


    class IdAtomContext(ValueAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ValueAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdAtom" ):
                return visitor.visitIdAtom(self)
            else:
                return visitor.visitChildren(self)



    def valueAtom(self):

        localctx = SimpleLangParser.ValueAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_valueAtom)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = SimpleLangParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(SimpleLangParser.ID)
                pass
            elif token in [34]:
                localctx = SimpleLangParser.CteAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(SimpleLangParser.CTE)
                pass
            elif token in [11]:
                localctx = SimpleLangParser.TrueAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(SimpleLangParser.TRUE)
                pass
            elif token in [10]:
                localctx = SimpleLangParser.FalseAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(SimpleLangParser.FALSE)
                pass
            elif token in [35]:
                localctx = SimpleLangParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 139
                self.match(SimpleLangParser.CADEIA)
                pass
            elif token in [30]:
                localctx = SimpleLangParser.ParenAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 140
                self.match(SimpleLangParser.ABPAR)
                self.state = 141
                self.expr()
                self.state = 142
                self.match(SimpleLangParser.FPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





