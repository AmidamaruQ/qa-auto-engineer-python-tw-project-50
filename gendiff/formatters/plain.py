def _format_plain_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def _walk(diff_tree, parent_path=""):
    lines = []

    for node in diff_tree:
        key = node["key"]
        status = node["status"]
        path = f"{parent_path}.{key}" if parent_path else key

        match status:
            case "added":
                value = _format_plain_value(node["value"])
                lines.append(
                    f"Property '{path}' was added with value: {value}"
                )
            case "removed":
                lines.append(f"Property '{path}' was removed")
            case "changed":
                old_value = _format_plain_value(node["old_value"])
                new_value = _format_plain_value(node["new_value"])
                lines.append(
                    f"Property '{path}' was updated. "
                    f"From {old_value} to {new_value}"
                )
            case "nested":
                lines.extend(_walk(node["children"], path))

    return lines


def format_plain(diff_tree):
    return "\n".join(_walk(diff_tree))
