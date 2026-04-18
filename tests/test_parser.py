import pytest

from gendiff.scripts.parser import parse_file


def test_parse_file_supports_json(test_data_dir):
    assert parse_file(test_data_dir / "file1.json") == {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": "",
                },
            },
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value",
            },
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45,
            },
        },
    }


def test_parse_file_supports_yaml(test_data_dir):
    assert parse_file(test_data_dir / "file1.yml") == {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": "",
                },
            },
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value",
            },
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45,
            },
        },
    }


def test_parse_file_raises_for_unsupported_extension(test_data_dir):
    invalid_file = test_data_dir / "invalid.txt"

    with pytest.raises(ValueError, match="Unsupported file format"):
        parse_file(invalid_file)
