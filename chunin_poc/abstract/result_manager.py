__all__ = ["ToolResultManager"]
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Generator, Literal, TypedDict


class Result(TypedDict):
    file_name: Path
    col_start: int
    row_start: int
    col_end: int | None
    row_end: int | None
    error: str
    tool: Literal["mypy", "flake8", "bandit"]
    link: str
    description: str


class ToolResultManager(ABC):
    def __init__(self, root: Path, tool: Literal["mypy", "flake8", "bandit"]):
        self.root = root
        self.tool = tool
        self.cx = sqlite3.connect(root / ".chunin")
        self.cu = self.cx.cursor()

    def save(self, raw_results: Any) -> list[Result]:
        results = list(self._extract_results(raw_results))
        for result in results:
            table_name = self._get_table_name(str(result["file_name"]))
            values = self._extract_values(result)
            self._insert_values(table_name, values)
        self.cx.commit()
        self.cx.close()
        return results

    @abstractmethod
    def _extract_results(self, results: Any) -> Generator[Result, None, None]:
        ...

    def _extract_values(
        self, result: Result
    ) -> tuple[int, int, int, int, str, str, str, str]:
        return (
            result["col_start"],
            result["row_start"],
            result["col_end"] if result["col_end"] is not None else result["col_start"],
            result["row_end"] if result["row_end"] is not None else result["row_start"],
            result["error"],
            self.tool,
            result["description"],
            result["link"],
        )

    def _get_table_name(self, file_path: str) -> str:
        file_path = Path(file_path)
        if not file_path.is_absolute():
            file_path = file_path.absolute()
        r = self.cu.execute(
            f"SELECT table_name FROM files WHERE abspath=?", (str(file_path),)
        )
        return r.fetchone()[0]

    def _insert_values(
        self, table_name: str, values: tuple[int, int, int, int, str, str, str, str]
    ):
        self.cu.execute(
            f"INSERT INTO {table_name} values (?, ?, ?, ?, ?, ?, ?, ?)", values
        )

    @abstractmethod
    def _generate_link(self, error: str, **kwargs) -> str:
        ...
