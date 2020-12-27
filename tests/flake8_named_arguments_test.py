import ast
from typing import Set

from flake8_named_arguments import Plugin


def _results(string: str) -> Set[str]:
    tree = ast.parse(string)
    plugin = Plugin(tree)
    return {f"{line}:{col + 1} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()


def test_incorrect_named_arguments():
    ret = _results("f(**{'foo': 'bar'})")
    assert ret == {"1:1 FNA100 all args in ** are identifiers"}


def test_allowed_splat_arguments():
    assert _results("f(**{'foo-bar': 'baz'})") == set()
