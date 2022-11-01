import json


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


def json_f(text):
    result = format_keys(text)
    return json.dumps(result, indent=4)
