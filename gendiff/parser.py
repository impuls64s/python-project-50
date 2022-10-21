import json
import yaml


def why_format(lst1, lst2):
    if lst1[-4:] == 'json' and lst2[-4:] == 'json':
        format = 'json'
    elif ((lst1[-4:] == '.yml' or lst1[-4:] == 'yaml')
          and (lst2[-4:] == '.yml' or lst2[-4:] == 'yaml')):
        format = 'yaml'
    else:
        format = 'wrong format'
    return format


def parsing(file1, file2):
    format = why_format(file1, file2)
    if format == 'json':
        json1 = json.load(open(file1))
        json2 = json.load(open(file2))
        return json1, json2
    elif format == 'yaml':
        yaml1 = yaml.safe_load(open(file1))
        yaml2 = yaml.safe_load(open(file2))
        return yaml1, yaml2
    else:
        return format
