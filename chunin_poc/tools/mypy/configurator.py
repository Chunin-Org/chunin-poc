__all__ = ["MyPyConfigurator"]
from abstract.configurator import ArgvToolConfigurator


class MyPyConfigurator(ArgvToolConfigurator):
    mapper = {
        "py_version": "python_version",
        "ignore": "disable_error_code",
        "select": "enable_error_code",
    }
    _additional_configuration = ["--show-column-numbers"]

    def _convert_list(self, arg_key: str, value: list[str]) -> list[str]:
        result = []
        for v in value:
            result.extend((arg_key, v))
        return result
