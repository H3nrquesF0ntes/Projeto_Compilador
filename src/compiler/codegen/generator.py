"""Geração de código intermediário (quádruplos)."""

from __future__ import annotations

from compiler.codegen.quad import Quadruple
from compiler.semantic.symbol_table import SymbolTable
from generated.SimpleLangLexer import SimpleLangLexer
from generated.SimpleLangParser import SimpleLangParser
from generated.SimpleLangVisitor import SimpleLangVisitor


class CodeGenerator(SimpleLangVisitor):
  def __init__(self, symbol_table: SymbolTable) -> None:
    self.table = symbol_table
    self.quads: list[Quadruple] = []
    self._temp = 0
    self._labels = 0

  def _new_temp(self) -> str:
    self._temp += 1
    return f"t{self._temp}"

  def _new_label(self) -> str:
    self._labels += 1
    return f"L{self._labels}"

  def _emit(self, op: str, arg1=None, arg2=None, result=None) -> int:
    self.quads.append(Quadruple(op, arg1, arg2, result))
    return len(self.quads) - 1

  def _backpatch(self, indexes: list[int], label: str) -> None:
    for idx in indexes:
      q = self.quads[idx]
      self.quads[idx] = Quadruple(q.op, q.arg1, q.arg2, label)

  def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
    self.visit(ctx.block())
    self._emit("halt")
    return self.quads

  def visitIntDecl(self, ctx: SimpleLangParser.IntDeclContext):
    name = ctx.ID().getText()[:16]
    value = self.visit(ctx.expr())
    self._emit("store", value, None, name)

  def visitBoolDecl(self, ctx: SimpleLangParser.BoolDeclContext):
    name = ctx.ID().getText()[:16]
    value = self.visit(ctx.expr())
    self._emit("store", value, None, name)

  def visitVarDecl(self, ctx: SimpleLangParser.VarDeclContext):
    name = ctx.ID().getText()[:16]
    value = self.visit(ctx.expr())
    self._emit("store", value, None, name)

  def visitAssignStmt(self, ctx: SimpleLangParser.AssignStmtContext):
    name = ctx.ID().getText()[:16]
    value = self.visit(ctx.expr())
    self._emit("store", value, None, name)

  def visitReadStmt(self, ctx: SimpleLangParser.ReadStmtContext):
    name = ctx.ID().getText()[:16]
    self._emit("read", None, None, name)

  def visitWriteStmt(self, ctx: SimpleLangParser.WriteStmtContext):
    value = self.visit(ctx.expr())
    self._emit("write", value, None, None)

  def visitWhileStmt(self, ctx: SimpleLangParser.WhileStmtContext):
    start = self._new_label()
    end = self._new_label()
    self._emit("label", None, None, start)
    cond = self.visit(ctx.expr())
    false_idx = self._emit("if_false", cond, None, None)
    self.visit(ctx.block())
    self._emit("goto", None, None, start)
    self._emit("label", None, None, end)
    self._backpatch([false_idx], end)

  def visitLogicOrExpr(self, ctx: SimpleLangParser.LogicOrExprContext):
    parts = ctx.logicAndExpr()
    if len(parts) == 1:
      return self.visit(parts[0])
    acc = self.visit(parts[0])
    for part in parts[1:]:
      right = self.visit(part)
      temp = self._new_temp()
      self._emit("or", acc, right, temp)
      acc = temp
    return acc

  def visitLogicAndExpr(self, ctx: SimpleLangParser.LogicAndExprContext):
    parts = ctx.relExpr()
    if len(parts) == 1:
      return self.visit(parts[0])
    acc = self.visit(parts[0])
    for part in parts[1:]:
      right = self.visit(part)
      temp = self._new_temp()
      self._emit("and", acc, right, temp)
      acc = temp
    return acc

  def visitRelExpr(self, ctx: SimpleLangParser.RelExprContext):
    left = self.visit(ctx.addExpr(0))
    if len(ctx.addExpr()) == 1:
      return left
    right = self.visit(ctx.addExpr(1))
    op_token = ctx.getChild(1).getSymbol().type
    op_map = {
      SimpleLangLexer.LT: "lt",
      SimpleLangLexer.LE: "le",
      SimpleLangLexer.GT: "gt",
      SimpleLangLexer.GE: "ge",
      SimpleLangLexer.EQ: "eq",
      SimpleLangLexer.NE: "ne",
    }
    temp = self._new_temp()
    self._emit(op_map[op_token], left, right, temp)
    return temp

  def visitAddExpr(self, ctx: SimpleLangParser.AddExprContext):
    acc = self.visit(ctx.mulExpr(0))
    for i in range(1, len(ctx.mulExpr())):
      op_token = ctx.getChild(2 * i - 1).getSymbol().type
      right = self.visit(ctx.mulExpr(i))
      temp = self._new_temp()
      if op_token == SimpleLangLexer.PLUS:
        self._emit("add", acc, right, temp)
      else:
        self._emit("sub", acc, right, temp)
      acc = temp
    return acc

  def visitMulExpr(self, ctx: SimpleLangParser.MulExprContext):
    acc = self.visit(ctx.unaryExpr(0))
    for i in range(1, len(ctx.unaryExpr())):
      op_token = ctx.getChild(2 * i - 1).getSymbol().type
      right = self.visit(ctx.unaryExpr(i))
      temp = self._new_temp()
      if op_token == SimpleLangLexer.MULT:
        self._emit("mul", acc, right, temp)
      else:
        self._emit("div", acc, right, temp)
      acc = temp
    return acc

  def visitUnaryNeg(self, ctx: SimpleLangParser.UnaryNegContext):
    inner = self.visit(ctx.unaryExpr())
    temp = self._new_temp()
    self._emit("neg", inner, None, temp)
    return temp

  def visitIdAtom(self, ctx: SimpleLangParser.IdAtomContext):
    return ctx.ID().getText()[:16]

  def visitCteAtom(self, ctx: SimpleLangParser.CteAtomContext):
    return ctx.CTE().getText()

  def visitTrueAtom(self, ctx: SimpleLangParser.TrueAtomContext):
    return "true"

  def visitFalseAtom(self, ctx: SimpleLangParser.FalseAtomContext):
    return "false"

  def visitStringAtom(self, ctx: SimpleLangParser.StringAtomContext):
    return ctx.CADEIA().getText()

  def visitParenAtom(self, ctx: SimpleLangParser.ParenAtomContext):
    return self.visit(ctx.expr())

  def visitValueAtomExpr(self, ctx: SimpleLangParser.ValueAtomExprContext):
    return self.visit(ctx.valueAtom())
