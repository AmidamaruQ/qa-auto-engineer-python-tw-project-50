import subprocess
import sys


def test_cli_prints_diff(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"

    completed = subprocess.run(
        [sys.executable, "-m",
         "gendiff.scripts.gendiff", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""
