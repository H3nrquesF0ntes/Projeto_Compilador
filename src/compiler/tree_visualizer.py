"""Gera imagem PNG da árvore sintática (parse tree) do ANTLR."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from antlr4.tree.Tree import TerminalNode
from matplotlib.patches import FancyBboxPatch

from compiler.parser_phase import ParseResult
from generated.SimpleLangParser import SimpleLangParser


def _node_label(node, parser: SimpleLangParser) -> str:
  if isinstance(node, TerminalNode):
    text = node.getText()
    if text == "<EOF>":
      return "EOF"
    return text.replace("\n", "\\n")
  rule_index = node.getRuleIndex()
  if rule_index >= 0:
    return parser.ruleNames[rule_index]
  return "?"


def _build_layout(parse: ParseResult) -> tuple[dict, list[tuple[int, int]]]:
  layout: dict = {}
  edges: list[tuple[int, int]] = []
  counter = [0, 0]  # [next_node_id, next_leaf_x]

  def walk(node, parser: SimpleLangParser, depth: int, parent_id: int | None) -> tuple[int, float]:
    node_id = counter[0]
    counter[0] += 1
    if parent_id is not None:
      edges.append((parent_id, node_id))

    child_count = node.getChildCount()
    if child_count == 0:
      x = float(counter[1])
      counter[1] += 1.0
    else:
      xs: list[float] = []
      for index in range(child_count):
        _, child_x = walk(node.getChild(index), parser, depth + 1, node_id)
        xs.append(child_x)
      x = sum(xs) / len(xs)

    label = _node_label(node, parser)
    if len(label) > 24:
      label = label[:21] + "..."
    layout[node_id] = {"label": label, "x": x, "y": -float(depth)}
    return node_id, x

  walk(parse.tree, parse.parser, 0, None)
  return layout, edges


def save_parse_tree_png(parse: ParseResult, output_path: Path) -> Path:
  """Renderiza a árvore em PNG e retorna o caminho gravado."""
  layout, edges = _build_layout(parse)
  if not layout:
    raise ValueError("árvore sintática vazia")

  xs = [info["x"] for info in layout.values()]
  ys = [info["y"] for info in layout.values()]
  width = max(8.0, (max(xs) - min(xs) + 1) * 1.4)
  height = max(6.0, (max(ys) - min(ys) + 2) * 1.2)

  fig, ax = plt.subplots(figsize=(width, height))
  ax.set_axis_off()

  x_min, x_max = min(xs), max(xs)
  y_min, y_max = min(ys), max(ys)
  margin_x = 0.6
  margin_y = 0.5
  ax.set_xlim(x_min - margin_x, x_max + margin_x)
  ax.set_ylim(y_min - margin_y, y_max + margin_y)

  for parent_id, child_id in edges:
    parent = layout[parent_id]
    child = layout[child_id]
    ax.plot(
      [parent["x"], child["x"]],
      [parent["y"], child["y"]],
      color="#555555",
      linewidth=1.0,
      zorder=1,
    )

  for info in layout.values():
    box = FancyBboxPatch(
      (info["x"] - 0.35, info["y"] - 0.18),
      0.7,
      0.36,
      boxstyle="round,pad=0.02",
      linewidth=1.0,
      edgecolor="#2c5282",
      facecolor="#ebf4ff",
      zorder=2,
    )
    ax.add_patch(box)
    ax.text(
      info["x"],
      info["y"],
      info["label"],
      ha="center",
      va="center",
      fontsize=7,
      family="monospace",
      zorder=3,
    )

  output_path = Path(output_path)
  output_path.parent.mkdir(parents=True, exist_ok=True)
  fig.tight_layout(pad=0.5)
  fig.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="white")
  plt.close(fig)
  return output_path.resolve()


def default_tree_image_path(source_path: Path | None) -> Path | None:
  """`programa.txt` → `programa.arvore.png`; stdin sem arquivo → None."""
  if source_path is None:
    return None
  return source_path.with_name(f"{source_path.stem}.arvore.png")
