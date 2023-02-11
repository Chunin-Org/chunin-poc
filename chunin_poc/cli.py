import sys
from pathlib import Path
from typing import Optional

import typer
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn
from .common.config import Config
from .common.utils import prepare_tables
from .tools import tools

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
    verbose: Optional[bool] = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show output in console"
    )
):
    """
    Lint provided directory with Flake8, MyPy and Bandit.

    To display report at console run add -v flag.
    """
    xcode = 0
    with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
    ) as progress:
        _main_task = progress.add_task("[cyan]:nerd_face: Linting  ", total=5)
        progress.console.print(":wrench: [italic]Reading Config file...[/italic]", emoji=True)
        config = Config(config_path).config
        progress.advance(_main_task)
        progress.console.print(":memo: [italic]Preparing report database...[/italic]", emoji=True)
        prepare_tables(location, config)
        progress.advance(_main_task)

        for tool_name, tool_executor_cls in tools.items():
            progress.console.print(f"[yellow]:zap: Running [bold]{tool_name}[/bold][/yellow]", emoji=True)
            try:
                tool_config = config[tool_name]
            except KeyError:
                tool_config = {}
            tool_executor = tool_executor_cls(tool_config, location)
            errors, tool_success, results = tool_executor.execute()
            if not tool_success:
                if errors > 1:
                    er = "errors"
                else:
                    er = "error"
                progress.console.print(f":x: [blue]{tool_name.capitalize()} finished![/blue] "
                                       f"[bold red]{errors} {er} found[/bold red] :anguished:", emoji=True)
                xcode = 1
            else:
                progress.console.print(f":white_check_mark: [blue]{tool_name.capitalize()} finished![/blue] "
                                       f"[bold green]No errors found[/bold green] :sparkles:", emoji=True)
            progress.advance(_main_task)
    sys.exit(xcode)
