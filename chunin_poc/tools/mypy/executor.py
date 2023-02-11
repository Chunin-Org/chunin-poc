__all__ = ["MyPyExecutor"]
from chunin_poc.abstract.executor import ToolExecutor
from .configurator import MyPyConfigurator
from .result_manager import MyPyResultManager
from .runner import MyPyRunner


class MyPyExecutor(ToolExecutor):
    _configurator = MyPyConfigurator
    _runner = MyPyRunner
    _result_manager = MyPyResultManager
    _tool = "mypy"
