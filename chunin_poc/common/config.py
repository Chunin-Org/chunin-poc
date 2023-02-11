__all__ = ["Config"]
from pathlib import Path

import toml
from tools import tools

from .profiles import profiles
from .types import ConfigDict


class Config:
    def __init__(self, path_to_config: Path):
        self._config_raw = toml.load(str(path_to_config))
        self.config = self.parse_config()

    def parse_config(self) -> dict:
        config: ConfigDict = self._config_raw["tool"]["chunin"]
        try:
            profile = config.pop("profile")
        except KeyError:
            pass
        else:
            try:
                config = self.__merge_profile_config(config, profiles[profile])
            except KeyError:
                raise KeyError("Invalid profile name!")
        self.__copy_generics(config)
        return config

    def __merge_profile_config(self, config: dict, profile_config: dict):
        if not config:
            return profile_config
        for key, value in profile_config.items():
            if isinstance(value, dict):
                config[key] = self.__merge_profile_config(config.get(key, {}), value)
        return profile_config | config

    @staticmethod
    def __copy_generics(config: ConfigDict):
        config_annotations = ConfigDict.__annotations__
        config_annotations_set = set(config_annotations.keys())
        for tool in tools:
            tool_config_set = set(config_annotations[tool].__annotations__)
            intersects = config_annotations_set & tool_config_set
            for intersection in intersects:
                tool_config = config.setdefault(tool, dict())
                try:
                    tool_config[intersection]
                except KeyError:
                    try:
                        tool_config[intersection] = config[intersection]
                    except KeyError:
                        continue
