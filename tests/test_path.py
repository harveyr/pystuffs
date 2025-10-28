from pathlib import Path

from pystuffs.path import unexpand_user


def test_unexpand_user_with_path_instance():
    raw = "~/my/test/path.py"
    test_path = Path(raw).expanduser()
    assert str(test_path) != raw
    assert str(test_path).startswith("/")

    result = unexpand_user(test_path)
    assert result == str(raw)
