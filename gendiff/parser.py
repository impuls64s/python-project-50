import json
import yaml


def why_format(lst1, lst2):
    if lst1[-4:] == lst2[-4:]:
        return lst1[-4:]
    elif lst1[-4:] == '.yml' and lst2[-4:] == 'yaml':
        return 'yaml'
    elif lst1[-4:] == 'yaml' and lst2[-4:] == '.yml':
        return 'yaml'
    else:
        return 'wrong format'


def parsing(file1, file2):
    format = why_format(file1, file2)
    if format == 'json':
        result = {
            'json': (json.load(open(file1)),
                     json.load(open(file2)))
            }
        return result['json']
    elif format == 'yaml' or format == '.yml':
        result = {
            'yaml': (yaml.safe_load(open(file1)),
                     yaml.safe_load(open(file2)))
            }
        return result['yaml']
    else:
        return format
