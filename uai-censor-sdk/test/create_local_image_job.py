import sys
import time
from api.create_sync_image_job import UAICensorCreateSyncImageJobApi
from api.utils import gen_signature, load_config

# usage: python create_local_image_job.py config_file='censor-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = 'censor-config.json'
    file_path = 'test.jpg'
    timestamp = int(time.time())
    scenes = ['porn']
    with open(file_path, 'rb') as fp:
        image = fp.read()
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp)
    caller = UAICensorCreateSyncImageJobApi(signature=signature, public_key=public_key, resource_id=resource_id,
                                             timestamp=timestamp, scenes=scenes, method='file',image=image)
    caller.call_api()