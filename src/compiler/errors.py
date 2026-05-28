"""Erros centralizados do compilador."""


class CompilerError(Exception):
  def __init__(self, message: str, line: int | None = None, column: int | None = None):
    self.line = line
    self.column = column
    loc = ""
    if line is not None:
      loc = f" (linha {line}"
      if column is not None:
        loc += f", coluna {column}"
      loc += ")"
    super().__init__(f"{message}{loc}")


class LexicalError(CompilerError):
  pass


class SyntaxError(CompilerError):
  pass


class SemanticError(CompilerError):
  pass
