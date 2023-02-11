__all__ = ["BanditConfigurator"]
from chunin_poc.abstract.configurator import ToolConfigurator
from bandit.core.config import BanditConfig


class BanditConfigurator(ToolConfigurator):
    def convert(self) -> dict:
        include = self.config.get("files", []) + self.config.get("extend_files", [])
        profile = {
            "include": set(
                self.config.get("select", []) + self.config.get("extend_select", [])
            ),
            "exclude": set(
                self.config.get("ignore", []) + self.config.get("extend_ignore", [])
            ),
        }
        conf_dict = {
            "plugin_name_pattern": "*.py",
            "include": include if include else ["*.py"],
        }
        config = BanditConfig()
        config._config = conf_dict
        return {
            "config": config,
            "target": [str(self.root)],
            "exclude": ",".join(
                self.config.get("exclude", []) + self.config.get("extend_exclude", [])
            ),
            "profile": profile if any(profile.values()) else None,
        }
