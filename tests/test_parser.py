import pytest

from gendiff.scripts.parser import parse_file


def test_parse_file_supports_json_and_yaml(test_data_dir):
    assert parse_file(test_data_dir / "file1.json") == {
        "follow": False,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
        "timeout": 50,
    }
    assert parse_file(test_data_dir / "file1.yml") == {
        "follow": False,
        "host": "hexlet.io",
        "proxy": "123.234.53.22",
        "timeout": 50,
    }


def test_parse_file_raises_for_unsupported_extension(test_data_dir):
    invalid_file = test_data_dir / "invalid.txt"

    with pytest.raises(ValueError, match="Unsupported file format"):
        parse_file(invalid_file)
