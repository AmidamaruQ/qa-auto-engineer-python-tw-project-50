
def _format_value(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return str(value)


def formatter(diff_tree):
    result = "{\n"
    for key, value in diff_tree.items():
        status = value.get('status')

        match status:
            case 'added':
                result += f'  + {key}: {_format_value(value["value"])}\n'
            case 'changed':
                result += f'  - {key}: {_format_value(value["old_value"])}\n'
                result += f'  + {key}: {_format_value(value["new_value"])}\n'
            case 'removed':
                result += f'  - {key}: {_format_value(value["value"])}\n'
            case 'unchanged':
                result += f'    {key}: {_format_value(value["value"])}\n'
    result += "}"
    return result
