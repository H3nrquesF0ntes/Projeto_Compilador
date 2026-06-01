"""Análise semântica: declarações, tipos e validações do enunciado."""

from __future__ import annotations

from compiler.cte_bounds import validate_cte_value
from compiler.errors import SemanticError
from compiler.semantic.symbol_table import SymbolTable
from compiler.semantic.types import DataType
from generated.SimpleLangParser import SimpleLangParser
from generated.SimpleLangVisitor import SimpleLangVisitor


def _truncate_id(name: str) -> str:
  return name[:16] if len(name) > 16 else name


def _cte_value(text: str) -> int:
  return validate_cte_value(int(text))


class SemanticAnalyzer(SimpleLangVisitor):
  def __init__(self) -> None:
    self.table = SymbolTable()
    self.errors: list[str] = []

  def _fail(self, message: str, ctx) -> None:
    line = ctx.start.line if hasattr(ctx, "start") else None
    column = ctx.start.column + 1 if hasattr(ctx, "start") else None
    self.errors.append(str(SemanticError(message, line=line, column=column)))

  def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
    self.visit(ctx.block())
    if self.errors:
      raise SemanticError(self.errors[0])
    return self.table

  def visitIntDecl(self, ctx: SimpleLangParser.IntDeclContext):
    name = _truncate_id(ctx.ID().getText())
    try:
      if ctx.expr() is not None:
        value_type = self._expr_type(ctx.expr())
        if value_type != DataType.INTEGER:
          self._fail(f"declaração de '{name}' exige expressão inteira", ctx)
          return
      self.table.declare(name, DataType.INTEGER)
    except ValueError as err:
      self._fail(str(err), ctx)

  def visitBoolDecl(self, ctx: SimpleLangParser.BoolDeclContext):
    name = _truncate_id(ctx.ID().getText())
    try:
      if ctx.expr() is not None:
        value_type = self._expr_type(ctx.expr())
        if value_type != DataType.BOOLEAN:
          self._fail(f"declaração de '{name}' exige expressão booleana", ctx)
          return
      self.table.declare(name, DataType.BOOLEAN)
    except ValueError as err:
      self._fail(str(err), ctx)

  def visitVarDecl(self, ctx: SimpleLangParser.VarDeclContext):
    name = _truncate_id(ctx.ID().getText())
    try:
      if ctx.expr() is not None:
        value_type = self._expr_type(ctx.expr())
        if value_type != DataType.STRING:
          self._fail(f"declaração VAR de '{name}' exige cadeia de caracteres", ctx)
          return
      self.table.declare(name, DataType.STRING)
    except ValueError as err:
      self._fail(str(err), ctx)

  def visitAssignStmt(self, ctx: SimpleLangParser.AssignStmtContext):
    name = _truncate_id(ctx.ID().getText())
    try:
      symbol = self.table.lookup(name)
    except ValueError as err:
      self._fail(str(err), ctx)
      return
    expr_type = self._expr_type(ctx.expr())
    if symbol.data_type != expr_type:
      self._fail(
        f"atribuição inválida para '{name}': esperado {symbol.data_type.value}, "
        f"obtido {expr_type.value}",
        ctx,
      )

  def visitReadStmt(self, ctx: SimpleLangParser.ReadStmtContext):
    name = _truncate_id(ctx.ID().getText())
    try:
      self.table.lookup(name)
    except ValueError as err:
      self._fail(str(err), ctx)

  def visitWriteStmt(self, ctx: SimpleLangParser.WriteStmtContext):
    self._expr_type(ctx.expr())

  def visitWhileStmtNode(self, ctx: SimpleLangParser.WhileStmtNodeContext):
    self.visit(ctx.whileStmt())

  def visitWhileStmt(self, ctx: SimpleLangParser.WhileStmtContext):
    cond_type = self._expr_type(ctx.expr())
    if cond_type != DataType.BOOLEAN:
      self._fail("condição do WHILE deve ser booleana", ctx)
    self.visit(ctx.block())

  def _expr_type(self, ctx: SimpleLangParser.ExprContext) -> DataType:
    return self.visit(ctx.logicOrExpr())

  def visitLogicOrExpr(self, ctx: SimpleLangParser.LogicOrExprContext):
    types = [self.visit(child) for child in ctx.logicAndExpr()]
    if len(types) == 1:
      return types[0]
    if any(t != DataType.BOOLEAN for t in types):
      raise ValueError("operador OR exige operandos booleanos")
    return DataType.BOOLEAN

  def visitLogicAndExpr(self, ctx: SimpleLangParser.LogicAndExprContext):
    types = [self.visit(child) for child in ctx.relExpr()]
    if len(types) == 1:
      return types[0]
    if any(t != DataType.BOOLEAN for t in types):
      raise ValueError("operador AND exige operandos booleanos")
    return DataType.BOOLEAN

  def visitRelExpr(self, ctx: SimpleLangParser.RelExprContext):
    left = self.visit(ctx.addExpr(0))
    if len(ctx.addExpr()) == 1:
      return left
    right = self.visit(ctx.addExpr(1))
    if left != right:
      raise ValueError("operador relacional exige operandos do mesmo tipo")
    if left not in (DataType.INTEGER, DataType.BOOLEAN):
      raise ValueError("operador relacional inválido para o tipo informado")
    return DataType.BOOLEAN

  def visitAddExpr(self, ctx: SimpleLangParser.AddExprContext):
    types = [self.visit(mul) for mul in ctx.mulExpr()]
    if len(types) == 1:
      return types[0]
    if any(t != DataType.INTEGER for t in types):
      raise ValueError("expressão aritmética exige operandos inteiros")
    return DataType.INTEGER

  def visitMulExpr(self, ctx: SimpleLangParser.MulExprContext):
    types = [self.visit(unary) for unary in ctx.unaryExpr()]
    if len(types) == 1:
      return types[0]
    if any(t != DataType.INTEGER for t in types):
      raise ValueError("termo aritmético exige operandos inteiros")
    return DataType.INTEGER

  def visitUnaryExpr(self, ctx: SimpleLangParser.UnaryExprContext):
    inner = self.visit(ctx.valueAtom())
    if ctx.OPNEG() is None:
      return inner
    if inner == DataType.INTEGER:
      return DataType.INTEGER
    if inner == DataType.BOOLEAN:
      return DataType.BOOLEAN
    raise ValueError("negação (~) inválida para o tipo da expressão")

  def visitIdAtom(self, ctx: SimpleLangParser.IdAtomContext):
    name = _truncate_id(ctx.ID().getText())
    return self.table.lookup(name).data_type

  def visitCteAtom(self, ctx: SimpleLangParser.CteAtomContext):
    _cte_value(ctx.CTE().getText())
    return DataType.INTEGER

  def visitTrueAtom(self, ctx: SimpleLangParser.TrueAtomContext):
    return DataType.BOOLEAN

  def visitFalseAtom(self, ctx: SimpleLangParser.FalseAtomContext):
    return DataType.BOOLEAN

  def visitStringAtom(self, ctx: SimpleLangParser.StringAtomContext):
    return DataType.STRING

  def visitParenAtom(self, ctx: SimpleLangParser.ParenAtomContext):
    return self._expr_type(ctx.expr())
