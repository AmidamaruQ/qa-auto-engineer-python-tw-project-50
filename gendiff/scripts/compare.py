from gendiff.scripts.parser import parse_file
from gendiff.utils.formatters import formatter


def get_diffs_tree(first_dict, second_dict):
    all_keys = sorted(first_dict.keys() | second_dict.keys())

    diffs = {}

    for key in all_keys:
        if key not in first_dict:
            diffs[key] = {
                "status": "added",
                "value": second_dict[key]
            }
        elif key not in second_dict:
            diffs[key] = {
                "status": "removed",
                "value": first_dict[key]
            }
        elif first_dict[key] == second_dict[key]:
            diffs[key] = {
                "status": "unchanged",
                "value": first_dict[key]
            }
        else:
            diffs[key] = {
                "status": "changed",
                "old_value": first_dict[key],
                "new_value": second_dict[key]
            }

    return diffs


def generate_diff(first_file, second_file):
    first_dict = parse_file(first_file)
    second_dict = parse_file(second_file)
    diff_tree = get_diffs_tree(first_dict, second_dict)

    return formatter(diff_tree)