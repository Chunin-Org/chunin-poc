__all__ = ["prepare_tables"]
import datetime as dt
import os
import sqlite3
import sys
from base64 import urlsafe_b64encode
from hashlib import sha1
from pathlib import Path

from .types import ConfigDict


def prepare_tables(checks_root: Path, config: ConfigDict):
    db_file = checks_root / ".chunin"
    if db_file.exists():
        if db_file.is_file():
            os.remove(db_file)
        elif db_file.is_dir():
            raise FileExistsError(".chunin is already exists ans it's a directory")
    db_file.touch()

    cx = sqlite3.connect(db_file)
    cu = cx.cursor()

    cu.execute("CREATE TABLE config(version, platform, project_root, date_time, hash)")

    try:
        version = config["py_version"]
    except KeyError:
        _vi = sys.version_info
        version = f"{_vi.major}.{_vi.minor}"
    try:
        platform = config["platform"]
    except KeyError:
        platform = sys.platform

    datetime = dt.datetime.now().isoformat()

    params = (
        version,
        platform,
        str(checks_root),
        datetime,
        _get_hash_from_string(datetime),
    )

    cu.execute("INSERT INTO config VALUES (?, ?, ?, ?, ?)", params)
    cx.commit()

    cu.execute("CREATE TABLE files(abspath, relpath, table_name)")

    excluded = [
        f
        for glob in config.get("exclude", []) + config.get("extend_exclude", [])
        for f in checks_root.rglob(glob)
    ]

    for child in checks_root.rglob("*"):
        if child.suffix == ".py" and all(x not in child.parents for x in excluded):
            rel_path = child.relative_to(checks_root)
            name_hash = _get_hash_from_string(str(rel_path))
            table_name = f"file_{name_hash}_{str(rel_path).replace('/','')}".replace(
                ".", ""
            ).replace("-", "_")
            cu.execute(
                f"CREATE TABLE {table_name}(col_start, row_start, col_end, row_end, error_code, tool, description, link)"
            )
            cu.execute(
                "INSERT INTO files VALUES (?,?,?)",
                (str(child.absolute()), str(rel_path), table_name),
            )
    cx.commit()
    cx.close()


def _get_hash_from_string(string: str) -> str:
    return urlsafe_b64encode(sha1(string.encode()).digest()[:6]).decode()
