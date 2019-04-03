import sys
import time
import json
from api.get_ocr_resource_record import GetUAIOcrResourceRecordInfoApi
# from api.utils import load_config

# usage: python get_ocr_resource_list.py config_file='controller-config.json'

WeekDuration = 7 * 24 * 60 * 60


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

    curr_time = int(time.time())
    begin_time = curr_time - WeekDuration
    public_key, private_key = load_config(config_file)
    caller = GetUAIOcrResourceRecordInfoApi(begin_time, curr_time, public_key, private_key)
    caller.call_api()
