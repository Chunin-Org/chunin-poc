__all__ = ["MyPyExecutor"]
from abstract.executor import ToolExecutor
from tools.mypy.configurator import MyPyConfigurator
from tools.mypy.result_manager import MyPyResultManager
from tools.mypy.runner import MyPyRunner


class MyPyExecutor(ToolExecutor):
    _configurator = MyPyConfigurator
    _runner = MyPyRunner
    _result_manager = MyPyResultManager
    _tool = "mypy"
