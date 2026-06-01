"""Limites de constantes inteiras (CTE): 2 bytes sem sinal (0..65535)."""

from __future__ import annotations

CTE_MIN = 0
CTE_MAX = 65535


def validate_cte_value(value: int) -> int:
  if value < CTE_MIN or value > CTE_MAX:
    raise ValueError(
      f"Fora do intervalo de 2 bytes sem sinal ({CTE_MIN} a {CTE_MAX})",
    )
  return value
