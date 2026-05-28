"""Fase sintática: construção da árvore de parse."""

from __future__ import annotations

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from compiler.errors import SyntaxError
from generated.SimpleLangLexer import SimpleLangLexer
from generated.SimpleLangParser import SimpleLangParser


class _SyntaxErrorListener(ErrorListener):
  def syntaxError(self, recognizer, offending_symbol, line, column, msg, exc):
    raise SyntaxError(f"Erro sintático: {msg}", line=line, column=column + 1)


def build_parse_tree(source: str) -> SimpleLangParser.ProgramContext:
  input_stream = InputStream(source)
  lexer = SimpleLangLexer(input_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleLangParser(tokens)
  parser.removeErrorListeners()
  parser.addErrorListener(_SyntaxErrorListener())
  return parser.program()
