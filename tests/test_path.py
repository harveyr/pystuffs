from pathlib import Path

import pytest

import pystuffs.path as testee


def test_assert_path_exists_with_str_instance():
    with pytest.raises(testee.PathNotExistError):
        testee.assert_path_exists("/everlasting/gobstoppers")


def test_assert_path_exists_with_path_instance():
    with pytest.raises(testee.PathNotExistError):
        testee.assert_path_exists(Path("/everlasting/gobstoppers"))


def test_unexpand_user_with_path_instance():
    raw = "~/my/test/path.py"
    test_path = Path(raw).expanduser()
    assert str(test_path) != raw
    assert str(test_path).startswith("/")

    result = testee.unexpand_user(test_path)
    assert result == str(raw)
