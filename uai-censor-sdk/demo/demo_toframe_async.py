import hashlib
import json
import time
from api.create_to_frame_job import UAICensorCreateAsyncToFrameJobApi
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

bucket = 'bbh'
prefix = 'testprefix'
timestamp = int(time.time())
url = 'http://uai-demo-adam.cn-bj.ufileos.com/face_test.mp4'
interval = 50
callback = 'http://117.50.25.220:3000/'
conf = loadConfig('toframe-config.json')
public_key = conf['public_key']
private_key = conf['private_key']
resource_id = conf['resource_id']
params = {
    'Timestamp': timestamp,
    'Url': url,
    'PublicKey': public_key,
    'ResourceId': resource_id
}
signature = genSignature(private_key, params)
sdk = UAICensorCreateAsyncToFrameJobApi(signature, public_key, resource_id, params['Timestamp'], url, interval, bucket, prefix, callback)
print (sdk.call_api())
