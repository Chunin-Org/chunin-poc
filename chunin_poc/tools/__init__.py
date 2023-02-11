__all__ = ["tools"]
from typing import Type

from chunin_poc.abstract.executor import ToolExecutor

from .bandit.executor import BanditExecutor
from .flake8.executor import Flake8Executor
from .mypy.executor import MyPyExecutor

tools: dict[str, Type[ToolExecutor]] = {
    "flake8": Flake8Executor,
    "mypy": MyPyExecutor,
    "bandit": BanditExecutor,
}
