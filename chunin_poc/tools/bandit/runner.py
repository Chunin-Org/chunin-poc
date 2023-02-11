__all__ = ["BanditRunner"]
from chunin_poc.abstract.runner import ToolRunner
from bandit.core.manager import BanditManager


class BanditRunner(ToolRunner):
    def run(self, config):
        b_mng = BanditManager(
            config["config"], "file", False, profile=config["profile"], quiet=True
        )

        b_mng.discover_files(config["target"], True)
        b_mng.run_tests()
        return b_mng.results
