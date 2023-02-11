__all__ = ["Flake8Configurator"]
from abstract.configurator import ArgvToolConfigurator


class Flake8Configurator(ArgvToolConfigurator):
    mapper = {
        "files": "filename",
        "disable_ignore_comments": "disable_noqa",
        "plugins": "enable_extensions",
        "console_redirect": "tee",
    }
    _additional_configuration = []

    def _convert_list(self, arg_key: str, value: list[str]) -> list[str]:
        return [arg_key, ",".join(value)]
