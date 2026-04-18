import json
import subprocess
import sys


def test_cli_prints_diff(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected_output = (test_data_dir / "expected_cli_output.txt").read_text()
    expected = expected_output.rstrip("\n") + "\n"

    completed = subprocess.run(
        [sys.executable, "-m",
         "gendiff.scripts.gendiff", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout == expected


def test_cli_accepts_stylish_format(test_data_dir):
    first_file = test_data_dir / "file1.yml"
    second_file = test_data_dir / "file2.yml"
    expected_output = (test_data_dir / "expected_cli_output.txt").read_text()
    expected = expected_output.rstrip("\n") + "\n"

    completed = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff",
         "-f", "stylish", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout == expected


def test_cli_accepts_plain_format(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected_output = (
        test_data_dir / "expected_plain_cli_output.txt"
    ).read_text()
    expected = expected_output.rstrip("\n") + "\n"

    completed = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff",
         "-f", "plain", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout == expected


def test_cli_accepts_json_format(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected = json.loads(
        (test_data_dir / "expected_full_tree.json").read_text()
    )

    completed = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff",
         "-f", "json", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert json.loads(completed.stdout) == expected
