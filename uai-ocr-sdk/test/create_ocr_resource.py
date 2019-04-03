import sys
import json
from api.create_ocr_resource import CreateUAIOcrResourceApi

# usage: python create_async_toframe_job.py config_file='controller-config.json'


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

    resource_types = '0'
    public_key, private_key = load_config(config_file)
    caller = CreateUAIOcrResourceApi(public_key, private_key, resource_types)
    caller.call_api()