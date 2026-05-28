"""Fase léxica: tokenização e impressão conforme o enunciado."""

from __future__ import annotations

from antlr4 import InputStream
from antlr4.error.ErrorListener import ErrorListener

from compiler.errors import LexicalError
from compiler.token_catalog import TokenInfo, describe_token
from generated.SimpleLangLexer import SimpleLangLexer


class _LexicalErrorListener(ErrorListener):
  def syntaxError(self, recognizer, offending_symbol, line, column, msg, exc):
    raise LexicalError(
      f"Erro léxico: caractere inválido '{offending_symbol.text}'",
      line=line,
      column=column + 1,
    )


def run_lexer(source: str) -> list[TokenInfo]:
  """Executa apenas a análise léxica e retorna a lista de tokens do enunciado."""
  input_stream = InputStream(source)
  lexer = SimpleLangLexer(input_stream)
  lexer.removeErrorListeners()
  lexer.addErrorListener(_LexicalErrorListener())

  tokens: list[TokenInfo] = []
  while True:
    token = lexer.nextToken()
    if token.type == -1:  # EOF
      break
    try:
      info = describe_token(token)
    except ValueError as err:
      raise LexicalError(str(err), line=token.line, column=token.column + 1) from err
    tokens.append(info)
  return tokens


def print_tokens(tokens: list[TokenInfo]) -> None:
  for info in tokens:
    print(info.format())
