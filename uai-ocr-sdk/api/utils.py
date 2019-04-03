import json
import string
import hashlib


DataStreamUrlPrefix = "http://api.uai.ucloud.cn"
OcrVersion = "v1"
IdcardOcr = "ocr/idcard"

def get_response(rsp, num):
    response = ""
    tag = ""
    for i in range(0,num) :
        tag += "\t"

    if type(rsp) is dict:
        response += "\n{0}{{\n".format(tag)
        for k in rsp.keys():
            response += "{0}{1} : {2},\n".format(tag,k,get_response(rsp[k], num+1))
        if response.endswith(",\n"):
            return "{0}\n{1}}}".format(response[0:len(response) -2], tag)
        else:
            return  "{0}\n{1}}}".format(response, tag)
    if type(rsp) is list:
        response += "\n{0}[\n".format(tag)
        for v in rsp:
            response += "{0}{1},\n".format(tag, get_response(v, num + 1))
        if response.endswith(",\n"):
            return "{0}\n{1}]".format(response[0:len(response) - 2], tag)
        else:
            return "{0}\n{1}]".format(response, tag)
    if type(rsp) is int or type(rsp) is float:
        return "{0}".format(rsp)
    if not rsp:
        return ""
    else:
        return "{0}".format(rsp.encode('utf-8'))

def gen_idcard_ocr_url():
    return string.join([DataStreamUrlPrefix, OcrVersion, IdcardOcr], "/")


def gen_signature(config_file, timestamp, url=''):
    public_key, private_key, resource_id = load_config(config_file)
    params = {
        'Timestamp': timestamp,
        'PublicKey': public_key,
        'ResourceId': resource_id
    }
    if url != '':
        params['Url'] = url
    print('params to gen signature:\n {0}'.format(params))
    items = list(params.items())
    items.sort()
    sign = ""
    for key, val in items:
        sign += str(key) + str(val)
    sign += private_key
    hash_new = hashlib.sha1()
    hash_new.update(sign.encode(encoding='utf-8'))
    return hash_new.hexdigest()


def load_config(config_file):
    with open(config_file, 'r') as fp:
        config_params = json.loads(fp.read())
    public_key = config_params['public_key']
    private_key = config_params['private_key']
    resource_id = config_params['resource_id']
    return public_key, private_key, resource_id


def verfy_ac(private_key, params):
    items = params.items()
    items = sorted(items, reverse=False) # must use reverse=False to adapt python3

    params_data = ""
    for key, value in items:
        params_data = params_data + str(key) + val_to_str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    sign.update(params_data.encode('utf-8')) # must encode to adapt python3
    signature = sign.hexdigest()
    return signature


def val_to_str(val):
    """ Transform value to string
    """
    if type(val) == bool:
        return 'true' if val == True else 'false'

    if type(val) != list:
        return str(val)

    # if value is type of list, then tansform into values split by ','
    val_arr = [val_to_str(item_val) for item_val in val]
    return ','.join(val_arr)
