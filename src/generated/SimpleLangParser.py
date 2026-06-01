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
        4,1,38,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,5,1,39,8,1,10,1,12,1,42,
        9,1,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,3,3,52,8,3,1,3,1,3,1,3,1,
        3,1,3,3,3,59,8,3,1,3,1,3,1,3,1,3,1,3,3,3,66,8,3,1,3,3,3,69,8,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,84,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,101,
        8,7,10,7,12,7,104,9,7,1,8,1,8,1,8,5,8,109,8,8,10,8,12,8,112,9,8,
        1,9,1,9,1,9,3,9,117,8,9,1,10,1,10,1,10,5,10,122,8,10,10,10,12,10,
        125,9,10,1,11,1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,12,
        3,12,136,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,3,13,149,8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,3,1,0,19,24,1,0,15,16,1,0,17,18,157,0,28,1,0,0,0,2,40,1,0,0,
        0,4,45,1,0,0,0,6,68,1,0,0,0,8,83,1,0,0,0,10,85,1,0,0,0,12,95,1,0,
        0,0,14,97,1,0,0,0,16,105,1,0,0,0,18,113,1,0,0,0,20,118,1,0,0,0,22,
        126,1,0,0,0,24,135,1,0,0,0,26,148,1,0,0,0,28,29,5,4,0,0,29,30,5,
        1,0,0,30,31,5,28,0,0,31,32,3,2,1,0,32,33,5,5,0,0,33,34,5,1,0,0,34,
        35,5,27,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,39,3,4,2,0,38,37,1,0,0,
        0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,3,1,0,0,0,42,40,1,
        0,0,0,43,46,3,6,3,0,44,46,3,8,4,0,45,43,1,0,0,0,45,44,1,0,0,0,46,
        5,1,0,0,0,47,48,5,2,0,0,48,51,5,33,0,0,49,50,5,32,0,0,50,52,3,12,
        6,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,69,5,26,0,0,54,
        55,5,3,0,0,55,58,5,33,0,0,56,57,5,32,0,0,57,59,3,12,6,0,58,56,1,
        0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,69,5,26,0,0,61,62,5,9,0,0,62,
        65,5,33,0,0,63,64,5,32,0,0,64,66,3,12,6,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,67,1,0,0,0,67,69,5,26,0,0,68,47,1,0,0,0,68,54,1,0,0,0,68,
        61,1,0,0,0,69,7,1,0,0,0,70,71,5,33,0,0,71,72,5,32,0,0,72,73,3,12,
        6,0,73,74,5,26,0,0,74,84,1,0,0,0,75,76,5,12,0,0,76,77,3,12,6,0,77,
        78,5,26,0,0,78,84,1,0,0,0,79,80,5,8,0,0,80,81,5,33,0,0,81,84,5,26,
        0,0,82,84,3,10,5,0,83,70,1,0,0,0,83,75,1,0,0,0,83,79,1,0,0,0,83,
        82,1,0,0,0,84,9,1,0,0,0,85,86,5,6,0,0,86,87,5,30,0,0,87,88,3,12,
        6,0,88,89,5,31,0,0,89,90,5,7,0,0,90,91,5,28,0,0,91,92,3,2,1,0,92,
        93,5,5,0,0,93,94,5,6,0,0,94,11,1,0,0,0,95,96,3,14,7,0,96,13,1,0,
        0,0,97,102,3,16,8,0,98,99,5,13,0,0,99,101,3,16,8,0,100,98,1,0,0,
        0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,15,1,0,0,0,
        104,102,1,0,0,0,105,110,3,18,9,0,106,107,5,14,0,0,107,109,3,18,9,
        0,108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,
        0,111,17,1,0,0,0,112,110,1,0,0,0,113,116,3,20,10,0,114,115,7,0,0,
        0,115,117,3,20,10,0,116,114,1,0,0,0,116,117,1,0,0,0,117,19,1,0,0,
        0,118,123,3,22,11,0,119,120,7,1,0,0,120,122,3,22,11,0,121,119,1,
        0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,21,1,0,
        0,0,125,123,1,0,0,0,126,131,3,24,12,0,127,128,7,2,0,0,128,130,3,
        24,12,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,23,1,0,0,0,133,131,1,0,0,0,134,136,5,25,0,0,135,134,
        1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,138,3,26,13,0,138,25,
        1,0,0,0,139,149,5,33,0,0,140,149,5,34,0,0,141,149,5,11,0,0,142,149,
        5,10,0,0,143,149,5,35,0,0,144,145,5,30,0,0,145,146,3,12,6,0,146,
        147,5,31,0,0,147,149,1,0,0,0,148,139,1,0,0,0,148,140,1,0,0,0,148,
        141,1,0,0,0,148,142,1,0,0,0,148,143,1,0,0,0,148,144,1,0,0,0,149,
        27,1,0,0,0,14,40,45,51,58,65,68,83,102,110,116,123,131,135,148
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

        def PONTO(self):
            return self.getToken(SimpleLangParser.PONTO, 0)

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
            self.match(SimpleLangParser.PONTO)
            self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589939532) != 0):
                self.state = 37
                self.blockItem()
                self.state = 42
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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.decl()
                pass
            elif token in [6, 8, 12, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
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
        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


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
        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


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
        def PVIG(self):
            return self.getToken(SimpleLangParser.PVIG, 0)
        def ATRIB(self):
            return self.getToken(SimpleLangParser.ATRIB, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolDecl" ):
                return visitor.visitBoolDecl(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = SimpleLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = SimpleLangParser.IntDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(SimpleLangParser.INTEGER)
                self.state = 48
                self.match(SimpleLangParser.ID)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 49
                    self.match(SimpleLangParser.ATRIB)
                    self.state = 50
                    self.expr()


                self.state = 53
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [3]:
                localctx = SimpleLangParser.BoolDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(SimpleLangParser.BOOLEAN)
                self.state = 55
                self.match(SimpleLangParser.ID)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 56
                    self.match(SimpleLangParser.ATRIB)
                    self.state = 57
                    self.expr()


                self.state = 60
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [9]:
                localctx = SimpleLangParser.VarDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(SimpleLangParser.VAR)
                self.state = 62
                self.match(SimpleLangParser.ID)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==32:
                    self.state = 63
                    self.match(SimpleLangParser.ATRIB)
                    self.state = 64
                    self.expr()


                self.state = 67
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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = SimpleLangParser.AssignStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(SimpleLangParser.ID)
                self.state = 71
                self.match(SimpleLangParser.ATRIB)
                self.state = 72
                self.expr()
                self.state = 73
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [12]:
                localctx = SimpleLangParser.WriteStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(SimpleLangParser.WRITE)
                self.state = 76
                self.expr()
                self.state = 77
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [8]:
                localctx = SimpleLangParser.ReadStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.match(SimpleLangParser.READ)
                self.state = 80
                self.match(SimpleLangParser.ID)
                self.state = 81
                self.match(SimpleLangParser.PVIG)
                pass
            elif token in [6]:
                localctx = SimpleLangParser.WhileStmtNodeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
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
            self.state = 85
            self.match(SimpleLangParser.WHILE)
            self.state = 86
            self.match(SimpleLangParser.ABPAR)
            self.state = 87
            self.expr()
            self.state = 88
            self.match(SimpleLangParser.FPAR)
            self.state = 89
            self.match(SimpleLangParser.DO)
            self.state = 90
            self.match(SimpleLangParser.DPONTOS)
            self.state = 91
            self.block()
            self.state = 92
            self.match(SimpleLangParser.END)
            self.state = 93
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
            self.state = 95
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
            self.state = 97
            self.logicAndExpr()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 98
                self.match(SimpleLangParser.OR)
                self.state = 99
                self.logicAndExpr()
                self.state = 104
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
            self.state = 105
            self.relExpr()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 106
                self.match(SimpleLangParser.AND)
                self.state = 107
                self.relExpr()
                self.state = 112
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
            self.state = 113
            self.addExpr()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0):
                self.state = 114
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
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
            self.state = 118
            self.mulExpr()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 119
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.mulExpr()
                self.state = 125
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
            self.state = 126
            self.unaryExpr()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.unaryExpr()
                self.state = 133
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

        def valueAtom(self):
            return self.getTypedRuleContext(SimpleLangParser.ValueAtomContext,0)


        def OPNEG(self):
            return self.getToken(SimpleLangParser.OPNEG, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = SimpleLangParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 134
                self.match(SimpleLangParser.OPNEG)


            self.state = 137
            self.valueAtom()
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                localctx = SimpleLangParser.IdAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(SimpleLangParser.ID)
                pass
            elif token in [34]:
                localctx = SimpleLangParser.CteAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(SimpleLangParser.CTE)
                pass
            elif token in [11]:
                localctx = SimpleLangParser.TrueAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(SimpleLangParser.TRUE)
                pass
            elif token in [10]:
                localctx = SimpleLangParser.FalseAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(SimpleLangParser.FALSE)
                pass
            elif token in [35]:
                localctx = SimpleLangParser.StringAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(SimpleLangParser.CADEIA)
                pass
            elif token in [30]:
                localctx = SimpleLangParser.ParenAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.match(SimpleLangParser.ABPAR)
                self.state = 145
                self.expr()
                self.state = 146
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





