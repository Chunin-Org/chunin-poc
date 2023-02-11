__all__ = ["ToolRunner"]
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class ToolRunner(ABC):
    def __init__(self, root: Path):
        self.root = root

    @abstractmethod
    def run(self, config: Any) -> Any:
        ...
