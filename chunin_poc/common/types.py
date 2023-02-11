__all__ = ["ConfigDict", "Flake8Config", "MyPyConfig", "BanditConfig"]
from typing import Literal, TypedDict

BanditConfig = TypedDict(
    "BanditConfig",
    dict(
        files=list[str],  # targets
        extend_files=list[str],  # targets
        exclude=list[str],  # exclude-dirs
        extend_exclude=list[str],  # exclude-dirs
        ignore=list[str],  # skips
        extend_ignore=list[str],  # skips
        select=list[str],  # tests
        extend_select=list[str],  # tests
    ),
    total=False,
)


MyPyConfig = TypedDict(
    "MyPyConfig",
    dict(
        py_version=str,  # python-version
        exclude=list[str],
        extend_exclude=list[str],
        ignore=list[str],  # disable-error-codes
        extend_ignore=list[str],  # disable-error-codes
        select=list[str],  # enable-error-codes
        extend_select=list[str],  # enable-error-codes
        platform=Literal[
            "aix", "emscripten", "linux", "wasi", "win32", "cygwin", "darwin"
        ],
        no_namespace_packages=bool,
        explicit_packages_bases=bool,
        ignore_missing_imports=bool,
        follow_imports=Literal["normal", "silent", "skip", "error"],
        follow_imports_for_stubs=bool,
        no_site_packages=bool,
        no_silence_site_packages=bool,
        always_ture=list[str],
        always_false=list[str],
        disallow_any_unimported=bool,
        disallow_any_expr=bool,
        disallow_any_decorated=bool,
        disallow_any_explicit=bool,
        disallow_any_generics=bool,
        disallow_subclassing_any=bool,
        disallow_untyped_calls=bool,
        disallow_untyped_defs=bool,
        disallow_incomplete_defs=bool,
        check_untyped_defs=bool,
        disallow_untyped_decorators=bool,
        implicit_optional=bool,
        strict_optional=bool,
        warn_redundant_casts=bool,
        warn_unused_ignores=bool,
        warn_no_return=bool,
        warn_return_any=bool,
        warn_unreachable=bool,
        ignore_errors=bool,
        allow_untyped_globals=bool,
        allow_redefinition=bool,
        local_partial_types=bool,
        implicit_reexport=bool,
        strict_concatenate=bool,
        strict_equality=bool,
        strict=bool,
        _python_executable=str,
        _show_error_context=bool,
        _show_column_numbers=bool,
        _hide_error_codes=bool,
        _pretty=bool,
        _color_output=bool,
        _error_summary=bool,
        _show_absolute_path=bool,
        _incremental=bool,
        _cache_dir=str,
        _sqlite_cache=bool,
        _cache_fine_grained=bool,
        _skip_version_check=bool,
        _skip_cache_mtime_checks=bool,
        _pdb=bool,
        _show_traceback=bool,
        _raise_exceptions=bool,
        _custom_typing_module=str,
        _custom_typeshed_dir=str,
        _warn_incomplete_stub=bool,
    ),
    total=False,
)


Flake8Config = TypedDict(
    "Flake8Config",
    dict(
        verbosity=int,  # -3 = -qqq; 3 = -vvv
        exclude=list[str],
        extend_exclude=list[str],
        files=list[str],  # filename
        hang_closing=bool,
        ignore=list[str],
        extend_ignore=list[str],
        max_line_length=int,
        max_doc_length=int,
        indent_size=int,
        select=list[str],
        extend_select=list[str],
        disable_ignore_comments=bool,  # disable-noqa
        require_plugins=list[str],
        plugins=list[str],  # enable_extensions
        console_redirect=bool,  # tee
        doctests=bool,
        max_complexity=int,
        _count=bool,
        _format=str,
        _per_file_ignore=list[str],
        _statistics=bool,
        _exit_zero=bool,
        _jobs=int,
        _output_file=str,
        _include_in_doctest=list[str],
        _exclude_from_doctest=list[str],
        _benchmark=bool,
        _bug_report=bool,
    ),
    total=False,
)

ConfigDict = TypedDict(
    "ConfigDict",
    dict(
        max_line_length=int,
        py_version=str,
        verbosity=int,
        files=list[str],
        extend_files=list[str],
        exclude=list[str],
        extend_exclude=list[str],
        disable_ignore_comments=bool,
        console_redirect=bool,
        platform=Literal[
            "aix", "emscripten", "linux", "wasi", "win32", "cygwin", "darwin"
        ],
        flake8=Flake8Config,
        mypy=MyPyConfig,
        bandit=BanditConfig,
    ),
    total=False,
)
