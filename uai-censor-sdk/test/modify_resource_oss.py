import sys
import json
from api.modify_censor_resource_oss import ModifyUAICensorResourceOssInfoApi
# from api.utils import load_config

# usage: python get_censor_resource_list.py config_file='toframe-config.json'


def load_config(config_file):
    with open(config_file, 'r') as fp:
        config_params = json.loads(fp.read())
    public_key = config_params['public_key']
    private_key = config_params['private_key']
    return public_key, private_key


if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = '../config_files/controller-config-pre.json'

    resource_id = "uaicensor-fa60dcc1-f705-41ac-9672-3747b7fccf89"
    modify_oss_pubkey = "sdk_modify_oss_pubkey"
    modify_oss_prikey = "sdk_modify_oss_prikey"

    public_key, private_key = load_config(config_file)
    caller = ModifyUAICensorResourceOssInfoApi(resource_id, modify_oss_pubkey, modify_oss_prikey, public_key, private_key)
    caller.call_api()