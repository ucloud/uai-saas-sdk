import sys
import time
from api.create_async_video_job import UAICensorCreateAsyncVideoJobApi
from api.utils import gen_signature, load_config


# usage: python create_sync_video_job.py config_file='censor-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = 'censor-config.json'
    url = 'http://uai-demo-adam.cn-bj.ufileos.com/face_test.mp4'
    timestamp = int(time.time())
    scenes = ['porn']
    interval = 25
    callback = ''
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, url=url)
    caller = UAICensorCreateAsyncVideoJobApi(signature, public_key, resource_id,
                                             timestamp, scenes, url, interval, callback)
    caller.call_api()