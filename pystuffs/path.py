from pathlib import Path


class PathNotExistError(Exception):
    def __init__(self, path: Path | str):
        self.message = f"Path does not exist: {path}"
        super().__init__(self.message)


def assert_path_exists(path: Path | str):
    if isinstance(path, str):
        path = Path(path)

    if not path.exists():
        raise PathNotExistError(path)


def unexpand_user(path: Path | str) -> str:
    return str(path).replace(str(Path.home()), "~", 1)
