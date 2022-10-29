def check_dict1(dict1, dict2):
    result = {}
    for k1, v1 in dict1.items():
        if k1 in dict2 and v1 == dict2[k1]:
            result['= ' + k1] = v1
        elif k1 in dict2 and v1 != dict2[k1] and type(v1) is dict:
            for kd, vd in v1.items():
                result['- ' + k1] = {'? ' + kd: vd}
                result['+ ' + k1] = dict2[k1]
        elif k1 in dict2 and v1 != dict2[k1] and type(v1) is not dict:
            result['- ' + k1] = v1
            result['+ ' + k1] = dict2[k1]
        else:
            result['- ' + k1] = v1
    return result


def check_dict2(dict1, dict2):
    result = {}
    for k, v in dict2.items():
        if k not in dict1 and type(v) is dict:
            for kd, vd in v.items():
                result['+ ' + k] = {'? ' + kd: vd + ''}
        elif k not in dict1:
            result['+ ' + k] = v
    return result


def check_value(item1, item2):
    value = {}
    if type(item1) is dict:
        for k1, v1 in item1.items():
            if type(v1) is not dict:
                value.update(check_dict1({k1: v1}, item2))
                value.update(check_dict2(item1, item2))
            elif type(v1) is dict and type(item2[k1]) is not dict:
                for kd, vd in v1.items():
                    value['- ' + k1] = {'? ' + kd: vd}
                    value['+ ' + k1] = item2[k1]
            elif type(v1) is dict and k1 in item2:
                value['= ' + k1] = check_value(v1, item2[k1])
        return value
    else:
        return str(item1)


def item_question(item):
    result = {}
    for key, value in item.items():
        if type(value) is dict and key[0] == '?':
            result[key] = item_question(value)
        elif type(value) is not dict:
            result['? ' + key] = value
        else:
            result['? ' + key] = item_question(value)
    return result


def finish_dict(dict1, dict2):
    res_lvl1 = {}
    for k, v in dict1.items():
        if k in dict2:
            res_lvl1['= ' + k] = check_value(dict1[k], dict2[k])
        else:
            res_lvl1['- ' + k] = item_question(dict1[k])
    for k2, v2 in dict2.items():
        if k2 not in dict1:
            res_lvl1['+ ' + k2] = item_question(v2)
    return res_lvl1


def generate_diff(text1, text2):
    for k, v in text1.items():
        if type(k) is not dict and type(v) is not dict:
            return check_value(text1, text2)
        else:
            res_dict = finish_dict(text1, text2)
        return res_dict
