import hashlib
import sys
import time
import json
from api.get_async_video_job import UAICensorGetAsyncVideoJobApi
def loadConfig(filename):
    ret = {}
    with open(filename, 'r') as fp:
        ret = json.loads(fp.read())
    return ret
def genSignature(prikey, params):
    items = list(params.items())
    items.sort()
    sign = ""
    for key, val in items:
        sign += str(key) + str(val)
    sign += prikey
    print (sign)
    hash_new = hashlib.sha1()
    hash_new.update(sign.encode(encoding='utf-8'))
    return hash_new.hexdigest()

jobid = sys.argv[1]
timestamp = int(time.time())
conf = loadConfig('config.json')
public_key = conf['public_key']
private_key = conf['private_key']
resource_id = conf['resource_id']
params = {
    'Timestamp': timestamp,
    'PublicKey': public_key,
    'ResourceId': resource_id,
    'JobId': jobid
}
signature = genSignature(private_key, params)
sdk = UAICensorGetAsyncVideoJobApi(signature, public_key, resource_id, timestamp, jobid)
print (sdk.call_api())
