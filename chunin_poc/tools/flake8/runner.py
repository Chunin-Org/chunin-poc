__all__ = ["Flake8Runner"]
from abstract.runner import ToolRunner
from flake8.main import application


class Flake8Runner(ToolRunner):
    def run(
        self, config: list[str]
    ) -> list[tuple[str, list[tuple[str, int, int, str, str]], dict]]:
        app = application.Application()
        app.initialize(config)
        app.run_checks()
        return app.file_checker_manager.results
