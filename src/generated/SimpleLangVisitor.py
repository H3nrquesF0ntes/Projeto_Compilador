# Generated from C:/Users/h3nri/Documents/Compiladores/grammar/SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#block.
    def visitBlock(self, ctx:SimpleLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#blockItem.
    def visitBlockItem(self, ctx:SimpleLangParser.BlockItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IntDecl.
    def visitIntDecl(self, ctx:SimpleLangParser.IntDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolDecl.
    def visitBoolDecl(self, ctx:SimpleLangParser.BoolDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#VarDecl.
    def visitVarDecl(self, ctx:SimpleLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AssignStmt.
    def visitAssignStmt(self, ctx:SimpleLangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#WriteStmt.
    def visitWriteStmt(self, ctx:SimpleLangParser.WriteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ReadStmt.
    def visitReadStmt(self, ctx:SimpleLangParser.ReadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#WhileStmtNode.
    def visitWhileStmtNode(self, ctx:SimpleLangParser.WhileStmtNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#whileStmt.
    def visitWhileStmt(self, ctx:SimpleLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#expr.
    def visitExpr(self, ctx:SimpleLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#logicOrExpr.
    def visitLogicOrExpr(self, ctx:SimpleLangParser.LogicOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#logicAndExpr.
    def visitLogicAndExpr(self, ctx:SimpleLangParser.LogicAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#relExpr.
    def visitRelExpr(self, ctx:SimpleLangParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#addExpr.
    def visitAddExpr(self, ctx:SimpleLangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#mulExpr.
    def visitMulExpr(self, ctx:SimpleLangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:SimpleLangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#IdAtom.
    def visitIdAtom(self, ctx:SimpleLangParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#CteAtom.
    def visitCteAtom(self, ctx:SimpleLangParser.CteAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#TrueAtom.
    def visitTrueAtom(self, ctx:SimpleLangParser.TrueAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#FalseAtom.
    def visitFalseAtom(self, ctx:SimpleLangParser.FalseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#StringAtom.
    def visitStringAtom(self, ctx:SimpleLangParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParenAtom.
    def visitParenAtom(self, ctx:SimpleLangParser.ParenAtomContext):
        return self.visitChildren(ctx)



del SimpleLangParser