def _format_scalar(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def _stringify(value, depth):
    if not isinstance(value, dict):
        return _format_scalar(value)

    lines = ["{"]
    for key, nested_value in value.items():
        indent = " " * (depth * 4)
        lines.append(f"{indent}{key}: {_stringify(nested_value, depth + 1)}")
    lines.append(f'{" " * ((depth - 1) * 4)}}}')
    return "\n".join(lines)


def _build_line(key, value, sign, depth):
    indent = " " * (depth * 4 - 2)
    return f"{indent}{sign} {key}: {value}"


def format_stylish(diff_tree, depth=1):
    lines = ["{"]

    for node in diff_tree:
        key = node["key"]
        status = node["status"]

        match status:
            case "added":
                lines.append(
                    _build_line(
                        key,
                        _stringify(node["value"], depth + 1),
                        "+",
                        depth,
                    )
                )
            case "removed":
                lines.append(
                    _build_line(
                        key,
                        _stringify(node["value"], depth + 1),
                        "-",
                        depth,
                    )
                )
            case "unchanged":
                lines.append(
                    _build_line(
                        key,
                        _stringify(node["value"], depth + 1),
                        " ",
                        depth,
                    )
                )
            case "changed":
                lines.append(
                    _build_line(
                        key,
                        _stringify(node["old_value"], depth + 1),
                        "-",
                        depth,
                    )
                )
                lines.append(
                    _build_line(
                        key,
                        _stringify(node["new_value"], depth + 1),
                        "+",
                        depth,
                    )
                )
            case "nested":
                lines.append(
                    _build_line(
                        key,
                        format_stylish(node["children"], depth + 1),
                        " ",
                        depth,
                    )
                )

    lines.append(f'{" " * ((depth - 1) * 4)}}}')
    return "\n".join(lines)
