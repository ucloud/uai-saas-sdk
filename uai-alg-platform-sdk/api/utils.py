import hashlib


def val_to_str(val):
    if type(val) == bool:
        return 'true' if val is True else 'false'

    if type(val) != list:
        return str(val)

    # if value is type of list, then transform into values split by ','
    val_arr = [val_to_str(item_val) for item_val in val]
    return ','.join(val_arr)


def format_response(rsp, num):
    response = ""
    tag = ""
    for i in range(0,num):
        tag += "\t"

    if type(rsp) is dict:
        response += "\n{0}{{\n".format(tag)
        for k in rsp.keys():
            response += "{0}{1} : {2},\n".format(tag,k,format_response(rsp[k], num+1))
        if response.endswith(",\n"):
            return "{0}\n{1}}}".format(response[0:len(response) -2], tag)
        else:
            return "{0}\n{1}}}".format(response, tag)
    if type(rsp) is list:
        response += "\n{0}[\n".format(tag)
        for v in rsp:
            response += "{0}{1},\n".format(tag, format_response(v, num + 1))
        if response.endswith(",\n"):
            return "{0}\n{1}]".format(response[0:len(response) - 2], tag)
        else:
            return "{0}\n{1}]".format(response, tag)
    if type(rsp) is int or type(rsp) is float:
        return "{0}".format(rsp)
    if type(rsp) is bool:
        return "{0}".format(rsp)
    if not rsp:
        return ""
    else:
        return "{0}".format(rsp.encode('utf-8'))


def gen_signature(private_key, params):
    print('params to gen signature:\n {0}'.format(params))
    items = params.items()
    # must use reverse=False to adapt python3
    items = sorted(items, reverse=False)

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + val_to_str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    # must encode to adapt python3
    sign.update(params_data.encode('utf-8'))
    signature = sign.hexdigest()
    return signature
