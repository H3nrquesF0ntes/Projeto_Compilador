from __future__ import annotations

from dataclasses import dataclass

from compiler.semantic.types import DataType


@dataclass
class Symbol:
  name: str
  data_type: DataType


class SymbolTable:
  def __init__(self) -> None:
    self._symbols: dict[str, Symbol] = {}

  def declare(self, name: str, data_type: DataType) -> None:
    key = name.lower()
    if key in self._symbols:
      raise ValueError(f"identificador '{name}' já declarado")
    self._symbols[key] = Symbol(name=name, data_type=data_type)

  def lookup(self, name: str) -> Symbol:
    key = name.lower()
    if key not in self._symbols:
      raise ValueError(f"identificador '{name}' não declarado")
    return self._symbols[key]

  def items(self) -> list[Symbol]:
    return list(self._symbols.values())
