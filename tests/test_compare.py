from gendiff.scripts.compare import generate_diff, get_diffs_tree
from gendiff.scripts.parser import parse_file


def test_get_diffs_tree_builds_expected_statuses(test_data_dir):
    first_data = parse_file(test_data_dir / "tree_file1.json")
    second_data = parse_file(test_data_dir / "tree_file2.json")
    expected = parse_file(test_data_dir / "expected_tree.json")

    assert get_diffs_tree(first_data, second_data) == expected


def test_generate_diff_json(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected = (test_data_dir / "expected_diff.txt").read_text().rstrip("\n")

    assert generate_diff(first_file, second_file) == expected


def test_generate_diff_yaml(test_data_dir):
    first_file = test_data_dir / "file1.yml"
    second_file = test_data_dir / "file2.yml"
    expected = (test_data_dir / "expected_diff.txt").read_text().rstrip("\n")

    assert generate_diff(first_file, second_file) == expected


def test_generate_diff_uses_stylish_by_default(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected = (test_data_dir / "expected_diff.txt").read_text().rstrip("\n")

    assert generate_diff(first_file, second_file, "stylish") == expected
