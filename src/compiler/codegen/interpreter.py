"""Interpretador simples dos quádruplos gerados (para demonstração)."""

from __future__ import annotations

from compiler.codegen.quad import Quadruple
from compiler.semantic.symbol_table import SymbolTable
from compiler.semantic.types import DataType


class QuadrupleInterpreter:
  def __init__(self, quads: list[Quadruple], symbols: SymbolTable) -> None:
    self.quads = quads
    self.symbols = symbols
    self.memory: dict[str, object] = {}
    self._label_index = {q.result: idx for idx, q in enumerate(quads) if q.op == "label"}

  def run(self) -> None:
    ip = 0
    while ip < len(self.quads):
      quad = self.quads[ip]
      ip += 1

      if quad.op == "halt":
        break

      if quad.op == "label":
        continue

      if quad.op == "goto":
        ip = self._label_index[quad.result]
        continue

      if quad.op == "if_false":
        if not self._truthy(self._resolve(quad.arg1)):
          ip = self._label_index[quad.result]
        continue

      if quad.op == "store":
        self.memory[quad.result] = self._resolve(quad.arg1)
        continue

      if quad.op == "read":
        symbol = self.symbols.lookup(quad.result)
        raw = input(f"Informe valor para {quad.result}: ")
        self.memory[quad.result] = self._parse_input(raw, symbol.data_type)
        continue

      if quad.op == "write":
        value = self._resolve(quad.arg1)
        print(self._format_output(value))
        continue

      left = self._resolve(quad.arg1)
      right = self._resolve(quad.arg2) if quad.arg2 is not None else None
      self.memory[quad.result] = self._apply_op(quad.op, left, right)

  def _apply_op(self, op: str, left, right):
    if op == "add":
      return int(left) + int(right)
    if op == "sub":
      return int(left) - int(right)
    if op == "mul":
      return int(left) * int(right)
    if op == "div":
      return int(left) // int(right)
    if op == "neg":
      if isinstance(left, bool):
        return not left
      return -int(left)
    if op == "or":
      return bool(left) or bool(right)
    if op == "and":
      return bool(left) and bool(right)
    if op == "lt":
      return int(left) < int(right)
    if op == "le":
      return int(left) <= int(right)
    if op == "gt":
      return int(left) > int(right)
    if op == "ge":
      return int(left) >= int(right)
    if op == "eq":
      return left == right
    if op == "ne":
      return left != right
    raise ValueError(f"operação não suportada: {op}")

  def _resolve(self, operand: str | None):
    if operand is None:
      return None
    if operand in self.memory:
      return self.memory[operand]
    if operand in {"true", "false"}:
      return operand == "true"
    if operand.startswith('"') and operand.endswith('"'):
      return operand[1:-1]
    try:
      return int(operand)
    except ValueError:
      return operand

  def _truthy(self, value) -> bool:
    return bool(value)

  def _parse_input(self, raw: str, data_type: DataType):
    if data_type == DataType.INTEGER:
      return int(raw)
    if data_type == DataType.BOOLEAN:
      return raw.strip().lower() in {"true", "1", "verdadeiro"}
    return raw

  def _format_output(self, value) -> str:
    if isinstance(value, bool):
      return "true" if value else "false"
    if isinstance(value, str):
      return value
    return str(value)
