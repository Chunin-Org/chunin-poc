__all__ = ["Flake8ResultManager"]
from pathlib import Path

from abstract.result_manager import ToolResultManager


class Flake8ResultManager(ToolResultManager):
    def _extract_results(
        self, results: list[tuple[str, list[tuple[str, int, int, str, str]], dict]]
    ):
        for file_meta in results:
            file_name = Path(file_meta[0])
            for d in file_meta[1]:
                yield {
                    "file_name": Path(file_name),
                    "col_start": d[2],
                    "row_start": d[1],
                    "col_end": d[2],
                    "row_end": d[1],
                    "error": d[0],
                    "tool": self.tool,
                    "link": self._generate_link(d[0]),
                    "description": d[3],
                }

    def _generate_link(self, error: str, **kwargs) -> str:
        if error.startswith("F"):
            return "https://flake8.pycqa.org/en/latest/user/error-codes.html#error-violation-codes"
        elif error.startswith("W") or error.startswith("E"):
            return "https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes"
        elif error.startswith("C"):
            return "https://flake8.pycqa.org/en/latest/glossary.html#term-mccabe"
