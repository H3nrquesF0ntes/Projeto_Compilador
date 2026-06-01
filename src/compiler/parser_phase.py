"""Fase sintática: construção da árvore de parse."""

from __future__ import annotations

from dataclasses import dataclass

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from compiler.errors import SyntaxError
from generated.SimpleLangLexer import SimpleLangLexer
from generated.SimpleLangParser import SimpleLangParser


class _SyntaxErrorListener(ErrorListener):
  def syntaxError(self, recognizer, offending_symbol, line, column, msg, exc):
    raise SyntaxError(f"Erro sintático: {msg}", line=line, column=column + 1)


@dataclass(frozen=True)
class ParseResult:
  tree: SimpleLangParser.ProgramContext
  parser: SimpleLangParser


def build_parse_tree(source: str) -> ParseResult:
  input_stream = InputStream(source)
  lexer = SimpleLangLexer(input_stream)
  tokens = CommonTokenStream(lexer)
  parser = SimpleLangParser(tokens)
  parser.removeErrorListeners()
  parser.addErrorListener(_SyntaxErrorListener())
  tree = parser.program()
  return ParseResult(tree=tree, parser=parser)


def format_parse_tree(parse: ParseResult) -> str:
  return parse.tree.toStringTree(recog=parse.parser)


def print_parse_tree(parse_tree_text: str) -> None:
  print(parse_tree_text)
