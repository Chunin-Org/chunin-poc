__all__ = ["Flake8Executor"]
from abstract.executor import ToolExecutor

from .configurator import Flake8Configurator
from .result_manager import Flake8ResultManager
from .runner import Flake8Runner


class Flake8Executor(ToolExecutor):
    _configurator = Flake8Configurator
    _runner = Flake8Runner
    _result_manager = Flake8ResultManager
    _tool = "flake8"
