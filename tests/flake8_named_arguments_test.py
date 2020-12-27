import ast
from typing import Set

from flake8_named_arguments import Plugin


def _results(string: str) -> Set[str]:
    tree = ast.parse(string)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()
