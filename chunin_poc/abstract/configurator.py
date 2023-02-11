__all__ = ["ToolConfigurator", "ArgvToolConfigurator"]
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Generator

from chunin_poc.common.types import BanditConfig, Flake8Config, MyPyConfig


class ToolConfigurator(ABC):
    def __init__(self, config: MyPyConfig | BanditConfig | Flake8Config, root: Path):
        self.config = config
        self.root = root

    @abstractmethod
    def convert(self) -> Any:
        ...


class ArgvToolConfigurator(ToolConfigurator, ABC):
    _additional_configuration: list[str]
    mapper: dict[str, str]

    def __init__(self, config: MyPyConfig | BanditConfig | Flake8Config, root: Path):
        self.additional_config = list(self._additional_configuration)
        super().__init__(config, root)

    def convert(self) -> list[str]:
        self._concat_extend()
        self._reduce_leading_underscore()
        self._remap_names()
        results = list(self.generate_args())
        results.extend(self.additional_config)
        return [str(self.root.absolute())] + results

    def generate_args(self) -> Generator[list[str], None, None]:
        for key, value in self.config.items():
            arg_key = f"--{key.replace('_', '-')}"
            if isinstance(value, bool) and value:
                yield arg_key
            elif isinstance(value, list):
                yield from self._convert_list(arg_key, value)
            else:
                yield from (arg_key, value)

    def _concat_extend(self):
        for key in tuple(self.config.keys()):
            if key.startswith("extend"):
                pair_key = key.replace("extend_", "")
                try:
                    self.config[pair_key] += self.config.pop(key)
                except KeyError:
                    self.config[pair_key] = self.config.pop(key)

    def _reduce_leading_underscore(self):
        for key in tuple(self.config.keys()):
            if key.startswith("_"):
                self.config[key[1:]] = self.config.pop(key)

    def _remap_names(self):
        for config_key, original_key in self.mapper.items():
            try:
                self.config[original_key] = self.config.pop(config_key)
            except KeyError:
                continue

    @abstractmethod
    def _convert_list(self, arg_key: str, value: list[str]) -> list[str]:
        ...
