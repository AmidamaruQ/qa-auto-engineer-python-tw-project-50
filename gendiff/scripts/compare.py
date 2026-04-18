from gendiff.formatters import format_diff
from gendiff.scripts.parser import parse_file


def get_diffs_tree(first_dict, second_dict):
    all_keys = sorted(first_dict.keys() | second_dict.keys())

    diffs = []

    for key in all_keys:
        if key not in first_dict:
            diffs.append(
                {"key": key, "status": "added", "value": second_dict[key]}
            )
        elif key not in second_dict:
            diffs.append(
                {"key": key, "status": "removed", "value": first_dict[key]}
            )
        elif (isinstance(first_dict[key], dict) and
              isinstance(second_dict[key], dict)):
            diffs.append(
                {
                    "key": key,
                    "status": "nested",
                    "children": get_diffs_tree(
                        first_dict[key],
                        second_dict[key],
                    ),
                }
            )
        elif first_dict[key] == second_dict[key]:
            diffs.append(
                {"key": key, "status": "unchanged", "value": first_dict[key]}
            )
        else:
            diffs.append(
                {
                    "key": key,
                    "status": "changed",
                    "old_value": first_dict[key],
                    "new_value": second_dict[key],
                }
            )

    return diffs


def generate_diff(first_file, second_file, format_name="stylish"):
    first_dict = parse_file(first_file)
    second_dict = parse_file(second_file)
    diff_tree = get_diffs_tree(first_dict, second_dict)

    return format_diff(diff_tree, format_name)
