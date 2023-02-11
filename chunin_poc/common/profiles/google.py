__all__ = ["profile"]

from common.types import ConfigDict

profile: ConfigDict = {
    "max_line_length": 88,
    "exclude": ["build/lib"],
    "flake8": {
        "inline_quotes": '"',  # type: ignore[typeddict-unknown-key]
        "ignore": [
            "E203",
            "W503",
            "E501",
            # Missing doc strings.
            "D100",
            "D101",
            "D103",
            "D104",
            "D105",
            "D107",
            "D102",
            # Warning: First line should be in imperative mood.
            # This is the opposite of the Google style.
            "D401",
            # Missing trailing comma.
            "C812",
            # Allow unindexed string format parameters
            "P101",
            "P102",
            "P103",
        ],
        "plugins": [
            "flake8-breakpoint",
            "flake8-broken-line",
            "flake8-bugbear",
            "flake8-builtins",
            "flake8-coding",
            "flake8-comprehensions",
            "flake8-commas",
            "flake8-debugger",
            "flake8-docstrings",
            "flake8-isort",
            "flake8-logging-format",
            "flake8-mock",
            "flake8-mutable",
            "flake8-pep3101",
            "flake8-print",
            "flake8-quotes",
            "flake8-spellcheck",
            "flake8-string-format",
            "flake8-type-annotations",
            "flake8-variables-names",
        ],
    },
    "mypy": {
        "ignore": ["attr-defined"],
        "implicit_optional": False,
    },
    "bandit": {
        "ignore": [
            # Audit url open for permitted schemes.
            "B310",
            # Standard pseudo-random generators are not suitable for security/cryptographic purposes.
            "B311",
            # Use of subprocess call and run.
            "B404",
            "B603",
            "B101",
            # Consider possible security implications associated with pickle module
            "B403",
            # Pickle and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue.
            "B301",
        ]
    },
}
