import sys
from api.create_censor_resource import CreateUAICensorResourceApi
from api.utils import load_config

# usage: python create_async_toframe_job.py config_file='toframe-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = '../config_files/controller-config-pre.json'

    resource_types = '0'
    public_key, private_key, _ = load_config(config_file)
    caller = CreateUAICensorResourceApi(public_key, private_key, resource_types)
    caller.call_api()