from gendiff.formatters.stylish import format_stylish


def format_diff(diff_tree, format_name="stylish"):
    if format_name == "stylish":
        return format_stylish(diff_tree)

    raise ValueError(f"Unsupported format: {format_name}")
