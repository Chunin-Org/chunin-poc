__all__ = ["BanditExecutor"]
from abstract.executor import ToolExecutor

from .configuratot import BanditConfigurator
from .result_manager import BanditResultManager
from .runner import BanditRunner


class BanditExecutor(ToolExecutor):
    _configurator = BanditConfigurator
    _runner = BanditRunner
    _result_manager = BanditResultManager
    _tool = "bandit"
