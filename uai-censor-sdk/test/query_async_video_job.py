import sys
import time
from api.get_async_video_job import UAICensorGetAsyncVideoJobApi
from api.utils import gen_signature, load_config

# usage: python query_async_video_job.py config_file='censor-config.json' job_id

if __name__ == '__main__':
    # job_id = sys.argv[1]
    # if job_id == '':
    #     raise ValueError('usage: python query_async_video_job.py job_id')
    if len(sys.argv) == 3:
        config_file = sys.argv[1]
        job_id = sys.argv[2]
    else:
        config_file = 'censor-config.json'
        job_id = sys.argv[1]
    timestamp = int(time.time())
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, job_id=job_id)
    caller = UAICensorGetAsyncVideoJobApi(signature, public_key, resource_id,
                                             timestamp, job_id=job_id)
    caller.call_api()