from pathlib import Path


def unexpand_user(path: Path | str) -> str:
    return str(path).replace(str(Path.home()), "~", 1)
