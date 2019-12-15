import json


def change_dict_to_json(str_dict):
    return json.dumps(str_dict)


def change_json_to_dict(str_json):
    return json.loads(str_json)


if __name__ == '__main__':
    # codes = {"python": 1001, "java": 1002, "c++": 1003}
    codes = {'python': 1001, 'java': 1002, 'c++': 1003}
    company = '{"huawei": 1000, "alibaba": 1002}'
    print(type(company))
    ret_json = change_dict_to_json(codes)
    ret_dict = change_json_to_dict(company)
    print(type(ret_json))
    print(type(ret_dict))
    print(ret_json)
    print(ret_dict)


