#!/usr/bin/env python3
"""Ponto de entrada do compilador SimpleLang."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Permite executar a partir da raiz do projeto: python src/main.py
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
  sys.path.insert(0, str(ROOT))

from compiler.lexer_phase import print_tokens
from compiler.pipeline import compile_file, compile_source, print_quads


def _read_source(path: Path | None) -> str:
  if path:
    return path.read_text(encoding="utf-8")
  return sys.stdin.read()


def main() -> int:
  parser = argparse.ArgumentParser(
    description="Compilador da linguagem SimpleLang (LF&C — Projeto I)",
  )
  parser.add_argument("arquivo", nargs="?", help="Arquivo-fonte (.txt)")
  parser.add_argument(
    "--fase",
    choices=["lex", "full"],
    default="full",
    help="lex = apenas tokens; full = pipeline completo",
  )
  parser.add_argument(
    "--executar",
    action="store_true",
    help="Interpreta o programa após gerar quádruplos",
  )
  parser.add_argument(
    "--arvore-png",
    nargs="?",
    const="",
    default=None,
    metavar="CAMINHO",
    help="Grava a árvore sintática em PNG (padrão: <arquivo>.arvore.png ao lado do fonte)",
  )
  args = parser.parse_args()

  path = Path(args.arquivo) if args.arquivo else None
  source = _read_source(path)

  if args.fase == "lex":
    from compiler.pipeline import compile_source

    result = compile_source(source, phase="lex")
    if "error" in result:
      print(result["error"], file=sys.stderr)
      return 1
    print_tokens(result["tokens"])
    return 0

  tree_png: Path | None = None
  if args.arvore_png is not None:
    tree_png = Path(args.arvore_png) if args.arvore_png else None

  if path:
    result = compile_file(path, phase="full", run_program=False, parse_tree_image=tree_png)
  else:
    result = compile_source(
      source,
      phase="full",
      run_program=False,
      parse_tree_image=tree_png,
    )

  if "error" in result:
    print(result["error"], file=sys.stderr)
    return 1

  print("=== Análise léxica (tokens) ===")
  print_tokens(result["tokens"])

  if "parse_tree_image" in result:
    print(f"\n=== Análise sintática (árvore) ===")
    print(f"Imagem gravada em: {result['parse_tree_image']}")

  print("\n=== Análise semântica (símbolos) ===")
  for symbol in result["symbols"]:
    print(f"- {symbol['name']}: {symbol['type']}")

  print("\n=== Código intermediário (quádruplos) ===")
  print_quads(result["quads"])

  if args.executar:
    print("\n=== Execução ===")
    from compiler.codegen.interpreter import QuadrupleInterpreter

    QuadrupleInterpreter(result["quads"], result["symbol_table"]).run()

  return 0


if __name__ == "__main__":
  raise SystemExit(main())
