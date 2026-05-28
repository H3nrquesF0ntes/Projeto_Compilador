from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Quadruple:
  op: str
  arg1: str | None
  arg2: str | None
  result: str | None

  def __str__(self) -> str:
    return f"({self.op}, {self.arg1}, {self.arg2}, {self.result})"
