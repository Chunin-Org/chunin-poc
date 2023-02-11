from pathlib import Path
from typing import Optional

import typer
from common.config import Config
from common.utils import prepare_tables
from tools import tools

app = typer.Typer()


@app.command()
def lint(
    location: Optional[Path] = typer.Argument(
        Path("."),
        help="Root of project that will be linted recursively",
        file_okay=True,
        dir_okay=True,
        readable=True,
        resolve_path=True,
    ),
    config_path: Optional[Path] = typer.Option(
        Path("./pyproject.toml"),
        "--config",
        "-c",
        help="Path to toml config file",
        file_okay=True,
        dir_okay=False,
        readable=True,
        resolve_path=True,
    ),
):
    config = Config(config_path).config
    prepare_tables(location, config)
    for tool_name, tool_executor_cls in tools.items():
        try:
            tool_config = config[tool_name]
        except KeyError:
            tool_config = {}
        tool_executor = tool_executor_cls(tool_config, location)
        tool_executor.execute()
