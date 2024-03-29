__all__ = ["ToolExecutor"]
from abc import ABC
from pathlib import Path
from typing import Literal, Type

from chunin_poc.common.types import BanditConfig, Flake8Config, MyPyConfig

from .configurator import ToolConfigurator
from .result_manager import ToolResultManager, Result
from .runner import ToolRunner


class ToolExecutor(ABC):
    _configurator: Type[ToolConfigurator]
    _runner: Type[ToolRunner]
    _result_manager: Type[ToolResultManager]
    _tool: Literal["mypy", "flake8", "bandit"]

    def __init__(self, config: MyPyConfig | BanditConfig | Flake8Config, root: Path):
        self.configurator = self._configurator(config, root)
        self.runner = self._runner(root)
        self.result_manager = self._result_manager(root, self._tool)
        self.root = root

    def execute(self) -> tuple[int, bool, list[Result]]:
        tool_config = self.configurator.convert()
        results = self.runner.run(tool_config)
        final = self.result_manager.save(results)
        return len(final), not bool(final), final
