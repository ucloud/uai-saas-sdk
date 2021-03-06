import sys
import time
from api.create_sync_image_job import UAICensorCreateSyncImageJobApi
from api.utils import gen_signature, load_config

# usage: python create_url_image_job.py config_file='censor-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = 'censor-config.json'
    url = 'http://uai-demo-adam.cn-bj.ufileos.com/adamtest_image.jpg'
    timestamp = int(time.time())
    scenes = ['porn']
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, url=url)
    caller = UAICensorCreateSyncImageJobApi(signature, public_key, resource_id,
                                             timestamp, scenes, url)
    caller.call_api()