"""
Mapeamento dos tokens ANTLR para os tipos/atributos exigidos no enunciado (Projeto I).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from antlr4.Token import Token

from compiler.cte_bounds import validate_cte_value
from generated.SimpleLangLexer import SimpleLangLexer


@dataclass(frozen=True)
class TokenInfo:
  tipo: str
  atributo: Any | None = None

  def format(self) -> str:
    if self.atributo is None:
      return f"<{self.tipo}>"
    return f"<{self.tipo}, {self.atributo}>"


def _truncate_id(name: str) -> str:
  return name[:16] if len(name) > 16 else name


def _parse_cte(text: str) -> int:
  return validate_cte_value(int(text))


def describe_token(token: Token) -> TokenInfo:
  token_type = token.type
  text = token.text or ""

  if token_type == SimpleLangLexer.ID:
    return TokenInfo("ID", _truncate_id(text))

  if token_type == SimpleLangLexer.CTE:
    return TokenInfo("CTE", _parse_cte(text))

  if token_type == SimpleLangLexer.CADEIA:
    return TokenInfo("CADEIA", text[1:-1])

  keyword_map = {
    SimpleLangLexer.PROGRAM: "PROGRAM",
    SimpleLangLexer.INTEGER: "INTEGER",
    SimpleLangLexer.BOOLEAN: "BOOLEAN",
    SimpleLangLexer.BEGIN: "BEGIN",
    SimpleLangLexer.END: "END",
    SimpleLangLexer.WHILE: "WHILE",
    SimpleLangLexer.DO: "DO",
    SimpleLangLexer.READ: "READ",
    SimpleLangLexer.VAR: "VAR",
    SimpleLangLexer.FALSE: "FALSE",
    SimpleLangLexer.TRUE: "TRUE",
    SimpleLangLexer.WRITE: "WRITE",
  }
  if token_type in keyword_map:
    return TokenInfo(keyword_map[token_type])

  op_map: dict[int, tuple[str, str]] = {
    SimpleLangLexer.PLUS: ("OPAD", "MAIS"),
    SimpleLangLexer.MINUS: ("OPAD", "MENOS"),
    SimpleLangLexer.MULT: ("OPMULT", "VEZES"),
    SimpleLangLexer.DIV: ("OPMULT", "DIV"),
    SimpleLangLexer.OR: ("OPLOG", "OR"),
    SimpleLangLexer.AND: ("OPLOG", "AND"),
    SimpleLangLexer.OPNEG: ("OPNEG", "NEG"),
    SimpleLangLexer.LT: ("OPREL", "MENOR"),
    SimpleLangLexer.LE: ("OPREL", "MENIG"),
    SimpleLangLexer.GT: ("OPREL", "MAIOR"),
    SimpleLangLexer.GE: ("OPREL", "MAIG"),
    SimpleLangLexer.EQ: ("OPREL", "IGUAL"),
    SimpleLangLexer.NE: ("OPREL", "DIFER"),
    SimpleLangLexer.PVIG: ("PVIG", None),
    SimpleLangLexer.PONTO: ("PONTO", None),
    SimpleLangLexer.DPONTOS: ("DPONTOS", None),
    SimpleLangLexer.VIG: ("VIG", None),
    SimpleLangLexer.ABPAR: ("ABPAR", None),
    SimpleLangLexer.FPAR: ("FPAR", None),
    SimpleLangLexer.ATRIB: ("ATRIB", None),
  }
  if token_type in op_map:
    tipo, attr = op_map[token_type]
    return TokenInfo(tipo, attr)

  if token_type == SimpleLangLexer.ERR_CHAR:
    raise ValueError(f"caractere inválido '{text}'")

  symbol_names = SimpleLangLexer.symbolicNames
  name = symbol_names[token_type] if token_type < len(symbol_names) else str(token_type)
  return TokenInfo(name, text)
