__all__ = ["MyPyResultManager"]
import re

from chunin_poc.abstract.result_manager import ToolResultManager
from mypy.version import __version__


class MyPyResultManager(ToolResultManager):
    regex_pattern = re.compile(
        r"(?P<file_name>[a-zA-Z0-9_\./]+):(?P<row_start>\d+):(?P<col_start>\d+): (?P<description>.+) \[(?P<error>[\w-]+)\]"
    )
    link_pattern = "https://mypy.readthedocs.io/en/{}/{}.html#{}"

    _optional_link = {
        "type-arg",
        "no-untyped-def",
        "redundant-cast",
        "redundant-self",
        "comparison-overlap",
        "no-untyped-call",
        "no-any-return",
        "no-any-unimported",
        "unreachable",
        "redundant-expr",
        "truthy-bool",
        "truthy-iterable",
        "ignore-without-code",
        "unused-awaitable",
    }

    def _extract_results(self, results: list[str]):
        for string in results:
            try:
                match = self.regex_pattern.match(string).groupdict()
            except AttributeError:
                continue

            match["col_end"] = match["col_start"]
            match["row_end"] = match["row_start"]
            match["tool"] = self.tool
            match["link"] = self._generate_link(match["error"])

            yield match

    def _generate_link(self, error: str, **kwargs) -> str:
        if error not in self._optional_link:
            page = "error_code_list"
        else:
            page = "error_code_list2"
        return self.link_pattern.format(__version__, page, error)
