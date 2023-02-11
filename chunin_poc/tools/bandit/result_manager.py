__all__ = ["BanditResultManager"]
from pathlib import Path

from chunin_poc.abstract.result_manager import ToolResultManager
from bandit import __version__


class BanditResultManager(ToolResultManager):
    link_pattern = "https://bandit.readthedocs.io/en/{version}/plugins/{id}_{name}.html"

    def _extract_results(self, results):
        for result in results:
            yield {
                "file_name": Path(result.fname),
                "col_start": result.col_offset,
                "row_start": result.lineno,
                "col_end": result.col_offset,
                "row_end": result.linerange[-1],
                "error": result.test_id,
                "tool": self.tool,
                "link": self._generate_link(result.test_id, test_name=result.test),
                "description": result.text,
            }

    def _generate_link(self, error, **kwargs):
        return self.link_pattern.format(
            version=__version__, id=error.lower(), name=kwargs["test_name"].lower()
        )
