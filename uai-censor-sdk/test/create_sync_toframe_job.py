import sys
import time
from api.create_to_frame_job import UAICensorCreateAsyncToFrameJobApi
from api.create_to_frame_job import ToFrameMode_FirstView
from api.utils import gen_signature, load_config

# usage: python create_sync_toframe_job.py config_file='toframe-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = 'toframe-config.json'
    timestamp = int(time.time())
    # url = 'http://uc-live-hls.ipaychat.com/fuliao_live/1000004/playlist.m3u8' # stream
    url = 'http://uai-demo-adam.cn-bj.ufileos.com/face_test.mp4'
    mode = ToFrameMode_FirstView
    bucket = 'bbh.ufile.ucloud.cn'
    prefix = 'sdk-'+str(timestamp)
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, url=url)
    caller = UAICensorCreateAsyncToFrameJobApi(signature, public_key, resource_id,
                                             timestamp, mode, url, bucket, prefix)
    caller.call_api()