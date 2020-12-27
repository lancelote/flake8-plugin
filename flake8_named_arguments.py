import ast
import sys
from typing import Generator, Tuple, Type, Any

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata

ErrLineNum = int
CharOffset = int
Message = str


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[ErrLineNum, CharOffset, Message, Type[Any]], None, None]:
        yield 1, 0, 'FNA100 named argument', type(self)
