def formater(item):
    result = {}
    if type(item) is dict:
        for k, v in item.items():
            if type(v) is not dict:
                result[k] = v
                result = dict(sorted(result.items(), key=lambda x: x[0][2:]))
            elif type(v) is dict:
                result[k] = dict(sorted(v.items(), key=lambda x: x[0][2:]))
                formater(v)
    else:
        return item
    return result


def format_keys(item):
    res = {}
    for k, v in item.items():
        res[k] = formater(v)
    return dict(sorted(res.items(), key=lambda x: x[0][2:]))


def format_str(item, char=' ', count=2, depth=1):
    value = '{'
    if type(item) is dict:
        for k, v in item.items():
            if type(v) is dict:
                value = (value + f'\n{char * (depth * count)}{k}: '
                                 f'{format_str(v, char, count, depth+2)}')
            elif type(v) is not dict:
                value = value + f'\n{char * depth * count}{k}: {v}'
        return value + '\n' + char * ((depth * count) - count) + '}'
    else:
        return str(item)


def stylish(text):
    sort_dict = format_keys(text)
    dict_str = format_str(sort_dict)
    result = (dict_str.replace('False', 'false').replace('None', 'null')
                      .replace('True', 'true').replace('=', ' ')
                      .replace('?', ' '))
    return result
