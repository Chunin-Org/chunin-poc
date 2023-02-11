__all__ = ["MyPyRunner"]
from chunin_poc.abstract.runner import ToolRunner
from mypy import api


class MyPyRunner(ToolRunner):
    def run(self, config: list[str]) -> list[str]:
        result = api.run(config)
        return result[0].splitlines()
