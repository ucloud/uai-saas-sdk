import sys
import time
from api.get_to_frame_job import UAICensorGetAsyncToFrameJobApi
from api.utils import gen_signature, load_config

# usage: python query_async_toframe_job.py config_file='toframe-config.json' job_id

if __name__ == '__main__':
    if len(sys.argv) == 3:
        config_file = sys.argv[1]
        job_id = sys.argv[2]
    else:
        config_file = 'toframe-config.json'
        job_id = sys.argv[1]

    timestamp = int(time.time())
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, job_id=job_id)
    caller = UAICensorGetAsyncToFrameJobApi(signature, public_key, resource_id,
                                             timestamp, job_id=job_id)
    caller.call_api()