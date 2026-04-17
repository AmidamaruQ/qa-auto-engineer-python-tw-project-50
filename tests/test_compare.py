from gendiff.scripts.compare import generate_diff, get_diffs_tree


def test_get_diffs_tree_builds_expected_statuses():
    first_data = {
        "follow": False,
        "host": "hexlet.io",
        "timeout": 50,
    }
    second_data = {
        "host": "hexlet.io",
        "timeout": 20,
        "verbose": True,
    }

    assert get_diffs_tree(first_data, second_data) == {
        "follow": {"status": "removed", "value": False},
        "host": {"status": "unchanged", "value": "hexlet.io"},
        "timeout": {"status": "changed", "old_value": 50, "new_value": 20},
        "verbose": {"status": "added", "value": True},
    }


def test_generate_diff_json(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(first_file, second_file) == expected


def test_generate_diff_yaml(test_data_dir):
    first_file = test_data_dir / "file1.yml"
    second_file = test_data_dir / "file2.yml"

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(first_file, second_file) == expected
