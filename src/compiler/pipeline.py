"""Orquestra as fases do compilador."""

from __future__ import annotations

from pathlib import Path

from compiler.codegen.generator import CodeGenerator
from compiler.codegen.interpreter import QuadrupleInterpreter
from compiler.codegen.quad import Quadruple
from compiler.errors import CompilerError
from compiler.lexer_phase import print_tokens, run_lexer
from compiler.parser_phase import build_parse_tree
from compiler.semantic.analyzer import SemanticAnalyzer


def compile_source(
  source: str,
  *,
  phase: str = "full",
  run_program: bool = False,
) -> dict:
  result: dict = {"phase": phase}

  try:
    if phase in {"lex", "full"}:
      tokens = run_lexer(source)
      result["tokens"] = tokens
      if phase == "lex":
        return result

    tree = build_parse_tree(source)
    result["parse"] = "ok"

    analyzer = SemanticAnalyzer()
    symbol_table = analyzer.visit(tree)
    result["semantic"] = "ok"
    result["symbols"] = [
      {"name": s.name, "type": s.data_type.value} for s in symbol_table.items()
    ]
    result["symbol_table"] = symbol_table

    generator = CodeGenerator(symbol_table)
    quads = generator.visit(tree)
    result["quads"] = quads

    if run_program:
      QuadrupleInterpreter(quads, symbol_table).run()

    return result
  except CompilerError as err:
    result["error"] = str(err)
    return result


def compile_file(
  path: Path,
  *,
  phase: str = "full",
  run_program: bool = False,
) -> dict:
  source = path.read_text(encoding="utf-8")
  return compile_source(source, phase=phase, run_program=run_program)


def print_quads(quads: list[Quadruple]) -> None:
  for index, quad in enumerate(quads, start=1):
    print(f"{index:03d} {quad}")
